'''
Tools to parse output of alignment and visualise results in Praat 
Created on Nov 27, 2014

@author: joro
'''
import sys
import os
import logging
import shutil
import subprocess

# change path to where Praat is installed
PATH_TO_PRAAT = '/Applications/Praat.app/Contents/MacOS/Praat'

parentDir = os.path.abspath(os.path.dirname(os.path.realpath(__file__ ) ) )
PATH_TO_PRAAT_SCRIPT= os.path.join(parentDir, 'loadAlignedResultAndTextGrid.rb')


HTK_MLF_ALIGNED_SUFFIX= ".htkAlignedMlf"
 
ANNOTATION_EXT = '.TextGrid'

# utils to do reading and writing into text files  
parentDir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__) ), os.path.pardir)) 
pathUtils = os.path.join(parentDir, 'utilsLyrics')
if pathUtils not in sys.path:
    sys.path.append(pathUtils )

from align_eval.Utilz import writeListOfListToTextFile
from align_eval.Utilz import loadTextFile

def prepareOutputForPraat(outputHTKPhoneAlignedURI, wordAlignedSuffix, phonemeAlignedSuffix):
        '''
        parse output in HTK's mlf output format ; load into list; 
        serialize into table format easy to load from praat: 
        -in word-level 
        and 
        - phoneme level
        
        '''    
    ################ parse mlf and write word-level text file    
       
        listTsAndWords = mlf2WordAndTsList(outputHTKPhoneAlignedURI)
        
        
        baseNameAudioFile = os.path.splitext(outputHTKPhoneAlignedURI)[0]
        wordAlignedfileName=  tokenList2TabFile(listTsAndWords, baseNameAudioFile, wordAlignedSuffix)
    
      
    ########################## same for phoneme-level: 
        
        # with : phoneme-level alignment
        listTsAndPhonemes = mlf2PhonemesAndTsList (outputHTKPhoneAlignedURI)
        phonemeAlignedfileName=  tokenList2TabFile(listTsAndPhonemes, baseNameAudioFile, phonemeAlignedSuffix)
        
        
        
        return wordAlignedfileName, phonemeAlignedfileName


def tokenList2TabFile( listTsAndPhonemes,  baseNameAudioFile, whichSuffix):
    '''
    convenience method. 
    '''
    
    # timeshift
#     for index in range(len(listTsAndPhonemes)):
#         listTsAndPhonemes[index][0] +=  timeShift
#         listTsAndPhonemes[index][1] +=  timeShift

#         if (len(listTsAndPhonemes[index]) == 3): mlf-caused issue
#             del listTsAndPhonemes[index][1]
        
    phonemeAlignedfileName = baseNameAudioFile + whichSuffix
    
    writeListOfListToTextFile(listTsAndPhonemes, 'startTs endTs phonemeOrWord\n', phonemeAlignedfileName)
    logging.debug('phoneme level alignment written to file: ',  phonemeAlignedfileName)
    return phonemeAlignedfileName

    
    
def addAlignmentResultToTextGrid(detectedTokenList,  grTruthAnnoURI, tokenAlignedSuffix):
    '''
    same as addAlignmentResultToTextGrid_htk, but
    instead of file with outputHTKPhoneAlignedURI use python list: @param detectedTokenList
    '''
    baseNameAudioFile = os.path.splitext(grTruthAnnoURI)[0]
    tokenAlignedfileName=  tokenList2TabFile(detectedTokenList, baseNameAudioFile, tokenAlignedSuffix)
    
    alignedResultPath, fileNameWordAnno = _alignmentResult2TextGrid(grTruthAnnoURI, tokenAlignedfileName)  
    return alignedResultPath, fileNameWordAnno               


def addAlignmentResultToTextGrid_htk( outputHTKPhoneAlignedURI, grTruthAnnoURI, wordAlignedSuffix, phonemeAlignedSuffix):
    '''
    called when HTK used and output written in mlf file
    @param outputHTKPhoneAlignedURI- output htk mlf format
    '''
   
    
    wordAlignedfileName, phonemeAlignedfileName = prepareOutputForPraat(outputHTKPhoneAlignedURI, wordAlignedSuffix, phonemeAlignedSuffix)
    
    alignedResultPath, fileNameWordAnno = _alignmentResult2TextGrid(grTruthAnnoURI, wordAlignedfileName, phonemeAlignedfileName)
    return alignedResultPath, fileNameWordAnno 
    

    '''
    call Praat script to: 
    -open phoneLevel.annotation file  .TextGrid
    -open the result alignemnt  
    -add the result as tier in the TextGrid
    -save the new file as .comparison.TextGrid
    
    '''
    

def addDetectionToAnnotationTextGrid(wordAlignedfileName, alignedResultPath, fileNameWordAnno):
    tokens_ = os.path.splitext(os.path.basename(wordAlignedfileName))
    alignedFileBaseName = tokens_[0]
    alignedSuffix = tokens_[1]
# in praat script extensions  alignedSuffix  is added automatically. use suffixName as tierName
    
    if not os.path.exists(PATH_TO_PRAAT):
        logging.warning("Praat not found at given path {}, skipping opening Praat ..\n")
        return
    command = [PATH_TO_PRAAT, PATH_TO_PRAAT_SCRIPT, alignedResultPath, fileNameWordAnno, alignedFileBaseName, alignedSuffix, '"' + alignedSuffix + '"']
    pipe = subprocess.Popen(command)
    pipe.wait()
