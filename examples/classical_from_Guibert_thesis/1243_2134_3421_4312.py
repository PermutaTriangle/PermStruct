from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Guibert paper -- #

# STATUS ================================================ >

# This is polynomial.

patts = [Permutation([1,2,4,3]), Permutation([2,1,3,4]), Permutation([3,4,2,1]), Permutation([4,3,1,2])]

struct(patts, subpatts_len = 2, size = 7, perm_bound = 12, verify_bound = 15, ask_verify_higher = True)
