from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Largest basis of length 4 patterns which is non-regular insertion encodable -- #

# STATUS ================================================ >

# https://oeis.org/A045925

task = '1243_1324_1342_1423_1432_2143_2413_2431_3142_3412_4132_4231'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts)
# struct(patts, size = 4, verify_bound = 10, ask_verify_higher = True)
