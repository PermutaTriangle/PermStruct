from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Kuszmaul paper -- #

# STATUS ================================================ >

task = '1234_1243_2134_2431_4213'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]
# patts = [Permutation([5,2,3,4,1]), Permutation([5,3,2,4,1]), Permutation([5,2,4,3,1]), Permutation([3,5,1,4,2]), Permutation([4,2,5,1,3]), Permutation([3,5,1,6,2,4])]

struct(patts, size=6, perm_bound = 8, subpatts_len=4, subpatts_num=3)
# struct(patts, size = 4, verify_bound = 10, ask_verify_higher = True)
