"""
evaluation using alignmentEvaluation
"""
import csv
from eval.filepath import *
from alignmentEvaluation.align_eval.eval import main_eval_one_file

full_fn_csv_result = os.path.join(path_eval_results_CW, "kugou", "clean", "result.csv")
with open(full_fn_csv_result, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for r in clean_kugou:
        fn = os.path.splitext(r)[0]
        full_fn_wav = os.path.join(path_clean_kugou, r)

        full_fn_annotation_word_corrected = os.path.join(path_clean_kugou, fn + '_word_corrected.txt')

        full_fn_output = os.path.join(path_eval_results_CW, "kugou", "clean", fn+".txt")

        mean_error, percentage_correct, percentage_tolerance = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output, 0.3])

        csv_writer.writerow([fn, mean_error, percentage_correct, percentage_tolerance])

full_fn_csv_result = os.path.join(path_eval_results_CW, "kugou", "mix", "result.csv")
with open(full_fn_csv_result, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for r in mix_kugou:
        fn = os.path.splitext(r)[0]
        full_fn_wav = os.path.join(path_mix_kugou, r)

        full_fn_annotation_word_corrected = os.path.join(path_mix_kugou, fn + '_word_corrected.txt')

        full_fn_output = os.path.join(path_eval_results_CW, "kugou", "mix", fn+".txt")
        mean_error, percentage_correct, percentage_tolerance = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output, 0.3])
        csv_writer.writerow([fn, mean_error, percentage_correct, percentage_tolerance])


full_fn_csv_result = os.path.join(path_eval_results_CW, "hansen", "clean", "result.csv")
with open(full_fn_csv_result, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for r in clean_hansen:
        fn = os.path.splitext(r)[0]
        full_fn_wav = os.path.join(path_clean_hansen, r)

        full_fn_annotation_word_corrected = os.path.join(path_clean_hansen, fn + '_word_corrected.txt')

        full_fn_output_cw2 = os.path.join(path_eval_results_CW, "hansen", "clean", fn+"_cw2.txt")
        full_fn_output_cw3 = os.path.join(path_eval_results_CW, "hansen", "clean", fn+"_cw3.txt")

        mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw2, 0.3])
        mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw3, 0.3])
        csv_writer.writerow([fn, mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2, mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3])


full_fn_csv_result = os.path.join(path_eval_results_CW, "hansen", "mix", "result.csv")
with open(full_fn_csv_result, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for r in mix_hansen:
        fn = os.path.splitext(r)[0]
        full_fn_wav = os.path.join(path_mix_hansen, r)

        full_fn_annotation_word_corrected = os.path.join(path_mix_hansen, fn + '_word_corrected.txt')

        full_fn_output_cw2 = os.path.join(path_eval_results_CW, "hansen", "mix", fn+"_cw2.txt")
        full_fn_output_cw3 = os.path.join(path_eval_results_CW, "hansen", "mix", fn+"_cw3.txt")

        mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw2, 0.3])
        mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw3, 0.3])
        csv_writer.writerow([fn, mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2, mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3])


full_fn_csv_result = os.path.join(path_eval_results_CW, "gracenote", "clean", "result.csv")
with open(full_fn_csv_result, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for r in clean_gracenote:
        fn = os.path.splitext(r)[0]
        full_fn_wav = os.path.join(path_clean_gracenote, r)

        full_fn_annotation_word_corrected = os.path.join(path_clean_gracenote, fn + '_word_corrected.txt')

        full_fn_output_cw2 = os.path.join(path_eval_results_CW, "gracenote", "clean", fn+"_cw2.txt")
        full_fn_output_cw3 = os.path.join(path_eval_results_CW, "gracenote", "clean", fn+"_cw3.txt")

        mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw2, 0.3])
        mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw3, 0.3])
        csv_writer.writerow([fn, mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2, mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3])


full_fn_csv_result = os.path.join(path_eval_results_CW, "gracenote", "mix", "result.csv")
with open(full_fn_csv_result, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for r in mix_gracenote:
        fn = os.path.splitext(r)[0]
        full_fn_wav = os.path.join(path_mix_gracenote, r)

        full_fn_annotation_word_corrected = os.path.join(path_mix_gracenote, fn + '_word_corrected.txt')

        full_fn_output_cw2 = os.path.join(path_eval_results_CW, "gracenote", "mix", fn+"_cw2.txt")
        full_fn_output_cw3 = os.path.join(path_eval_results_CW, "gracenote", "mix", fn+"_cw3.txt")

        mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw2, 0.3])
        mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw3, 0.3])
        csv_writer.writerow([fn, mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2, mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3])

full_fn_csv_result = os.path.join(path_eval_results_CW, "mauch", "mix", "result.csv")
with open(full_fn_csv_result, 'w') as csvfile:
    csv_writer = csv.writer(csvfile)
    for r in mix_mauch:
        fn = os.path.splitext(r)[0]
        full_fn_wav = os.path.join(path_mix_mauch, r)

        full_fn_annotation_word_corrected = os.path.join(path_mix_mauch, fn + '_word_corrected.txt')

        full_fn_output_cw2 = os.path.join(path_eval_results_CW, "mauch", "mix", fn+"_cw2.txt")
        full_fn_output_cw3 = os.path.join(path_eval_results_CW, "mauch", "mix", fn+"_cw3.txt")

        mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw2, 0.3])
        mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3 = main_eval_one_file([None, full_fn_annotation_word_corrected, full_fn_output_cw3, 0.3])
        csv_writer.writerow([fn, mean_error_cw2, percentage_correct_cw2, percentage_tolerance_cw2, mean_error_cw3, percentage_correct_cw3, percentage_tolerance_cw3])
