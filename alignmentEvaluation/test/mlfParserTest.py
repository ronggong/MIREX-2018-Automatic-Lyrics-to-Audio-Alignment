'''
Created on Dec 1, 2015

@author: joro
'''
from align_eval.PraatVisualiser import ANNOTATION_EXT
from align_eval.ErrorEvaluator import DETECTED_EXT, AUDIO_EXT, tierAliases,\
    loadDetectedTokenListFromMlf
import os


########## 1 example with detected mlf file: 
def loadDetectedTokenListFromMlfTest():
    PATH_TEST_DATASET = '../example/'
       
    audioName = '01_Bakmiyor_3_nakarat'
#     annotationURI = os.path.join(PATH_TEST_DATASET,  audioName + ANNOTATION_EXT)
    detectedHTK_URI = os.path.join(PATH_TEST_DATASET,  audioName +  DETECTED_EXT)
    detectedHTK_URI = '/Users/joro/Documents/Phd/UPF/JingjuSingingAnnotation/lyrics2audio/praat/shiwenhui_tingxiongyan_30.3531146852_61.6663629537.out.mlf'
#     audioURI = os.path.join(PATH_TEST_DATASET,  audioName + AUDIO_EXT)
    whichEvalLevel = tierAliases.words
   
      # load result from file into python list
    detectedTokenList = loadDetectedTokenListFromMlf( detectedHTK_URI, whichEvalLevel )
    print detectedTokenList
    
#     mean, stDev,  median, alignmentErrors  = evalOneFile([__file__, annotationURI, detectedURI, tierAliases.wordLevel, audioURI ])

if __name__ == '__main__':
    loadDetectedTokenListFromMlfTest()