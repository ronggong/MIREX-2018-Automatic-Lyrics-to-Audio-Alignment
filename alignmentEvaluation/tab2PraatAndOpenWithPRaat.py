'''
Created on Apr 3, 2014

@author: joro
'''
import sys
import subprocess
import os
import logging
from align_eval.PraatVisualiser import openTextGridInPraat, PATH_TO_PRAAT
from align_eval.PraatVisualiser import tokenList2TabFile
from align_eval.ErrorEvaluator import loadDetectedTokenListFromMlf

#used to open detected result only in TextGrid. after alignemnt algorithm is run.

parentDir = os.path.abspath(os.path.dirname(os.path.realpath(__file__ ) ) )
PATH_TO_PRAAT_SCRIPT= os.path.join(parentDir, 'tab2TextGrid.rb')


   
def tab2PraatAndOpenWithPRaat(argv):    
    if len(argv) != 2  :
            print ("usage: {}  <URItsvFileWithExtension>".format(argv[0]) )
            sys.exit();
    
    dirName =  os.path.dirname(argv[1])
    baseName = os.path.basename(argv[1])
    fileName = os.path.splitext(baseName)[0]
    ext = os.path.splitext(baseName)[1]
    
    if not os.path.exists(PATH_TO_PRAAT):
        logging.warning("Praat not found at given path {}, skipping opening Praat ..\n")
        return
    
    textGridURI =  os.path.join(dirName, fileName)  +  '.TextGrid'
    if not os.path.isfile(textGridURI):
        sys.exit("TextGrid file {} does not exist".format(textGridURI))

    
    comparisonTextGridURI =  os.path.join(dirName, fileName)  + ext + 'TextGrid'
    if os.path.isfile(comparisonTextGridURI):
        raw_input("there is already a file {}! You may overwrite it! \n do you want to proceed? ".format(comparisonTextGridURI))
        
    command = [PATH_TO_PRAAT, PATH_TO_PRAAT_SCRIPT, dirName, fileName, ext]
    pipe = subprocess.Popen(command)
    pipe.wait()
        
    # open newly-created .TextGrid in  praat. OPTIONAL
    audio_URI = os.path.join(dirName, fileName)  + '.wav'
    openTextGridInPraat(dirName, fileName, audio_URI)
    
    
if __name__ == '__main__':
    tab2PraatAndOpenWithPRaat(sys.argv)
    
    # example:
#     python /Users/joro/Documents/Phd/UPF/voxforge/myScripts/AlignmentEvaluation/tab2PraatAndOpenWithPRaat.py /Users/joro/Documents/Phd/UPF/turkish-makam-lyrics-2-audio-test-data-synthesis/muhayyerkurdi--sarki--duyek--ruzgar_soyluyor--sekip_ayhan_ozisik_short/1-05_Ruzgar_Soyluyor_Simdi_O_Yerlerde/ 1-05_Ruzgar_Soyluyor_Simdi_O_Yerlerde_2_zemin_from_16_459_to_38_756510 .wordsDurationSynthAligned
 