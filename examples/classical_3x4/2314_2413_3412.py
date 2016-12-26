from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Kuszmaul paper -- #

# STATUS ================================================ >

task = '2314_2413_3412'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts)
# struct(patts, size = 4, verify_bound = 10, ask_verify_higher = True)
