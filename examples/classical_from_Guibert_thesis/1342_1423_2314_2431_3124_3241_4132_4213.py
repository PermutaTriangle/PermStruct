from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Guibert paper -- #

# STATUS ================================================ >

# This can be done by insertion encoding.

patts = [ Permutation([1,3,4,2]), Permutation([1,4,2,3]),
Permutation([2,3,1,4]), Permutation([2,4,3,1]), Permutation([3,1,2,4]),
Permutation([3,2,4,1]), Permutation([4,1,3,2]), Permutation([4,2,1,3]) ]

struct(patts, size = 6, perm_bound = 8, verify_bound = 12, ask_verify_higher = True)
