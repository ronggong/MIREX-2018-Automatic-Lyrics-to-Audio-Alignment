"""
Created on Jun 30, 2015

@author: joro
"""
import sys
import os
import numpy as np
from align_eval.Utilz import getMeanAndStDevError
from align_eval.Utilz import load_labeled_intervals

project_dir = os.path.join(os.path.dirname(__file__), '..')

if project_dir not in sys.path:
    sys.path.append(project_dir)

from align_eval.ErrorEvaluator import _eval_alignment_error
from align_eval.ErrorEvaluator import _eval_percentage_tolerance
from align_eval.ErrorEvaluator import tierAliases
from align_eval.ErrorEvaluator import strip_non_lyrics_tokens
from align_eval.PraatVisualiser import ANNOTATION_EXT
from align_eval.PercentageCorrectEvaluator import _eval_percentage_correct


PATH_TEST_DATASET = os.path.join(project_dir, 'example/')


def load_ref_and_detections(dataset='hanson'):
    """
    convenience method. You can test with one example audio and annotation of each of the two datasets
    """
    # plt.figure()

    if dataset == 'generic':
        # generic data
        refs_url = os.path.join(PATH_TEST_DATASET, 'words.refs.lab')
        detected_url = os.path.join(PATH_TEST_DATASET, 'words.detected.lab')

        # refs_url = os.path.join(PATH_TEST_DATASET, 'words.onsets.refs.lab')
        # detected_url = os.path.join(PATH_TEST_DATASET, 'words.onsets.detected.lab')
    elif dataset == 'hansen':
        # for Hansen's dataset
        refs_url = os.path.join(PATH_TEST_DATASET, 'umbrella_words.refs.lab')
        detected_url = os.path.join(PATH_TEST_DATASET, 'umbrella_words.refs.lab')  # as if reference were detections
    elif dataset == 'mauch':
        # for Mauch's dataset
        refs_url = os.path.join(PATH_TEST_DATASET, 'Muse_GuidingLight.refs.lab')
        detected_url = os.path.join(PATH_TEST_DATASET, 'Muse_GuidingLight.refs.lab')  # as if reference were detections
    else:
        raise ValueError("{} is not exist.".format(dataset))

    ref_intervals, ref_labels = load_labeled_intervals(refs_url)
    detected_intervals, detected_labels = load_labeled_intervals(detected_url)

    return ref_intervals, detected_intervals, ref_labels


'''
percentage metric tests
'''


def eval_percentage_correct_lab_helper(ref_intervals,
                                       ref_labels,
                                       detected_intervals):
    initial_time_offset_refs = ref_intervals[0][0]
    finalts_refs = ref_intervals[-1][1]
    duration_correct, total_length = _eval_percentage_correct(ref_intervals,
                                                              detected_intervals,
                                                              finalts_refs,
                                                              initial_time_offset_refs,
                                                              ref_labels)
    return duration_correct, total_length


def test_eval_percentage_correct_lab_generic():
    """
    test the percentage of duration of correctly aligned tokens with loading the .lab files 
    """
    
    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='generic')
    duration_correct, total_length = eval_percentage_correct_lab_helper(ref_intervals=ref_intervals,
                                                                        ref_labels=ref_labels,
                                                                        detected_intervals=detected_intervals)
    assert np.allclose(0.612355429849504, duration_correct / total_length)


def test_eval_percentage_correct_lab_hansen():
    """
    test the percentage of duration of correctly aligned tokens with loading the .lab files
    """

    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='hansen')
    duration_correct, total_length = eval_percentage_correct_lab_helper(ref_intervals=ref_intervals,
                                                                        ref_labels=ref_labels,
                                                                        detected_intervals=detected_intervals)
    assert np.allclose(1.0, duration_correct / total_length)


def test_eval_percentage_correct_lab_mauch():
    """
    test the percentage of duration of correctly aligned tokens with loading the .lab files
    """

    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='mauch')
    duration_correct, total_length = eval_percentage_correct_lab_helper(ref_intervals=ref_intervals,
                                                                        ref_labels=ref_labels,
                                                                        detected_intervals=detected_intervals)
    assert np.allclose(1.0, duration_correct / total_length)


'''
eval error test
'''


def test_eval_error_lab_generic():
    """
    test mean average error/displacement (in seconds) of alignment with loading the .lab files 
    """
    
    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='generic')
    alignment_errors = _eval_alignment_error(ref_intervals, detected_intervals, ref_labels)
    mean_generic, std_dev_generic, median_generic = getMeanAndStDevError(alignment_errors)

    assert mean_generic == 0.98 and std_dev_generic == 0.96


def test_eval_error_lab_hansen():
    """
    test mean average error/displacement (in seconds) of alignment with loading the .lab files
    """

    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='hansen')
    alignment_errors = _eval_alignment_error(ref_intervals, detected_intervals,  ref_labels)
    mean_hansen, std_dev_hansen, median_hansen = getMeanAndStDevError(alignment_errors)
    assert mean_hansen == 0.0 and std_dev_hansen == 0.0


