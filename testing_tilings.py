from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

from permstruct.permutation_sets import SimpleGeneratingRule, GeneratingRule, StaticPermutationSet

import sys



# STATUS ================================================ >

G = GeneratingRule([
    [P,P,P,P],
    [P,P,P,P],
    [P,P,P,P],
    [P,P,P,P],
])

for perm in G.generate_of_length(16, P): print(perm)

# task = '1234_1243_1324_1342_1432_2134_2143_2413_3124_4123_4132_4213'
# patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]
#
# struct(patts, perm_bound=7)
