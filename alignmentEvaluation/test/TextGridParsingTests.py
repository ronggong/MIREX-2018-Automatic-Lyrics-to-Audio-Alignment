'''
Created on Sep 25, 2015

@author: joro
'''
import os
from TextGrid_Parsing import TextGrid2WordList

if __name__ == '__main__':
    
    #     TextGrid2Dict(sys.argv[1], sys.argv[2])
    dirURI = os.path.join(os.path.dirname(os.path.realpath(__file__))  ,    os.path.pardir)
    annotationURI = os.path.abspath(dirURI + '/example/01_Bakmiyor_0_zemin.TextGrid')
    whichTier = 2 # phrases
    annotationTokenListA = TextGrid2WordList(annotationURI, whichTier)
    print annotationTokenListA
#     toChronTest(annotationURI)