from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Kuszmaul paper -- #

# STATUS ================================================ >

patts = [Permutation([2,4,3,1]), Permutation([2,1,4,3]), Permutation([3,1,4,2]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([1,3,2,4]), Permutation([1,4,2,3]), Permutation([1,2,4,3])]

struct(patts, size = 4, verify_bound = 10, ask_verify_higher = False)
