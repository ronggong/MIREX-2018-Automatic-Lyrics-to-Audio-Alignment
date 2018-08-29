# -*- coding: utf-8 -*-
"""
Created on Mar 5, 2014

This metric is strict, because an error might be counted twice if end and begin of consecutive tokens coincide. 
This happens when there is no silent pause between tokens both in annotation and detected result. 
This is similar to proposed by shriberg on sentence boundary detection.  
@author: joro
"""

import sys
import numpy
from align_eval.PraatVisualiser import mlf2PhonemesAndTsList
from align_eval.PraatVisualiser import mlf2WordAndTsList
from parse.TextGrid_Parsing import tierAliases
from parse.TextGrid_Parsing import tier_names
from parse.TextGrid_Parsing import readNonEmptyTokensTextGrid
from align_eval.Utilz import getMeanAndStDevError


ANNOTATION_EXT = '.TextGrid'
DETECTED_EXT = '.dtwDurationsAligned'
AUDIO_EXT = '.wav'


def determine_suffix_old(with_duration, with_synthesis, eval_level):
    '''
    
    lookup suffix for result files  depending on which algorithm used
    '''    
    eval_level_token = tier_names[eval_level]
    if with_duration:
        if with_synthesis:
            token_aligned_suffix =  '.' + eval_level_token + 'DurationSynthAligned'
            phonemes_aligned_suffix = '.phonemesDurationSynthAligned'
        else:
            token_aligned_suffix = '.' + eval_level_token + 'DurationAligned'
            phonemes_aligned_suffix = '.phonemesDurationAligned'
    else:
        token_aligned_suffix = '.' + eval_level_token + 'Aligned'
        phonemes_aligned_suffix = '.phonemesAligned'
    return token_aligned_suffix, phonemes_aligned_suffix


'''
calculate evaluation metric
For now works only with begin ts
@deprecated
'''


def words_list_2_avrg_txt(annotation_word_list, detected_word_list):
    
    sum_differences = 0;
    matched_word_counter = 0;
    
    # parse annotation word ts and compare each with its detected
    for tupleWordAndTs in annotation_word_list:
        for tupleDetectedWordAndTs in  detected_word_list:
            
            if tupleWordAndTs[1] == tupleDetectedWordAndTs[1]:
                currdifference = abs(float(tupleWordAndTs[0]) - float(tupleDetectedWordAndTs[0]))
                matched_word_counter +=1
                sum_differences = sum_differences + currdifference
                # from beginning of list till first matched word
                break
    return sum_differences/matched_word_counter


def evalAlignmentError(annotationURI, detectedURI, whichLevel, startIdx, endIdx ):
    '''reads detected from htk mlf
    @param detectedURI: URI of htk-mlf format
    @param annotationURI: URI of Praat annotaiton textgrid. 
    @param whichLevel, 0- phonemeLevel, 1 -wordLevel,  2 - phraseLevel. The level at which to compare phrases 
    reads only the layer from with name correspondingly phonemes, words or phrases

    
    '''
    detectedTokenList = loadDetectedTokenListFromMlf( detectedURI, whichLevel=2 )
    
    annotation_Token_List_NoPauses, detected_Token_List_noPauses, dummy, dummy, dummyInitialiTimeOffset = strip_non_lyrics_tokens(annotationURI, detectedTokenList, whichLevel, startIdx, endIdx)

    evalErrors = _eval_alignment_error(annotation_Token_List_NoPauses, detected_Token_List_noPauses)
    return evalErrors


def loadDetectedTokenListFromMlf( detectedURI, whichLevel=2 ):

    ####################### 
    # # prepare list of phrases/phonemes from DETECTED:
    if whichLevel == tierAliases.phonemes:
        detectedTokenList= mlf2PhonemesAndTsList(detectedURI)
    elif whichLevel == tierAliases.words or whichLevel == tierAliases.phrases or whichLevel == tierAliases.pinyin :
        detectedTokenList= mlf2WordAndTsList(detectedURI)
    else:
        sys.exit("level could be only phoneme- or word- or syllable_pinyin-level")
    
    detectedTokenListNoPauses = []    
    for token in detectedTokenList:
        if token[2] != 'REST':
            detectedTokenListNoPauses.append(token)
                
    return detectedTokenListNoPauses


