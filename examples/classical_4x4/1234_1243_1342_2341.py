from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# STATUS ================================================ >

# Successful with 2x2 rules

task = '1234_1243_1342_2341'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts, size=2)
