from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- One of the two 6x4 bases that seem to take a really long time -- #

# STATUS ================================================ >

task = '1324_1342_1423_1432_2431_4132'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts, perm_bound=10, subpatts_type='EVERY')
# struct(patts, size = 4, verify_bound = 10, ask_verify_higher = True)
