import os
import string
from data_manip.file_path import *
from utils.file_manip import read_gracenote_groundtruth

filename_gracenote_long_groundtruth = os.path.join(gracenote_root, 'groundtruth.txt')
list_groundtruth = read_gracenote_groundtruth(filename=filename_gracenote_long_groundtruth,
                                              delimiter='\t')

num_syllable = 0
list_syllable = []
for ii in range(len(list_groundtruth)-1):
    if list_groundtruth[ii+1][0] != list_groundtruth[ii][0] and ii != 0:
        if '2NE1' not in list_groundtruth[ii][0]:
            filename_write = os.path.join(gracenote_root,
                                          'annotation',
                                          list_groundtruth[ii][0]+'_'+list_groundtruth[ii][1]+'.txt')
            with open(filename_write, 'w') as f:
                f.writelines(list_syllable)
        list_syllable = []
    list_syllable.append('\t'.join([list_groundtruth[ii+1][3], list_groundtruth[ii+1][2]])+'\n')
    syllable = list_groundtruth[ii+1][2].rstrip()
    if len(syllable) > 0 and syllable not in string.punctuation and '2NE1' not in list_groundtruth[ii][0]:
        num_syllable += 1

for ii in range(1, 8):
    filename_gracenote_single = os.path.join(gracenote_root, 'song'+str(ii), 'lyrics_timestamps.csv')
    list_groundtruth = read_gracenote_groundtruth(filename=filename_gracenote_single,
                                                  delimiter=',')
    filename_write = os.path.join(gracenote_root,
                                  'annotation',
                                  'song'+str(ii)+'.txt')
    with open(filename_write, 'w') as f:
        for line in list_groundtruth[1:]:
            syllable = line[0].rstrip().lower()
            if syllable not in string.punctuation:
                syllable = ''.join([s for s in syllable if s not in string.punctuation])
                f.write('\t'.join([line[5], syllable])+'\n')

            if len(syllable) > 0 and syllable not in string.punctuation:
                num_syllable += 1

print('num syllable', num_syllable)
