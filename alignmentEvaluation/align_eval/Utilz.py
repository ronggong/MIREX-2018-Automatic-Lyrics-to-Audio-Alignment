'''
Created on Jul 30, 2017

These scripts are copued from https://github.com/georgid/AlignmentDuration/blob/noteOnsets/src/utilsLyrics/Utilz.py
in order to reduce inter-porject dependency, please if you modify them, make sure they are updated in the original place
@author: joro
'''
import codecs
import numpy as np
import warnings
from mutagen.mp3 import MP3
# import mad

import logging
from mir_eval.io import load_delimited
from mir_eval import util
import os
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)


def get_duration_audio(filename):
    '''
    get duration in seconds of .wav file 
    '''
    import wave
    import contextlib
    with contextlib.closing(wave.open(filename, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration


def load_delimited_variants(filename, delimiter=r'\s+'):
    '''
    load from delimited file
    in order to be able to change the converters arguments of load_delimieted  to handle , instead of . in floating point vals 

    '''
    converter_comma = lambda val:float(val.replace(',', '.')) # replace ',' by '.'
    ends = None
    try:
        starts, ends, labels = load_delimited(filename, [converter_comma, converter_comma, str], delimiter) # start times and end times given
    except Exception as e: # only start times given
        try:
            starts, labels = load_delimited(filename, [converter_comma, str], delimiter)
        except Exception:
            labels, starts = load_delimited(filename, [str, converter_comma], delimiter)
            pass
    return starts, ends, labels


def load_labeled_intervals(filename, delimiter=r'\s+'):
    """
    overwrites https://github.com/craffel/mir_eval/blob/master/mir_eval/io.py#L208
    ends of intervals are not used later in evaluation, vut are needed for sanity check
    """
    # Use our universal function to load in the events
    
    starts, ends, labels = load_delimited_variants(filename, delimiter)
    
    if ends is None:  # add ends

        filename_base = remove_extension(filename)
        if "_word_corrected" in filename_base:
            filename_base = filename_base.replace("_word_corrected", "")
        filename_wav = filename_base + '.wav'
        filename_mp3 = filename_base + '.mp3'
        if not os.path.isfile(filename_wav) and not os.path.isfile(filename_mp3):
            raise IOError("not found file {}".format(filename_base))
            # dir = ''
            # while not os.path.isfile(filename_wav):
            #     dir = raw_input('cannot find {} \n Please enter folder where the wav file is:'.format(filename_wav))
            #     filename_wav = os.path.join(dir, os.path.basename(filename_wav))
        if os.path.isfile(filename_wav):
            duration = get_duration_audio(filename_wav)  # generate end timestamps from following start timestamps
        elif os.path.isfile(filename_mp3):
            # audio_mp3 = mad.MadFile(filename_mp3)
            audio_mp3 = MP3(filename_mp3)
            duration = audio_mp3.info.length
            # duration = audio_mp3.total_time()
            # print(duration)
            # raise ValueError
#         duration = starts[-1] + 1 # fake last word to be 1 sec long
        ends = starts[1:]
        ends = np.append(ends, duration)
    
    starts, ends, labels = remove_dot_tokens(starts, ends, labels)  # special words  '.' are discarded
     
    # Stack into an interval matrix
    intervals = np.array([starts, ends]).T
    # Validate them, but throw a warning in place of an error
    try:
        util.validate_intervals(intervals)
    except ValueError as error:
        warnings.warn(error.args[0])

    return intervals, labels


def remove_extension(URI):
    '''
    remove all extensions after dots completely
    e.g. path/base.ext1.ext2 -> path/base 
    '''
    URI = os.path.splitext(URI)[0]

    # while True:
    #     a1 = os.path.splitext(URI)[0]
    #
    #     if a1 == URI:
    #         break
    #     else:
    #         URI = a1
    return URI


def remove_dot_tokens(starts, ends,  labels):
    starts_no_dots = []
    ends_no_dots = []
    labels_no_dots = []
    for tuple_token in zip(starts, ends, labels):
        if tuple_token[-1] != '.' and tuple_token[-1] != -1:
            starts_no_dots.append(tuple_token[0])
            ends_no_dots.append(tuple_token[1])
            labels_no_dots.append(tuple_token[2])
    return np.array(starts_no_dots), np.array(ends_no_dots), labels_no_dots


def loadTextFile(pathToFile):
        '''
        helper method to load all lines from a text file 
        '''
        
        # U means cross-platform  end-line character
        inputFileHandle = codecs.open(pathToFile, 'rU', 'utf-8')
        
        allLines = inputFileHandle.readlines()

        
        inputFileHandle.close()
        
        return allLines
    
    
def writeListOfListToTextFile(listOfList,headerLine, pathToOutputFile, toFlip=False):    
    outputFileHandle = codecs.open(pathToOutputFile, 'w', 'utf-8')
    
    if not headerLine == None:
        outputFileHandle.write(headerLine)
    
    # flip (transpose) matrix
    if toFlip:
        a = np.rot90(listOfList)
        listOfList = np.flipud(a)
    
    for listLine in listOfList:
        
        output = ""
        for element in listLine:
            outputFileHandle.write("{:35}\t".format(element))
#             output = output + str(element) + "\t"
#         output = output.strip()
#         output = output + '\n'
#         outputFileHandle.write(output)
        outputFileHandle.write('\n')    
    
    outputFileHandle.close()
    
    logger.info ("successfully written file: \n {} \n".format( pathToOutputFile))


def writeCsv(fileURI, list_, withListOfRows=1, append=0):
    '''
    TODO: move to utilsLyrics
    '''
    from csv import writer
    if append:
        fout = open(fileURI, 'ab')
    else:
        fout = open(fileURI, 'wb')
    w = writer(fout)
    print('writing to csv file {}...'.format(fileURI) )
    for row in list_:
        if withListOfRows:
            w.writerow(row)
        else:
            tuple_note = [row.onsetTime, row.noteDuration]
            w.writerow(tuple_note)
    
    fout.close()


def getMeanAndStDevError(alignmentErrors):
    '''
    statistics for an array
    '''
        
    # convert to np array
    absalignmentErrors = [0] * len(alignmentErrors)
    for index, alError in enumerate(alignmentErrors):
        absalignmentErrors[index] = abs(alError)
    
    # calculate with numpy
    mean = np.round(np.mean(absalignmentErrors), decimals=2)
    median = np.round( np.median(absalignmentErrors), decimals=2)
    stDev = np.round( np.std(alignmentErrors), decimals=2)
    
    return mean, stDev, median