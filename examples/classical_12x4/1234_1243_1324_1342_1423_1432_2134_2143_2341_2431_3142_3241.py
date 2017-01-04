from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# -- Example from Kuszmaul paper -- #

# STATUS ================================================ >

# https://oeis.org/A045925

task = '1234_1243_1324_1342_1423_1432_2134_2143_2341_2431_3142_3241'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts, size=2)