def split_into_tokens(annotation_tokens):
    '''
    Split annotated phrases (having more than one word/syllable)  by white spaces into text 
    
    Parameters
    ------------
    
    annotation_tokens: list of list
         tokens (phrase, consisting of 1 or more words or syllables) with their belonging annotated timestamps 
         
         
         
    Returns
    --------------
    num_tokens_in_all_phrases: list
        number of subtokens (words, syllables) in all tokens (phrases)  
    
    currAnnoTsAndToken: list
        last token and its timestamp
        
    
    '''
    
    num_tokens_in_all_phrases = []
    
    for currAnnoTsAndToken in annotation_tokens:
        if type(currAnnoTsAndToken) == str: #  the text itself
            txtToken = currAnnoTsAndToken
        else:                                
            txtToken = currAnnoTsAndToken[-1]    # assume the text is the last entry of a token
        txtToken = txtToken.strip()
        
        subtokens = txtToken.split()
        num_tokens_in_phrase = len(subtokens)
        if num_tokens_in_phrase == 0:
            sys.exit('token (phrase) with no subtokens (words) in annotation file!')
        num_tokens_in_all_phrases.append(num_tokens_in_phrase)
    
    return num_tokens_in_all_phrases, currAnnoTsAndToken


def _eval_alignment_error(reference_token_list,
                          detected_token_List,
                          reference_labels=None,
                          use_end_ts=False):
    """
    Calculate alignment errors. Does not check token identities, but proceeds successively one-by-one  
    Make sure number of detected tokens (without counting sp, sil ) is same as number of annotated tokens

    for description see related method: PercentageCorrectEvaluator._evalPercentageCorrect
    """
    alignment_errors = []

    curr_anno_ts_and_token, num_tokens_in_phrase = check_num_tokens(reference_token_list,
                                                                    detected_token_List,
                                                                    reference_labels)
    
    current_num_tokens = 0

    # evaluate: loop in tokens of gr truth reference annotation
    for idx, curr_anno_ts_and_token in enumerate(reference_token_list):
        
        if num_tokens_in_phrase[idx] == 0:
            sys.exit('token (phrase) with no sub-tokens (words) in annotation file!')
        
        if current_num_tokens >= len(detected_token_List):
            sys.exit(' number of tokens in annotation {} differs from  num tokens detected {}. No evaluation possible'.format(current_num_tokens, len(detected_token_List)))

        begin_alignment_error, end_alignment_error = \
            calcErrorBeginAndEndTs(detected_token_List,
                                   curr_anno_ts_and_token,
                                   current_num_tokens,
                                   num_tokens_in_phrase[idx])

        alignment_errors.append(begin_alignment_error)

        # end timestamp of each token considered, too.
        # this makes sense when inter-word silences/instrumentals are present.
        if use_end_ts:
            alignment_errors.append(end_alignment_error)
        
        # UPDATE: proceed in detection the number of subtokens in current token.
        current_num_tokens += num_tokens_in_phrase[idx]

    return alignment_errors


def _eval_percentage_tolerance(ref_intervals,
                               detected_intervals,
                               reference_labels=None,
                               tolerance=0.3):

    alignment_errors = _eval_alignment_error(reference_token_list=ref_intervals,
                                             detected_token_List=detected_intervals,
                                             reference_labels=reference_labels)
    num_correct = 0
    for err in alignment_errors:
        if abs(err) <= tolerance:
            num_correct += 1
    return num_correct / float(len(ref_intervals))


