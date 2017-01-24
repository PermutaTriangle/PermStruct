from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# STATUS ================================================ >

task = '1243_2143_3412_3421'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

struct(patts)