def test_eval_error_lab_mauch():
    """
    test mean average error/displacement (in seconds) of alignment with loading the .lab files
    """

    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='mauch')
    alignment_errors = _eval_alignment_error(ref_intervals, detected_intervals, ref_labels)
    mean_mauch, std_dev_mauch, median_mauch = getMeanAndStDevError(alignment_errors)
    assert mean_mauch == 0.0 and std_dev_mauch == 0.0


def test_eval_percentage_tolerance_lab_generic():
    """
    test the accuracy of tokens with a tolerance window tau loading the .lab files
    """

    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='generic')
    accuracy = _eval_percentage_tolerance(ref_intervals=ref_intervals,
                                          detected_intervals=detected_intervals,
                                          reference_labels=ref_labels,
                                          tolerance=0.3)
    assert accuracy == 0.0


def test_eval_percentage_tolerance_lab_hansen():
    """
    test the accuracy of tokens with a tolerance window tau loading the .lab files 
    """
    
    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='hansen')
    accuracy = _eval_percentage_tolerance(ref_intervals=ref_intervals,
                                          detected_intervals=detected_intervals,
                                          reference_labels=ref_labels,
                                          tolerance=0.3)
    
    assert accuracy == 1.0


def test_eval_percentage_tolerance_lab_mauch():
    """
    test the accuracy of tokens with a tolerance window tau loading the .lab files
    """

    ref_intervals, detected_intervals, ref_labels = load_ref_and_detections(dataset='mauch')
    accuracy = _eval_percentage_tolerance(ref_intervals=ref_intervals,
                                          detected_intervals=detected_intervals,
                                          reference_labels=ref_labels,
                                          tolerance=0.3)

    assert accuracy == 1.0


def eval_percentage_correct_textgrid_test():
       
    audio_name = '05_Semahat_Ozdenses_-_Bir_Ihtimal_Daha_Var_0_zemin_from_69_5205_to_84_2'
    annotation_url = os.path.join(PATH_TEST_DATASET,  audio_name + ANNOTATION_EXT)
   
    detected_token_list = [[0.61, 0.94, u'Bir'],
                           [1.02, 3.41, u'ihtimal'],
                           [3.42, 4.11, u'daha'],
                           [4.12, 5.4, u'var'],
                           [8.03, 8.42, u'o'],
                           [8.46, 8.83, u'da'],
                           [8.86, 10.65, u'\xf6lmek'],
                           [10.66, 11.04, u'mi'],
                           [11.05, 14.39, u'dersin']]
     
    start_index = 0
    end_index = -1

    annotation_token_list, detected_token_list, final_ts_anno, initial_time_offset = \
        strip_non_lyrics_tokens(annotation_url,
                                detected_token_list,
                                tierAliases.phrases,
                                start_index,
                                end_index)
    
    duration_correct, total_length = _eval_percentage_correct(annotation_token_list,
                                                              detected_token_list,
                                                              final_ts_anno,
                                                              initial_time_offset)
    print(duration_correct / total_length)


def eval_error_textgrid_test():
    
    audio_name = '05_Semahat_Ozdenses_-_Bir_Ihtimal_Daha_Var_0_zemin_from_69_5205_to_84_2'
    annotation_url = os.path.join(PATH_TEST_DATASET,  audio_name + ANNOTATION_EXT)
    
    start_index = 0
    end_index = -1
    
    detected_token_list = [[0.61, 0.94, u'Bir'],
                           [1.02, 3.41, u'ihtimal'],
                           [3.42, 4.11, u'daha'],
                           [4.12, 5.4, u'var'],
                           [8.03, 8.42, u'o'],
                           [8.46, 8.83, u'da'],
                           [8.86, 10.65, u'\xf6lmek'],
                           [10.66, 11.04, u'mi'],
                           [11.05, 14.39, u'dersin']]
    
    annotation_token_list, detected_token_list, dummy, dummy = \
        strip_non_lyrics_tokens(annotation_url,
                                detected_token_list,
                                tierAliases.phrases,
                                start_index,
                                end_index)
     
    alignment_errors = _eval_alignment_error(annotation_token_list,
                                             detected_token_list,
                                             tierAliases.phrases)
    mean, std_dev, median = getMeanAndStDevError(alignment_errors)
    print("mean : ", mean, "st dev: ", std_dev)


if __name__ == '__main__':
#     test_eval_percentage_correct_lab_hansen()
#     test_eval_percentage_correct_lab_mauch()
    test_eval_error_lab_mauch()

#     test_eval_percentage_tolerance_lab_generic()
#     test_eval_percentage_tolerance_lab_hansen()
    test_eval_percentage_tolerance_lab_mauch()
