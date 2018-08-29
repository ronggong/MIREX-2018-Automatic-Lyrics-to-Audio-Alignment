import os

import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, "../data_manip"))
from file_path import *

root_path_mirex_ala = "/Volumes/rong_segate/mirex_submissions/mirex2018/submissions/ala"
path_eval_results_CW = "/Users/ronggong/PycharmProjects/MIREX-2018-Automatic-Lyrics-to-Audio-Alignment/eval/CW/results"

venv_py3 = "/Users/ronggong/venv/mirex2018_py36/bin/python3"

align_eval_py3 = os.path.join(dir_path, "..", "alignmentEvaluation", "align_eval", "eval.py")

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