from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

# STATUS ================================================ >
patts = map(Permutation, [[1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2], [2,1,4,3], [2,3,1,4], [3,1,2,4]]) # 1243_1324_1342_1423_1432_2143_2314_3124
patts = map(Permutation, [[1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,3,2], [2,1,4,3], [2,3,1,4], [2,4,1,3]]) # 1243_1324_1342_1432_2143_2314_2413
patts = [Permutation([1,2,4,3]), Permutation([1,3,2,4]), Permutation([1,3,4,2]), Permutation([1,4,3,2]), Permutation([2,1,4,3]), Permutation([2,3,1,4]), Permutation([2,4,1,3])]
# patts = map(Permutation, [[1,2,4,3], [1,3,2,4]])
# patts = map(Permutation, [[4,2,3,1]])

task = '1324_1342_1423_1432_2143_2314_2341_2413_2431_3124_3142_3214_3241_4123_4132_4213'
task = '1342_1432_2413_3124_3142_3214_3241_3412_4132'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

perm_bound    = 7
verify_bound  = 8
ignored       = 0

# The dag
max_len_patt = 4
upper_bound  = 24
remove       = False

# Grids
max_rule_size = (5, 5)
max_non_empty = 5
max_rules     = None

# ------------------------------------------------------------------------------

settings = StructSettings(
        perm_bound=perm_bound,
        verify_bound=verify_bound,
        max_rule_size=max_rule_size,
        max_non_empty=max_non_empty,
        max_rules=max_rules,
        verbosity=StructLogger.INFO)
# settings.set_input(StructInput.from_avoidance(settings, patts))
settings.set_input(AvoiderInput(settings, patts))
settings.set_dag(taylor_dag(settings,
                    max_len_patt=max_len_patt,
                    remove=remove,
                    upper_bound=upper_bound))

exhaustive(settings)
