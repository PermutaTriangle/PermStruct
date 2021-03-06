from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

# -- Example from Kuszmaul paper -- #

# STATUS ================================================ >

patts = [Permutation([2,1,4,3]), Permutation([3,1,4,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([1,3,2,4])]

# The dag
max_len_patt = None
upper_bound  = None
remove       = False

ignored       = 0

# ------------------------------------------------------------------------------ FAILURE: no cover
perm_bound    = 5
verify_bound  = 10

# Grids
max_rule_size = (4, 4)
max_non_empty = 4
max_rules     = None
# ------------------------------------------------------------------------------
perm_bound    = 6
verify_bound  = 10

# Grids
max_len_patt = 3
upper_bound  = 1
max_rule_size = (6, 6)
max_non_empty = 6
max_rules     = None
# ------------------------------------------------------------------------------ Takes too long, move to server. Failure on server. No cover found
perm_bound    = 6
verify_bound  = 10

# Grids
max_len_patt = None
upper_bound  = None
max_rule_size = (5, 5)
max_non_empty = 5
max_rules     = None
# ------------------------------------------------------------------------------ No cover
perm_bound    = 7
verify_bound  = 10

# Grids
max_len_patt = 3
upper_bound  = 1
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
