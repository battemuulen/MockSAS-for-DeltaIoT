# MockSAS-for-DeltaIoT

This python package allows the creation of profiles of SAS systems for the evaluation of multi-armed bandit policies.
# Explanation
Profiles are specified in the profile folder, a profile of SWIM (a SAS Exemplar) is included. Execution starts from the run.py script through which MAB policies to evaluate are specified. By default the run.py takes two arguments, the number of seeds to use and the name of the csv file of the results. For example:
    
python run.py 10 results.csv

# This extension provides profiles for DeltaIoT SAS
This work was done as a part of Bachelor Thesis project at Vrije Universiteit Amsterdam.

The origininal MockSAS version can be found by this link - https://github.com/EGAlberts/MockSAS
