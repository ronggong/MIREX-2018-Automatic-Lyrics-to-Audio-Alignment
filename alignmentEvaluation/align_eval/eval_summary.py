'''
Created on Oct 16, 2017

@author: joro
'''
import sys
import os
import glob
from eval import main_eval_one_file
from Utilz import getMeanAndStDevError, writeCsv

def main_eval_all_files_summary(argv):
    if len(argv) != 5:
        sys.exit('usage: {} <algorithm name> <path dir with to reference word boundaries> <path to dir with detected word boundaries> <path_output>'.format(sys.argv[0]))
    
    algorithm_name = argv[1]
    refs_dir_URI = argv[2]
    detected_dir_URI = argv[3]
    a = os.path.join(detected_dir_URI, "*.lab")
    lab_files = glob.glob(a)
    output_URI = argv[4]
    
    errors = []
    percentages = []
       
    for lab_file in lab_files:
        base_name = os.path.basename(lab_file)
        
        ref_file = os.path.join(refs_dir_URI, base_name[:-4] + '.wordonset.tsv')
        error, percentage = main_eval_one_file(["dummy",  ref_file, lab_file])
        errors.append(error)
        percentages.append(percentage)
        
    meanE,  stdevE, medianE = getMeanAndStDevError(errors)
    meanP, stdevP, medianP = getMeanAndStDevError(percentages)
    
    if not os.path.exists(output_URI):
        results = [['Submission', 'Mean error'    , 'Median error', 'St. dev. error', 'Mean percentage'    , 'Median percentage', 'St. dev. percentage']]

        results.append( [algorithm_name,'{:.2f}'.format(meanE), '{:.2f}'.format(medianE) ,  '{:.2f}'.format(stdevE), '{:.2f}'.format(meanP), '{:.2f}'.format(medianP) ,  '{:.2f}'.format(stdevP) ] )
        writeCsv(output_URI, results)
    else:
        results = [[algorithm_name,'{:.2f}'.format(meanE), '{:.2f}'.format(medianE) ,  '{:.2f}'.format(stdevE), '{:.2f}'.format(meanP), '{:.2f}'.format(medianP) ,  '{:.2f}'.format(stdevP) ]]
        writeCsv(output_URI, results, append=1)
    
if __name__ == '__main__':
#     main_eval_one_file(sys.argv)
    main_eval_all_files_summary(sys.argv)