import os
import fool
import pinyin
from opencc import OpenCC
from data_manip.file_path import *
from utils.file_manip import get_filenames_in_folder
from utils.file_manip import write_line
from utils.file_manip import write_lyrics_one_line
from utils.file_manip import read_kugou_annotation_chao_gang
from utils.file_manip import read_mir1k_lyrics
from utils.textgrid_parser import textgrid_2_word_list


def segmentation_conversion_helper(fn, list_line, sub_folder):
    list_line_char = [[line[0], line[1], ' '.join(fool.cut(line[2])[0])] for line in list_line if
                      len(line[2].replace(" ", "")) > 0]
    list_line_pinyin = [[line[0], line[1], pinyin.get(line[2], format='strip', delimiter=' ')] for line in list_line if
                        len(line[2].replace(" ", "")) > 0]
    write_line(filename=os.path.join(mandarin_kugou_root, sub_folder, fn + '_phrase_char.txt'),
               list_line=list_line_char)
    write_line(filename=os.path.join(mandarin_kugou_root, sub_folder, fn + '_phrase_pinyin.txt'),
               list_line=list_line_pinyin)


def segment_lyrics_convert_pinyin_kugou_clean():
    folder_train_kugou = os.path.join(mandarin_kugou_root, 'train_10_clean')
    filenames_train_kugou = list(set(get_filenames_in_folder(folder_train_kugou)))
    filenames_train_kugou.remove('songlist')

    # script to segment lyrics and convert to pinyin, don't run it again!
    for fn in filenames_train_kugou:
        fn_textgrid = os.path.join(folder_train_kugou, fn+'.textgrid')
        list_line, _ = textgrid_2_word_list(textgrid_file=fn_textgrid, whichTier='line')
        segmentation_conversion_helper(fn, list_line, 'annotation')


def segment_lyrics_convert_pinyin_kugou_separation():
    folder_train_kugou = os.path.join(mandarin_kugou_root, 'train_10_separation')
    filenames_train_kugou = list(set(get_filenames_in_folder(folder_train_kugou)))
    for fn in filenames_train_kugou:
        print(fn)
        fn_txt = os.path.join(folder_train_kugou, fn+'.txt')
        list_line = read_kugou_annotation_chao_gang(fn_txt)
        segmentation_conversion_helper(fn, list_line, 'annotation_separation')


def segment_lyric_convert_pinyin_mir1k():
    openCC = OpenCC('tw2s')
    folder_lyrics_mir1k = os.path.join(mir1k_root, 'Lyrics')
    filenames_lyrics_mir1k = list(set(get_filenames_in_folder(folder_lyrics_mir1k)))
    for fn in filenames_lyrics_mir1k:
        fn_txt = os.path.join(folder_lyrics_mir1k, fn+'.txt')
        try:
            list_line = read_mir1k_lyrics(fn_txt)
            line_simplified = openCC.convert(list_line[0])
            line_pinyin = pinyin.get(line_simplified, format='strip', delimiter=' ')
            line_char = ' '.join(fool.cut(line_simplified)[0])
            write_lyrics_one_line(filename=os.path.join(mir1k_root, 'annotation', fn + '_phrase_char.txt'),
                                  line=line_char)
            write_lyrics_one_line(filename=os.path.join(mir1k_root, 'annotation', fn + '_phrase_pinyin.txt'),
                                  line=line_pinyin)
        except UnicodeDecodeError:
            print(fn)

#
# if __name__ == '__main__':
#     segment_lyric_convert_pinyin_mir1k()