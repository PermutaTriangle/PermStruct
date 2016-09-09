from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

# Stuff from Bridget's database
# http://math.depaul.edu/bridget/patterns.html

                        #-- P0009 --#
# The permutations ================================================== > FAILURE!
patts = [Permutation([3,2,1]), Permutation([4,6,7,1,8,2,3,5]), Permutation([4,6,7,8,1,2,3,5]), Permutation([5,6,7,1,8,2,3,4]), Permutation([5,6,7,8,1,2,3,4])]

perm_bound    = 9
verify_bound  = 10
ignored       = 0

# The dag
max_len_patt = 3
upper_bound  = None
remove       = True

# Grids
max_rule_size = (3, 3)
max_non_empty = 3
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
