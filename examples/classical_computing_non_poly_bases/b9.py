from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

# -- Examples from Vatter paper -- #

# STATUS ================================================ >

patts = map(Permutation, [[1, 2, 3], [3, 1, 4, 2], [3, 4, 1, 2]])

# ------------------------------------------------------------------------------
perm_bound    = 5
verify_bound  = 10
ignored       = 0

# The dag
max_len_patt = 3
upper_bound  = None
remove       = False

# Grids
max_rule_size = (5, 5)
max_non_empty = 5
max_rules     = None
# ------------------------------------------------------------------------------

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
