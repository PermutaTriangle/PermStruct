from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

# STATUS ================================================ >

# Skew-merge permutations

task = '2143_2413_3142_3412'
patts = [ Permutation([ int(c) for c in p ]) for p in task.split('_') ]

perm_bound    = 7
verify_bound  = 8
ignored       = 0

# The dag
max_len_patt = None
upper_bound  = None
remove       = False

# Grids
max_rule_size = (6, 6)
max_non_empty = 6
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
