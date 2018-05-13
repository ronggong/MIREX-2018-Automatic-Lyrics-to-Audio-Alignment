import os
from data_manip.file_path import *
from utils.file_manip import read_phone_lexicon
from utils.file_manip import get_filenames_in_folder
from utils.file_manip import read_mir1k_pinyins
from utils.file_manip import read_kugou_annotation_rong


def test_pinyin_lexicon():
    list_pinyin_lexicon = read_phone_lexicon('../lm_pinyin/lexicon.txt')
    list_phone_lexicon = read_phone_lexicon('../lm_phone/lexicon.txt')
    phones = [l[0] for l in list_phone_lexicon]
    for l in list_pinyin_lexicon:
        for l_phone in l[1:]:
            if l_phone not in phones:
                print(l[0])


def pinyin_print_helper(fn, pinyins, annotation):
    for _, _, list_p in annotation:
        for p in list_p.split():
            if p not in pinyins:
                print(fn, p)


def test_annotation_in_lexicon():
    """
    test if annotation pinyin is contained in lexicon
    :return:
    """
    list_pinyin_lexicon = read_phone_lexicon('../lm_pinyin/lexicon.txt')
    pinyins = [l[0] for l in list_pinyin_lexicon]

    # mir1k
    path_mir1k_annotation = os.path.join(mir1k_root, 'annotation')
    filenames_mir1k = get_filenames_in_folder(folder_name=path_mir1k_annotation)
    filenames_mir1k = [fn for fn in filenames_mir1k if 'pinyin' in fn]

    for fn in filenames_mir1k:
        list_pinyins = read_mir1k_pinyins(filename=os.path.join(path_mir1k_annotation, fn+'.txt'))
        for p in list_pinyins[0]:
            if p not in pinyins:
                print(fn, p)

    # kugou
    path_kugou_annotation = os.path.join(mandarin_kugou_root, 'annotation')
    filenames_kugou_annotation = get_filenames_in_folder(folder_name=path_kugou_annotation)
    filenames_kugou_annotation = [fn for fn in filenames_kugou_annotation if 'pinyin' in fn]

    for fn in filenames_kugou_annotation:
        annotation = read_kugou_annotation_rong(filename=os.path.join(path_kugou_annotation, fn+'.txt'))
        pinyin_print_helper(fn, pinyins, annotation)


    # jingju
    train_dan_ss, train_dan_nacta, train_dan_primary, \
    train_laosheng_nacta, train_laosheng_primary, \
    dev_dan_ss, dev_dan_nacta, dev_dan_primary, \
    dev_laosheng_nacta, dev_laosheng_primary, test_dan_primary, \
    test_laosheng_primary = get_recording_names_jingju()

    extra_primary = get_recording_names_jingju_extra()

    train_nacta_2017, test_nacta_2017 = get_recording_names_jingju_nacta_2017()

    for path_fn in train_dan_ss + train_dan_nacta + train_laosheng_nacta + dev_dan_ss + dev_dan_nacta + dev_laosheng_nacta:
        fn = os.path.join(jingju_part1_root, 'annotation_txt', path_fn[0], path_fn[1]+'_phrase.txt')
        annotation = read_kugou_annotation_rong(filename=fn)
        pinyin_print_helper(fn, pinyins, annotation)

    for path_fn in train_nacta_2017 + test_nacta_2017:
        fn = os.path.join(jingju_part2_root, 'annotation_txt', path_fn[0], path_fn[1]+'_phrase.txt')
        annotation = read_kugou_annotation_rong(filename=fn)
        pinyin_print_helper(fn, pinyins, annotation)

    for path_fn in train_dan_primary + train_laosheng_primary + dev_dan_primary + dev_laosheng_primary + test_dan_primary + test_laosheng_primary + extra_primary:
        fn = os.path.join(jingju_part3_root, 'annotation_txt', path_fn[0], path_fn[1]+'_phrase.txt')
        annotation = read_kugou_annotation_rong(filename=fn)
        pinyin_print_helper(fn, pinyins, annotation)


if __name__ == '__main__':
    test_annotation_in_lexicon()