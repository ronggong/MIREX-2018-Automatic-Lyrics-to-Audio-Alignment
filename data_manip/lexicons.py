from utils.file_manip import read_phone_lexicon
from utils.file_manip import write_phone_lexicon
from string import digits


def convert_phone_intonation_lexicon():
    list_phone_lexicon = read_phone_lexicon('../lm_phone/lexicon_intonation.txt')
    filename_phone_lexicon_no_digits_no_rep = '../lm_phone/lexicon.txt'

    # remove digits
    remove_digits = str.maketrans('', '', digits)
    list_phone_lexicon_no_digits =[l[0].translate(remove_digits) for l in list_phone_lexicon]

    # remove repeats
    list_phone_lexicon_no_digits_no_rep = []
    for p in list_phone_lexicon_no_digits:
        if p not in list_phone_lexicon_no_digits_no_rep:
            list_phone_lexicon_no_digits_no_rep.append(p)

    # write into a new lexicon file
    list_phone_lexicon_no_digits_no_rep_to_write = [[l, l] for l in list_phone_lexicon_no_digits_no_rep]
    write_phone_lexicon(filename_phone_lexicon_no_digits_no_rep, list_phone_lexicon_no_digits_no_rep_to_write)
