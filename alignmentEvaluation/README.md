
Copyright 2018 Music Technology Group - Universitat Pompeu Fabra

AlignmentEvaluation
==============================

A tool for computing common alignment metrics of tokens (a token could be at different granularity level: a phoneme, word or phrase - a group of words ). Done to evaluate results of a system for lyrics-to-audio alignment on different token levels. 
Three common metrics are implemented: 
1) mean average absolute error/deviation
2) percentage of correct segments from total audio duration
3) percentage of correct tokens with tolerance window (0.3 seconds)

For definition of the metrics see Chapter 2.2.1 from [this thesis](http://compmusic.upf.edu/phd-thesis-georgi)

The algorithm considers only begin timestamps of each token. It is token-identities-agnostic, e.g. it does not try to match token-IDs between detected result and annotation, but proceeds successively one-by-one.  
Extendable to the evaluation for any token-based alignment (e.g. if a token is a phrase, note, section )

Supported detected file formats :  
- mlf format of [htk](htk.eng.cam.ac.uk/) 
- lab format  of tuples <begin_timestamp, end_timestamp, tokenID>. If end timestamps are not known, tuples are <begin_timestamp, tokenID>, but the percentage of correct segments might degrade for a dataset that has annotated end timestamps. 

Supported annotation file formats: 
- TextGrid of [Praat](www.praat.org/) 
- lab format (see above). When exported from many tools among which e.g. [Audacity](http://www.audacityteam.org/home/). End time stamps are important only for the metric percentage of correct segments. They are ingored for the other two metrics.

Enjoy!
 

BUILD INSTRUCTIONS:
------------------------------------------
- install [mir_eval](https://github.com/craffel/mir_eval)
- git clone https://github.com/georgid/AlignmentEvaluation
- cd <path_to_installed AlignmentEvaluation>
- python setup.py install


USAGE: 
---------------------------------------- 

### For .lab file 

python [eval.py](https://github.com/georgid/AlignmentEvaluation/blob/master/align_eval/eval.py) 
<path to file with reference word boundaries> <path to file with detected word boundaries>
This reports (1) the mean average error, (2) the percentage of correct segments and (3) percentage of correct tokens with tolerance window (0.3s).


See also the individual metrics as test cases: 
- mean average absolute error/deviation : [test.EvalMetricsTest.evalError_lab_test()](https://github.com/georgid/AlignmentEvaluation/blob/126c3fa5fa1994acdcfbe3ea1344acfe71ae2b8e/test/EvalMetricsTest.py#L117)

- percentage of correct segments : [test.EvalMetricsTest.evalPercentageCorrect_lab_test()](https://github.com/georgid/AlignmentEvaluation/blob/126c3fa5fa1994acdcfbe3ea1344acfe71ae2b8e/test/EvalMetricsTest.py#L76)

- percentage of correct tokens with tolerance window (0.3 seconds) : [test.EvalMetricsTest.evalAccuracy_lab_test()](https://github.com/georgid/AlignmentEvaluation/blob/126c3fa5fa1994acdcfbe3ea1344acfe71ae2b8e/test/EvalMetricsTest.py#L151)



### For .TextGrid file 

test.EvalMetricsTest.evalAccuracy_TextGird_test()

test.EvalMetricsTest.eval_error_textGrid_test()

There is also a module to convert automatically the decoded result to Praat's TextGrid format.
This enables the  visualization of the decoding result together with the groundTruth in Praat:
see PraatVisualiser.openTextGridInPraatopenTextGridInPraat() : opens the text Grid in Praat
NOTE: # deprecated due to error on opening word-level files... use instead tab2TextGrid 

As well make sure to change the path to your installed Praat program:
PraatVisualiser.PATH_TO_PRAAT

To change extensions edit variables in WordLevelEvaluator 
ANNOTATION_EXT = '.TextGrid'
DETECTED_EXT = '.dtwDurationAligned'
when parsing TextGrid: tier_names are expected as defined in TextGrid_Parsing


EXAMPLE: 
---------------------------------------- 
if decoded result is:
 
startTs endTs phonemeOrWord

0.0		1.11	sil

1.11	2.41	usagi

2.41	2.90	usagi

2.90	3.38	sp

3.38	4.15	nani

and annotation  is:

1.12 	usagi usagi 

3.56 	nani

...then the two detected phrases are considered to evaluate:  

1.11 2.90 usagi usagi 

and 

3.38 4.15	nani


LICENSE:
-------------------
AlignmentEvaluation is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation (FSF), either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see http://www.gnu.org/licenses/

CITATION: 
----------------------
please cite 
Dzhambazov, G., - Knowledge-based Probabilistic Modeling for Tracking Lyrics in Music Audio Signals, PhD Thesis


