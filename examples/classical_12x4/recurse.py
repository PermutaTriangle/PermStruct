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

task = '132_3412_4231'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts)
# struct(patts, size = 4, verify_bound = 10, ask_verify_higher = True)
