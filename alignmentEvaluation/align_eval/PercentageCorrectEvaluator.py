'''
Created on Feb 24, 2015

@author: joro
'''
from align_eval.ErrorEvaluator import strip_non_lyrics_tokens,\
    loadDetectedTokenListFromMlf, check_num_tokens
import logging
import sys
import os

# file parsing tools as external lib 
parentDir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]) ), os.path.pardir)) 

# pathUtils = os.path.join(parentDir, 'utilsLyrics')
# sys.path.append(pathUtils )
# from utilsLyrics.Utilz import  readListOfListTextFile

def evalPercentageCorrect(annotationURI, outputHTKPhoneAlignedURI, whichTier, startIdx, endIdx ):
    '''
    Wrapper around _evalPercentageCorrect() for txt file outputHTKPhoneAlignedURI
    
    Parameters
    --------------
    outputHTKPhoneAlignedURI: detected timestamps in htk's mlf format 
    
    other parameters same as in _evalPercentageCorrect
    '''
    
    detectedTokenList = loadDetectedTokenListFromMlf( outputHTKPhoneAlignedURI, whichTier )
    
    annotationTokenList, detectedTokenList, finalTsAnno,  initialTimeOffset = \
     strip_non_lyrics_tokens(annotationURI, detectedTokenList, whichTier, startIdx, endIdx)
    
    durationCorrect, totalDuration = _eval_percentage_correct(annotationTokenList, detectedTokenList, finalTsAnno, initialTimeOffset)
    return durationCorrect, totalDuration


def _eval_percentage_correct(reference_token_list,
                             detected_token_List,
                             final_ts_anno,
                             initial_time_offset_refs=0,
                             reference_labels=None):
    '''
    Calculate percentage of duration of correctly aligned tokens as suggested in
    Fujihara: LyricSynchronizer: Automatic Synchronization System Between Musical Audio Signals and Lyrics
    Does not check token identities, but proceeds successively one-by-one  
    Makes sure number of detected tokens (not counting special tokens sp, sil ) is same as number of annotated tokens 

    token: could be 
    - phoneme (consists of one subtoken -phoneme itself),
    - word (consists of one subtoken -word itself) or 
    - phrase (consist of subtokens words ) 


    Parameters
    -------------- 
    detected_token_List: list [[]]
        a list of triples: (startTs, endTs, word) detections 
    
    reference_token_list: list [[]]
        a list of triples: (startTs, endTs, word) reference annotations
    
    final_ts_anno: float
        timestamps of last annotated token (e.g. last timestamp) 
        
    
    '''
    
    # WoRKAROUND. because currenty I dont store final sil in detected textFile .*Aligned 

    currAnnoTsAndToken, num_tokens_in_phrase = \
        check_num_tokens(reference_token_list, detected_token_List, reference_labels)
    
    durationCorrect = 0
    finalTsDetected = detected_token_List[-1][1]

    currentWordNumber = 0
    # evaluate: loop in tokens of gr truth reference annotation
    for idx, currAnnoTsAndToken in enumerate(reference_token_list):
        
        durationCorrectCurr = calcCorrect(detected_token_List,
                                          reference_token_list,
                                          idx, currentWordNumber,
                                          num_tokens_in_phrase[idx],
                                          final_ts_anno,
                                          finalTsDetected)
        durationCorrect += durationCorrectCurr
        
        #### UPDATE: proceed in detection the number of subtokens in current token
        currentWordNumber += num_tokens_in_phrase[idx]

    #  total length of annotated part, because non-vocal regions at end and beginning are not considered in results
    totalLength = float(final_ts_anno) - initial_time_offset_refs

    return durationCorrect, totalLength


def calcCorrect(detectedTokenListNoPauses, annotationTokenListNoPauses, idx, currentWordNumber, numWordsInPhrase, finallTsAnno, finalTsDetected)  :
#     phrase overlap correct
    currBeginAnno = float(annotationTokenListNoPauses[idx][0])
    currEndAnno = float(annotationTokenListNoPauses[idx][1])

    currBeginDetected  = detectedTokenListNoPauses[currentWordNumber][0]
    currEndDetected = detectedTokenListNoPauses[currentWordNumber + numWordsInPhrase - 1][1]
    
    correct = max(0,min(currEndAnno,currEndDetected) - max(currBeginAnno, currBeginDetected))

#     silence overlap correct
    if idx !=  (len(annotationTokenListNoPauses) - 1):
        nextBeginAnno = float(annotationTokenListNoPauses[idx+1][0])
        
        if currentWordNumber + numWordsInPhrase > len(detectedTokenListNoPauses) -1 :
            sys.exit("length of list of deteceted tokens = {} differes from len of tokens in annotation {}".format(len(detectedTokenListNoPauses),currentWordNumber + numWordsInPhrase ))
        nextBeginDetected = detectedTokenListNoPauses[currentWordNumber + numWordsInPhrase][0]
        correct += max(0,min(nextBeginAnno,nextBeginDetected) - max(currEndAnno, currEndDetected))
    else:
        if (currEndAnno > finalTsDetected):  
            pass
#             sys.exit("currEndAnno > finalTsDetected")
        if (currEndDetected > finallTsAnno ):
            # WORKAROUND
            logging.warn("currEndDetected {} > finallTsAnno {}".format(currEndDetected, finallTsAnno))
            currEndDetected = finallTsAnno
        
        correct += max(0, min(finallTsAnno,finalTsDetected) - max(currEndAnno, currEndDetected))
        
    return correct

