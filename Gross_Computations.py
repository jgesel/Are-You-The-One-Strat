# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 14:24:13 2019

@author: david
"""
import numpy as np
from itertools import permutations 
import random

all_perms = list(permutations(range(1, 8))) 
true_perm = np.array([2,1, 3, 4, 5, 6, 7])
#test_ind = np.int(np.random.choice(len(all_perms), 1))


dt = np.dtype('int,float')
all_perms = np.asarray(all_perms)
test_perm = all_perms[np.int(np.random.choice(len(all_perms), 1))]

#Narrow Down permutations which are admissible given collected data



def Logic_Puzzle(true_permutation, submitted_permutation, remaining_permutations):
    work_perms = ["nan" for x in range(len(remaining_permutations))]
    num_correct = sum((submitted_permutation - true_permutation) == 0)
    # which_perms_dont_work = [0 for x in range(len(all_perms))]
    i = 0
    for perm in remaining_permutations:
        diff_arr = submitted_permutation - perm
        match = sum(diff_arr == 0)
        if(match == num_correct):
            #which_perms_dont_work[i] = perm
            work_perms[i] = perm
            i = i+1
       # else:
          #  which_perms_dont_work[i] = 1
      #  i = i+1
    #return(which_perms_dont_work)
    cleanedList = [x for x in work_perms if str(x) != 'nan']
    return(cleanedList)

#Recursively play multiple rounds (time2game)
def Games_We_Play(true_permutation, submitted_permutation, remaining_permutations, rounds):
    if(rounds == 1):
        #submitted_perm = remaining_permutations[np.int(np.random.choice(len(remaining_permutations), 1))]
        return(Logic_Puzzle(true_permutation, submitted_permutation, remaining_permutations))
    else:
        remaining_perms = Logic_Puzzle(true_permutation, submitted_permutation, remaining_permutations)
        submitted_perm = remaining_perms[np.int(np.random.choice(len(remaining_perms), 1))]
        return(Games_We_Play(true_permutation, submitted_perm, remaining_perms, rounds - 1))
    
test = Games_We_Play(true_perm, test_perm, all_perms, 5)
#remaining_perms = Logic_Puzzle(true_perm, test_perm, all_perms)
#test_perm2 = remaining_perms[np.int(np.random.choice(len(remaining_perms), 1))]
#correct = Logic_Puzzle(true_perm, test_perm2, remaining_perms)
        
    
#perms_left = all_perms[correct]