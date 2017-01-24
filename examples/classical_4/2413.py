from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

# STATUS ================================================ >
patts = [Permutation([2,4,1,3])]

# Running... should run on the cluster
struct(patts)
