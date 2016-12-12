from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Guibert paper -- #

# STATUS ================================================ >

# Answer: 2 * |Av(123,1432,3214)| for all n >= 6

patts = [Permutation([1,4,3,2]), Permutation([2,3,4,1]), Permutation([3,2,1,4]), Permutation([4,1,2,3])]

struct(patts, size = 8, perm_bound = 10, verify_bound = 14, ask_verify_higher = True)
