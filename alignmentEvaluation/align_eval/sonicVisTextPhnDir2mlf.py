'''
Created on Feb 5, 2014

@attention: not working just put here if SonicVis needed
Converts from .lab format: tuple (phoneme and timestamp) 
(as used e.g. by  sonic visualizer ) to mlf. 
Currently adjusted according to syllablingDB
@author: joro
'''

import os
import sys
# utilLyrics is a separate project

parentDir = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]) ), os.path.pardir)) 
pathUtils = os.path.join(parentDir, 'utilsLyrics')
sys.path.append(pathUtils )

if pathUtils not in sys.path:
    sys.path.append(pathUtils)

listVocals = ['AA', 'A', 'E', 'EE', 'O', 'IY', 'I', 'U', 'UE' , 'OE' ,  'sil']




def sonicVisText2mlf(inputFileName, outputFileHandle):
    ''' convert from
     SV text format:
      0.000000000    sil
     to .mlf format
     @param: inputFileName- abs file path and name
    '''
    
    inputFileHandle = open(inputFileName)
   
    
    inputFileBaseName = os.path.basename(inputFileName)
    nameAndExt = os.path.splitext(inputFileBaseName)
    outputFileHandle.write  ("\"*/")
    outputFileHandle.write  (nameAndExt[0])
    outputFileHandle.write  (".lab\"\n")

    allLines = inputFileHandle.readlines()
    
    #  with end ts. at least two lines of vowels needed. For only one vowel annotations this is not the case. But ts are not use by HEREst anyway 
#     for i in range( 1, len(allLines) - 1):
#         
#         tokens =  allLines[i].split("\t")
#         nextLineTokens = allLines[i+1].split("\t")
#         
#         monoPhone = replaceMonophonesNotDefinedInHMMList(tokens[1])
#         output=str(float(tokens[0])*10000000) +" " + str(float(nextLineTokens[0])*10000000) + " " +  monoPhone
#         outputFileHandle.write(output)
     
    #only one line    
    for i in range( len(allLines) ):
        
        tokens =  allLines[i].split("\t")
         
        monoPhone = replaceMonophonesNotDefinedInHMMList(tokens[-1])
        outputFileHandle.write(monoPhone)
        
        
    
    outputFileHandle.write  (".\n")
        
   
    
    inputFileHandle.close()

    return


def sonicVisTextPhnDir2mlf(inputDir, outputFileName):
    
    '''
    # convert all files in a dir from
    # .phoneAnno SV text format:
    #  0.000000000    sil
    # to .mlf format
    NOTE: all .phoneAnno should have a corresponding .wav file. uses .wav correpsonding to existing .phoneAnno files
    # @param: inputPath - dir with .phoneAnno Files
    # @param outputFileName - abs path and name to file  .mlf 
    
    '''
       
    
    outputFileHandle = open(outputFileName,  'w')
    outputFileHandle.write  ("#!MLF!#\n")

    
#     browse dir inputDir
    for roots, dirs, files in walklevel(inputDir, level=1):
        for inputFileName in files:
            ext = os.path.splitext(inputFileName)[1]
            # search for files with phn extension
            if ".phoneAnno" == ext: 
                    inputFileName = os.path.join(inputDir,inputFileName)
                    sonicVisText2mlf(inputFileName, outputFileHandle)
    



    
   
    
   
    outputFileHandle.close()
    
    # end each file  

    
    return


def replaceMonophonesNotDefinedInHMMList(monophone):
    '''
    replace all non-vowel monophones with model 'DUMMY'
    '''
    monophone  = monophone.rstrip()
    if  monophone in listVocals:
        return monophone + '\n'
    else: 
        return 'DUMMY\n'
    
    

if __name__ == '__main__':
    print 'in main'
#      sonicVisText2mlf(sys.argv[1], sys.argv[2]) 
#    sonicVisTextPhnDir2mlf(sys.argv[1], sys.argv[2])
    
#     sonicVisText2mlf("/Users/joro/Documents/Phd/UPF/Turkey-makam/kani_karaca-hicaz-durak.annotation.phn.txt","/Users/joro/Documents/Phd/UPF/Turkey-makam/kani_karaca-hicaz-durak.annotation.phn.txt.htk" )
#    
#     
#     mlf2sonicVisText("/Users/joro/Documents/Phd/UPF/Turkey-makam/kani_karaca-hicaz-durak.phn", "/Users/joro/Documents/Phd/UPF/Turkey-makam/kani_karaca-hicaz-durak.phn2")
#     
    
    