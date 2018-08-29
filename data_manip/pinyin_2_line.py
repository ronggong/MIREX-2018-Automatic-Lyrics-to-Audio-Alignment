import os
import string
from utils.file_manip import read_kugou_annotation_rong
from utils.file_manip import read_word_annotation
from utils.file_manip import write_line_level_annotation
from utils.file_manip import write_line_num_col
from data_manip.file_path import *


def concatenate_words_2_list(list_annotation, col_word):
    list_words = []
    for row in list_annotation:
        list_words.append(row[col_word])

    return list_words


def remove_special_char(list_annotation, col_word):
    list_annotation_removed = []
    for row in list_annotation:
        if row[col_word] == '<pau>' or row[col_word].lower() == 'breath*' or row[col_word] in string.punctuation:
            continue
        if row[col_word][0] in string.punctuation:
            row[col_word] = row[col_word][1:]
        if row[col_word][-1] in string.punctuation:
            row[col_word] = row[col_word][:-1]
        row[col_word] = row[col_word].replace('_', '\'')
        list_annotation_removed.append(row)
    return list_annotation_removed


if __name__ == "__main__":
    clean_kugou, mix_kugou = get_kugou_filename()
    clean_hansen, mix_hansen = get_hansen_filename()
    clean_gracenote, mix_gracenote = get_gracenote_filename()
    mix_mauch = get_mauch_filename()

    path_clean_kugou = os.path.join(mandarin_kugou_root, 'clean')
    path_mix_kugou = os.path.join(mandarin_kugou_root, 'mix')

    path_clean_hansen = os.path.join(hansen_root, 'clean')
    path_mix_hansen = os.path.join(hansen_root, 'mix')

    path_clean_gracenote = os.path.join(gracenote_root, 'clean')
    path_mix_gracenote = os.path.join(gracenote_root, 'mix')

    path_mix_mauch = os.path.join(mauch_root, 'EP')

    """
    # fix biggie
    fn_biggie = os.path.join(path_mix_gracenote, 'biggie.txt')
    list_annotation = read_kugou_annotation_rong(fn_biggie)
    with open(os.path.join(path_mix_gracenote, 'biggie_word.txt'), 'w') as f:
        for row in list_annotation:
            f.write(row[-1] + '\t' + row[-2] + '\n')
    """

    for r in clean_kugou:
        fn = os.path.splitext(r)[0]
        full_fn_annotation = os.path.join(path_clean_kugou, fn+'_syllable_pinyin.txt')
        list_annotation = read_kugou_annotation_rong(full_fn_annotation)
        list_annotation_removed = remove_special_char(list_annotation, col_word=2)
        list_words = concatenate_words_2_list(list_annotation_removed, col_word=2)

        full_fn_annotation_word_corrected = os.path.join(path_clean_kugou, fn+'_word_corrected.txt')
        write_line_num_col(filename=full_fn_annotation_word_corrected, list_line=list_annotation_removed, num_col=3)

        full_fn_annotation_line = os.path.join(path_clean_kugou, fn+'_line_pinyin.txt')
        write_line_level_annotation(filename=full_fn_annotation_line, list_words=list_words)

    for r in mix_kugou:
        fn = os.path.splitext(r)[0]
        full_fn_annotation = os.path.join(path_mix_kugou, fn+'_syllable_pinyin.txt')
        list_annotation = read_kugou_annotation_rong(full_fn_annotation)
        list_annotation_removed = remove_special_char(list_annotation, col_word=2)
        list_words = concatenate_words_2_list(list_annotation_removed, col_word=2)

        full_fn_annotation_word_corrected = os.path.join(path_mix_kugou, fn+'_word_corrected.txt')
        write_line_num_col(filename=full_fn_annotation_word_corrected, list_line=list_annotation_removed, num_col=3)

        full_fn_annotation_line = os.path.join(path_mix_kugou, fn + '_line_pinyin.txt')
        write_line_level_annotation(filename=full_fn_annotation_line, list_words=list_words)

    for r in clean_hansen:
        fn = os.path.splitext(r)[0]
        full_fn_annotation = os.path.join(path_clean_hansen, fn+'_word_aligned.txt')
        list_annotation = read_word_annotation(full_fn_annotation)
        list_annotation_removed = remove_special_char(list_annotation, col_word=2)
        list_words = concatenate_words_2_list(list_annotation_removed, col_word=2)

        full_fn_annotation_word_corrected = os.path.join(path_clean_hansen, fn+'_word_corrected.txt')
        write_line_num_col(filename=full_fn_annotation_word_corrected, list_line=list_annotation_removed, num_col=3)

        full_fn_annotation_line = os.path.join(path_clean_hansen, fn + '_line_pinyin.txt')
        write_line_level_annotation(filename=full_fn_annotation_line, list_words=list_words)

    for r in mix_hansen:
        fn = os.path.splitext(r)[0]
        full_fn_annotation = os.path.join(path_mix_hansen, fn+'.wordonset.tsv')
        list_annotation = read_kugou_annotation_rong(full_fn_annotation)
        list_annotation_removed = remove_special_char(list_annotation, col_word=2)
        list_words = concatenate_words_2_list(list_annotation_removed, col_word=2)

        full_fn_annotation_word_corrected = os.path.join(path_mix_hansen, fn+'_word_corrected.txt')
        write_line_num_col(filename=full_fn_annotation_word_corrected, list_line=list_annotation_removed, num_col=3)

        full_fn_annotation_line = os.path.join(path_mix_hansen, fn + '_line_pinyin.txt')
        write_line_level_annotation(filename=full_fn_annotation_line, list_words=list_words)

    for r in clean_gracenote:
        fn = os.path.splitext(r)[0]
        full_fn_annotation = os.path.join(path_clean_gracenote, fn+'.txt')
        list_annotation = read_kugou_annotation_rong(full_fn_annotation)
        list_annotation_removed = remove_special_char(list_annotation, col_word=1)
        list_words = concatenate_words_2_list(list_annotation_removed, col_word=1)

        full_fn_annotation_word_corrected = os.path.join(path_clean_gracenote, fn+'_word_corrected.txt')
        write_line_num_col(filename=full_fn_annotation_word_corrected, list_line=list_annotation_removed, num_col=2)

        full_fn_annotation_line = os.path.join(path_clean_gracenote, fn + '_line_pinyin.txt')
        write_line_level_annotation(filename=full_fn_annotation_line, list_words=list_words)

    for r in mix_gracenote:
        fn = os.path.splitext(r)[0]
        full_fn_annotation = os.path.join(path_mix_gracenote, fn+'.txt')
        list_annotation = read_kugou_annotation_rong(full_fn_annotation)
        list_annotation_removed = remove_special_char(list_annotation, col_word=1)
        list_words = concatenate_words_2_list(list_annotation_removed, col_word=1)

        full_fn_annotation_word_corrected = os.path.join(path_mix_gracenote, fn+'_word_corrected.txt')
        write_line_num_col(filename=full_fn_annotation_word_corrected, list_line=list_annotation_removed, num_col=2)

        full_fn_annotation_line = os.path.join(path_mix_gracenote, fn + '_line_pinyin.txt')
        write_line_level_annotation(filename=full_fn_annotation_line, list_words=list_words)

    for r in mix_mauch:
        fn = os.path.splitext(r)[0]
        full_fn_annotation = os.path.join(path_mix_mauch, fn+'.wordonset.tsv')
        list_annotation = read_kugou_annotation_rong(full_fn_annotation)
        list_annotation_removed = remove_special_char(list_annotation, col_word=1)
        list_words = concatenate_words_2_list(list_annotation_removed, col_word=1)

        full_fn_annotation_word_corrected = os.path.join(path_mix_mauch, fn+'_word_corrected.txt')
        write_line_num_col(filename=full_fn_annotation_word_corrected, list_line=list_annotation_removed, num_col=2)

        full_fn_annotation_line = os.path.join(path_mix_mauch, fn + '_line_pinyin.txt')
        write_line_level_annotation(filename=full_fn_annotation_line, list_words=list_words)
