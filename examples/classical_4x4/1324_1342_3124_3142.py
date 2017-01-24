from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# STATUS ================================================ >

task = '1324_1342_3124_3142'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts, perm_bound = 12, size = 6)
