from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

# -- Wilf-class 3 in http://wikipedia.org/wiki/Enumerations_of_specific_permutation_classes -- #

# STATUS ================================================ > SUCCESS!

patts = [Permutation([1,3,2]), Permutation([4,3,2,1])]

perm_bound    = 8
verify_bound  = 15
ignored       = 0

# The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = False
# Grids
# max_rule_size = (8, 8)
# max_non_empty = 8
# max_rules     = None

max_len_patt = None
upper_bound  = None
remove       = False

# Grids
max_rule_size = (7, 7)
max_non_empty = 7
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
