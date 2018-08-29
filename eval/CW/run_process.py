"""
needs to be executed in terminal
"""
import os
from subprocess import call, Popen

import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, ".."))
from filepath import *


path_CW1 = os.path.join(root_path_mirex_ala, "CW1/CW1/go.py")
path_CW2 = os.path.join(root_path_mirex_ala, "CW2/CW2/go.py")
path_CW3 = os.path.join(root_path_mirex_ala, "CW3/CW3/go.py")

for r in clean_kugou:
    fn = os.path.splitext(r)[0]
    full_fn_wav = os.path.join(path_clean_kugou, r)

    full_fn_annotation_word_corrected = os.path.join(path_clean_kugou, fn + '_word_corrected.txt')

    full_fn_annotation_line = os.path.join(path_clean_kugou, fn + '_line_pinyin_break.txt')

    full_fn_output = os.path.join(path_eval_results_CW, "kugou", "clean", fn+".txt")

    call([venv_py3, path_CW1, full_fn_wav, full_fn_annotation_line, full_fn_output])

for r in mix_kugou:
    fn = os.path.splitext(r)[0]
    full_fn_wav = os.path.join(path_mix_kugou, r)

    full_fn_annotation_word_corrected = os.path.join(path_mix_kugou, fn + '_word_corrected.txt')

    full_fn_annotation_line = os.path.join(path_mix_kugou, fn + '_line_pinyin_break.txt')

    full_fn_output = os.path.join(path_eval_results_CW, "kugou", "mix", fn+".txt")

    call([venv_py3, path_CW1, full_fn_wav, full_fn_annotation_line, full_fn_output])


for r in clean_hansen:
    fn = os.path.splitext(r)[0]
    full_fn_wav = os.path.join(path_clean_hansen, r)

    full_fn_annotation_word_corrected = os.path.join(path_clean_hansen, fn + '_word_corrected.txt')

    full_fn_annotation_line = os.path.join(path_clean_hansen, fn + '_line_pinyin_break.txt')

    full_fn_output_cw2 = os.path.join(path_eval_results_CW, "hansen", "clean", fn+"_cw2.txt")
    full_fn_output_cw3 = os.path.join(path_eval_results_CW, "hansen", "clean", fn+"_cw3.txt")

    call([venv_py3, path_CW2, full_fn_wav, full_fn_annotation_line, full_fn_output_cw2])
    call([venv_py3, path_CW3, full_fn_wav, full_fn_annotation_line, full_fn_output_cw3])


for r in mix_hansen:
    fn = os.path.splitext(r)[0]
    full_fn_wav = os.path.join(path_mix_hansen, r)

    full_fn_annotation_word_corrected = os.path.join(path_mix_hansen, fn + '_word_corrected.txt')

    full_fn_annotation_line = os.path.join(path_mix_hansen, fn + '_line_pinyin_break.txt')

    full_fn_output_cw2 = os.path.join(path_eval_results_CW, "hansen", "mix", fn+"_cw2.txt")
    full_fn_output_cw3 = os.path.join(path_eval_results_CW, "hansen", "mix", fn+"_cw3.txt")

    call([venv_py3, path_CW2, full_fn_wav, full_fn_annotation_line, full_fn_output_cw2])
    call([venv_py3, path_CW3, full_fn_wav, full_fn_annotation_line, full_fn_output_cw3])


for r in clean_gracenote:
    fn = os.path.splitext(r)[0]
    full_fn_wav = os.path.join(path_clean_gracenote, r)

    full_fn_annotation_word_corrected = os.path.join(path_clean_gracenote, fn + '_word_corrected.txt')

    full_fn_annotation_line = os.path.join(path_clean_gracenote, fn + '_line_pinyin_break.txt')

    full_fn_output_cw2 = os.path.join(path_eval_results_CW, "gracenote", "clean", fn+"_cw2.txt")
    full_fn_output_cw3 = os.path.join(path_eval_results_CW, "gracenote", "clean", fn+"_cw3.txt")

    call([venv_py3, path_CW2, full_fn_wav, full_fn_annotation_line, full_fn_output_cw2])
    call([venv_py3, path_CW3, full_fn_wav, full_fn_annotation_line, full_fn_output_cw3])


for r in mix_gracenote:
    fn = os.path.splitext(r)[0]
    full_fn_wav = os.path.join(path_mix_gracenote, r)

    full_fn_annotation_word_corrected = os.path.join(path_mix_gracenote, fn + '_word_corrected.txt')

    full_fn_annotation_line = os.path.join(path_mix_gracenote, fn + '_line_pinyin_break.txt')

    full_fn_output_cw2 = os.path.join(path_eval_results_CW, "gracenote", "mix", fn+"_cw2.txt")
    full_fn_output_cw3 = os.path.join(path_eval_results_CW, "gracenote", "mix", fn+"_cw3.txt")

    call([venv_py3, path_CW2, full_fn_wav, full_fn_annotation_line, full_fn_output_cw2])
    call([venv_py3, path_CW3, full_fn_wav, full_fn_annotation_line, full_fn_output_cw3])


for r in mix_mauch:
    fn = os.path.splitext(r)[0]
    full_fn_wav = os.path.join(path_mix_mauch, r)

    full_fn_annotation_word_corrected = os.path.join(path_mix_mauch, fn + '_word_corrected.txt')

    full_fn_annotation_line = os.path.join(path_mix_mauch, fn + '_line_pinyin_break.txt')

    full_fn_output_cw2 = os.path.join(path_eval_results_CW, "mauch", "mix", fn+"_cw2.txt")
    full_fn_output_cw3 = os.path.join(path_eval_results_CW, "mauch", "mix", fn+"_cw3.txt")

    call([venv_py3, path_CW2, full_fn_wav, full_fn_annotation_line, full_fn_output_cw2])
    call([venv_py3, path_CW3, full_fn_wav, full_fn_annotation_line, full_fn_output_cw3])
