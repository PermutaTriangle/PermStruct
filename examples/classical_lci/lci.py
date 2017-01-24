from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Kuszmaul paper -- #

# STATUS ================================================ >

patts = [Permutation([5,2,3,4,1]), Permutation([5,3,2,4,1]), Permutation([5,2,4,3,1]), Permutation([3,5,1,4,2]), Permutation([4,2,5,1,3]), Permutation([3,5,1,6,2,4])]

struct(patts, size=4, subpatts_len=2)
# struct(patts, size = 4, verify_bound = 10, ask_verify_higher = True)
