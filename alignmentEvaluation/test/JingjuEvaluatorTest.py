'''
Created on Jun 30, 2015

@author: joro
'''
import os
from align_eval.AccuracyEvaluator import _evalPercentageCorrect
import sys

# file parsing tools as external lib 
parentDir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]) ), os.path.pardir, os.path.pardir)) 

if parentDir not in sys.path:
      sys.path.append(parentDir)
pathUtils = os.path.join(parentDir, 'utilsLyrics')

    
    

def evalAccuracyTest_jingju_old():

######### for test logic see ErrorEvaluator instead

    PATH_TEST_DATASET = '../example/'
      
    annotationURI = os.path.join(PATH_TEST_DATASET,  'grTruth.TextGrid')
    
    #  load from file
#     detectedURI = os.path.join(PATH_TEST_DATASET,  audioName +  '.phrasesDurationAligned')
    detectedTokenList = readListOfListTextFile(os.path.join(PATH_TEST_DATASET,  'detected.aligned'))
    
    
    ###############
    annotationURI = '/Users/joro/Documents/Phd/UPF/arias_dev_01_t_70//laosheng-erhuang_04.TextGrid'
    
    detectedTokenList = readListOfListTextFile('/Users/joro/Documents/Phd/UPF/arias_dev_01_t_70/laosheng-erhuang_04_49.8541936425_108.574785469.syllables')
    startIdx=1; endIdx=13
    
    #################
    annotationURI = '/Users/joro/Documents/Phd/UPF/arias_dev_01_t_70/laosheng-erhuang_04.TextGrid'
    detectedTokenList = readListOfListTextFile('/Users/joro/Documents/Phd/UPF/arias_dev_01_t_70/laosheng-erhuang_04_134.647686205_168.77679257.syllables')
    startIdx=15; endIdx=26

    
    whichTier=3
    durationCorrect, totalLength  = _evalPercentageCorrect(annotationURI, detectedTokenList, whichTier , startIdx, endIdx)
    print durationCorrect
    print totalLength
    print durationCorrect/totalLength

if __name__ == '__main__':
    evalAccuracyTest_jingju_old()
    