def strip_non_lyrics_tokens(annotationURI, detectedTokenList, whichTier, startIdx, endIdx):
    
    '''
    
    prepare list of tokens. remove detected tokens NOISE, sil, sp entries from  detectedTokenList and annoTokenList

    Parameters
    ------------------------
    whichTier: 
        works only with the tier from TextGrid_Parsing  tier_names = ["phonemes", 'words', "phrases", "lyrics-syllables-pinyin", 'sections'];
    startIdx: int
         index of boundary in tier to be considered as start one  (from TextGrid -1 )
    endIdx: int
         index of end token
    '''
    annotationTokenListA, annotationTokenListNoPauses =  readNonEmptyTokensTextGrid(annotationURI, whichTier, startIdx, endIdx)

    for currDetectedTsAndToken in detectedTokenList:
        currDetectedTsAndToken[0] = float(currDetectedTsAndToken[0])
        currDetectedTsAndToken[1] = float(currDetectedTsAndToken[1])

    detectedTokenListNoPauses = []  #result
    for currDetectedTsAndToken in detectedTokenList:

        if currDetectedTsAndToken[2] != 'sp' and currDetectedTsAndToken[2] != 'sil' and currDetectedTsAndToken[2] != 'NOISE' and currDetectedTsAndToken[2] != 'REST':
            detectedTokenListNoPauses.append(currDetectedTsAndToken)
    
    for token in annotationTokenListNoPauses:
        token = token[0]

    initialTimeOffset = annotationTokenListA[0][0]
    return annotationTokenListNoPauses, detectedTokenListNoPauses, float(annotationTokenListA[-1][1]), initialTimeOffset


def check_num_tokens(reference_token_list, detected_Token_List, reference_labels=None):
    '''
    Sanity Check of number of  tokens in reference and detection 
    '''
    if len(reference_token_list) == 0:
        sys.exit(reference_token_list + ' is empty! Check code')
    if len(detected_Token_List) == 0:
        sys.exit(' detected token list is empty! Check code')
    
    # divide phrases into tokens
    if reference_labels != None: # labels of reference tokens given separately
        num_tokens_in_phrase, currAnnoTsAndToken = split_into_tokens(reference_labels)
    else:
        num_tokens_in_phrase, currAnnoTsAndToken = split_into_tokens(reference_token_list) # labels should be the last field of reference_token_list
        
    # check that annotation and detection have same number of tokens
    if sum(num_tokens_in_phrase) != len(detected_Token_List):
        sys.exit(' number of tokens in annotation {} differs from  num tokens detected {}. No evaluation possible'.format(sum(num_tokens_in_phrase), len(detected_Token_List)))

    return currAnnoTsAndToken, num_tokens_in_phrase


def calcErrorBeginAndEndTs(detectedTokenListNoPauses, annoTsAndToken, currentWordNumber, numWordsInPhrase):
    '''
    @param annoTsAndToken: - might have 1 or more tokens 
    @param detectedTokenListNoPauses:  list of tokens. here reference only the relevant beginning and ending tokens
    '''
    # calc difference phrase begin Ts
    annotatedTs = annoTsAndToken[0]
    detectedTs = detectedTokenListNoPauses[currentWordNumber][0]
    beginAlignmentError = calcError(annotatedTs, detectedTs)
    
    # calc difference phrase endTs (1)
    annotatedTs = annoTsAndToken[1]
    detectedTs = detectedTokenListNoPauses[currentWordNumber + numWordsInPhrase - 1][1]
    endAlignmentError = calcError(annotatedTs, detectedTs)
    
    return beginAlignmentError, endAlignmentError


def calcError(annotatedTokenTs, detectedTokenTs):
    '''
    abs error btw a token form anno and detected 
    '''
    currAlignmentError = float(annotatedTokenTs) - float(detectedTokenTs)
    currAlignmentError = numpy.round(currAlignmentError, decimals=2)
    return currAlignmentError      
    

def evalOneFile(argv):
    ''' Main utility function
    '''

    if len(argv) != 5:
        print ("usage: {} <URI_annotation> <URI_detected> <evalLevel> <URI_audio>".format(argv[0]))
        sys.exit()

    annoURI = argv[1]
    detectedURI = argv[2]
    evalLevel = int(argv[3])
    audio_URI = argv[4]
    alignmentErrors  = evalAlignmentError(annoURI , detectedURI  , evalLevel)

    mean, stDev, median = getMeanAndStDevError(alignmentErrors)
    print("mean : ", mean, "st dev: " , stDev)

    return mean, stDev,  median, alignmentErrors