#     return tokens_, alignedFileBaseName, alignedSuffix, command, pipe

def _alignmentResult2TextGrid(grTruthAnnoURI, wordAlignedfileName, phonemeAlignedfileName="" ):
    '''
    create a tier from list with detections @param wordAlignedfileName and add it to TextGrid grTruthAnnoURI
    '''
    if not os.path.exists(grTruthAnnoURI):
        sys.exit(" ground truth annotation file {} does not exist. cannot add alignment to it ".format (grTruthAnnoURI))
        
     
    ########### call praat script to add alignment as a new layer to existing annotation TextGrid
    alignedResultPath = os.path.dirname(wordAlignedfileName)
    
    
    # copy  annotation TExtGrid to path of results
    dirNameAnnotaion = os.path.dirname(grTruthAnnoURI)
    if (dirNameAnnotaion != alignedResultPath):
        shutil.copy2(grTruthAnnoURI,alignedResultPath )
     
    fileNameWordAnno = os.path.splitext(os.path.basename(grTruthAnnoURI))[0]

    ########################
    # WORD result   
    addDetectionToAnnotationTextGrid(wordAlignedfileName, alignedResultPath, fileNameWordAnno)
    
    ###########################
    # PHONEME result
    if phonemeAlignedfileName != '':
        addDetectionToAnnotationTextGrid(phonemeAlignedfileName, alignedResultPath, fileNameWordAnno)

    
    return alignedResultPath, fileNameWordAnno
    
    
def openTextGridInPraat(alignedResultPath, fileNameWordAnno, pathToAudioFile):
    '''     open Praat to visualize it (done for MAC OS X)
    '''
    print(PATH_TO_PRAAT)
    if not os.path.exists(PATH_TO_PRAAT):
        logging.warning("Praat not found at given path {}, skipping opening Praat ..\n")
        return
    
    comparisonTextGridURI =  os.path.join(alignedResultPath, fileNameWordAnno)  + ANNOTATION_EXT
    pipe = subprocess.Popen(["open", '-a', PATH_TO_PRAAT, comparisonTextGridURI])
    pipe.wait()
    
    # and audio

    pipe = subprocess.Popen(["open", '-a', PATH_TO_PRAAT, pathToAudioFile])
    pipe.wait()



def mlf2PhonemesAndTsList(inputFileName):
    '''
    parse output of alignment in mlf format ( with words) 
    output: phonemes with begin and end ts 
    
    # TODO: change automatically extension from txt to mlf
    
    ''' 
    
    allLines = loadTextFile(inputFileName)
    
    
    listPhonemesAndTs = []
    prevStartTime = -1    
    
    
    # when reading lines from MLF, skip first 2 and last
    for line in allLines[2:-1]:
        
        tokens =  line.split(" ")

        startTime = float(tokens[0])/10000000
        
        endTime = float(tokens[1])/10000000
        
        # if Praat does not allow insertion of new token with same timestamp. This happend when prev. token was 'sp'. So remove it and insert current
        if (prevStartTime == startTime):
            listPhonemesAndTs.pop()
            
        
        phoneme = tokens[2].strip()
        
        
        listPhonemesAndTs.append([startTime,endTime,  phoneme])
        
        # remember startTime 
        prevStartTime = startTime
         
    return listPhonemesAndTs
    
    

    
def mlf2WordAndTsList(inputFileName):
        
    '''
    parse output of alignment in mlf format ( with words) 
    output: words with begin and end ts 
    NOTE: length of tokens=5 if no -o option is set on HVite
    TODO: change automatically extension from txt to mlf
    ''' 
    
    extracedWordList = []
    
    LENGTH_TOKENS_NEW_WORD= 5
    
    allLines = loadTextFile(inputFileName)
    
    # skip first two control lines and last . 
    listWordsAndTs = allLines[2:-1]
        
    currentTokenIndex = 0    
    tokens =  listWordsAndTs[currentTokenIndex].split(" ")
    lastLineReached = 0
    
    while currentTokenIndex <= len(listWordsAndTs):
        
        # get begin ts 
        if len(tokens) == LENGTH_TOKENS_NEW_WORD:
            startTime = float(tokens[0])/10000000
            wordMETU = tokens[-1].strip()
        
        # move to next        
        prevTokens = tokens 
        currentTokenIndex += 1
        
        # sanity check
        if currentTokenIndex >= len(listWordsAndTs):
            endTime =  float(tokens[1])/10000000
            extracedWordList.append([startTime, endTime, wordMETU])     
 
            break
        
        tokens =  listWordsAndTs[currentTokenIndex].split(" ")
        
        # fast forward phonemes while end of word
        while len(tokens) == LENGTH_TOKENS_NEW_WORD - 1 and currentTokenIndex < len(listWordsAndTs):
            
            # end of word is last phoneme before 'sp' 
            if tokens[2]=="sp":
                # move to next
                currentTokenIndex += 1
                if currentTokenIndex < len(listWordsAndTs):
                    tokens =  listWordsAndTs[currentTokenIndex].split(" ")

                break
            
            prevTokens = tokens 
            currentTokenIndex += 1
            if currentTokenIndex < len(listWordsAndTs):
                tokens =  listWordsAndTs[currentTokenIndex].split(" ")
            else:
                lastLineReached = 1;
        
        # end of word. after inner while loop  
        if not lastLineReached:
            endTime =  float(prevTokens[1])/10000000
            extracedWordList.append([startTime, endTime, wordMETU])     
        
    return extracedWordList    
    