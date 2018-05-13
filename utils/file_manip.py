import os
from utils.time_manip import mmss_2_ss


def get_filenames_in_folder(folder_name):
    recordings = []
    for root, subFolders, files in os.walk(folder_name):
        for f in files:
            file_prefix, file_extension = os.path.splitext(f)
            if file_prefix != '.DS_Store' and file_prefix != '_DS_Store':
                recordings.append(file_prefix)
    return recordings


def write_line(filename, list_line):
    """
    Write a list of lines into filename, line by line
    :param filename:
    :param list_line:
    :return:
    """
    with open(filename, "w") as f:
        for line in list_line:
            if len(line[2].rstrip()):
                f.write("%.3f" % round(line[0],3)+'\t'+"%.3f" % round(line[1],3)+'\t'+line[2])
            else:
                f.write("%.3f" % round(line[0],3)+'\t'+"%.3f" % round(line[1],3)+'\t'+'sil')
            f.write('\n')


def write_lyrics_one_line(filename, line):
    """
    Write line into filename
    :param filename:
    :param line:
    :return:
    """
    with open(filename, "w") as f:
        if len(line.rstrip()):
            f.write(line)
        f.write('\n')


def read_kugou_annotation_chao_gang(filename):
    """
    Convert kugou annotation chao gang to list
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        content = f.readlines()
        list_annotation = []
        for line in content:
            line_split = line.rstrip().split('\t')
            list_annotation.append([mmss_2_ss(line_split[0]), mmss_2_ss(line_split[1]), line_split[2]])
    return list_annotation


def read_kugou_annotation_rong(filename):
    """
    Convert kugou annotation chao gang to list
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        content = f.readlines()
        list_annotation = []
        for line in content:
            line_split = line.rstrip().split('\t')
            list_annotation.append(line_split)
    return list_annotation


def read_phone_lexicon(filename):
    """
    Read phone lexicon into list
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        content = f.readlines()
        list_phone_lexicon = []
        for line in content:
            line_split = line.rstrip().split()
            list_phone_lexicon.append(line_split)
    return list_phone_lexicon


def write_phone_lexicon(filename, list_line):
    """
    Write a phone lexicon list into filename, line by line
    :param filename:
    :param list_line:
    :return:
    """
    with open(filename, "w") as f:
        for line in list_line:
            f.write(line[0]+' '+line[1])
            f.write('\n')


def read_mir1k_lyrics(filename):
    """
    Read mir1k lyrics into list
    :param filename:
    :return:
    """
    with open(filename, "r", encoding="Big5") as f:
        content = f.readlines()
        list_lyrics = []
        for line in content:
            line_split = line.rstrip().split('_')
            list_lyrics.append(''.join(line_split))
    return list_lyrics


def read_mir1k_pinyins(filename):
    """
    Read mir1k pinyin annotation
    :param filename:
    :return:
    """
    with open(filename, "r") as f:
        content = f.readlines()
        list_pinyins = []
        for line in content:
            line_split = line.rstrip().split()
            list_pinyins.append(line_split)
    return list_pinyins


def read_gracenote_groundtruth(filename, delimiter):
    """
    Convert gracenote annotation chao gang to list
    :param filename:
    :return:
    """
    with open(filename, "r", encoding="ISO-8859-1") as f:
        content = f.readlines()
        list_annotation = []
        for line in content:
            line_split = line.rstrip().split(delimiter)
            list_annotation.append(line_split)
    return list_annotation
