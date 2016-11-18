from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Kuszmaul paper -- #

# STATUS ================================================ >

patts = [Permutation([1,3,2]), Permutation([2,3,1,4]), Permutation([2,3,4,1]), Permutation([4,3,1,2])]

struct(patts, verify_bound = 10, ask_verify_higher = False)
