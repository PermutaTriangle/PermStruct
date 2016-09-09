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

                        #-- P0023 --#
# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]),
# Permutation([3,4,1,2]),
# Permutation([2,3,4,5,1]),
# Permutation([2,3,5,1,4]),
# Permutation([2,4,1,5,3]),
# Permutation([2,5,1,3,4]),
# Permutation([3,1,4,2,5]),
# Permutation([3,1,5,2,4]),
# Permutation([4,1,2,5,3]),
# Permutation([5,1,2,3,4]),
# Permutation([2,3,4,1,6,5]),
# Permutation([2,3,1,5,6,4]),
# Permutation([2,3,1,6,4,5]),
# Permutation([2,4,1,3,6,5]),
# Permutation([2,1,4,5,6,3]),
# Permutation([2,1,4,6,3,5]),
# Permutation([2,1,5,3,6,4]),
# Permutation([2,1,6,3,4,5]),
# Permutation([3,1,4,2,6,5]),
# Permutation([3,1,2,5,6,4]),
# Permutation([3,1,2,6,4,5]),
# Permutation([4,1,2,3,6,5]),
# Permutation([2,3,1,5,4,7,6]),
# Permutation([2,1,4,3,6,7,5]),
# Permutation([2,1,4,3,7,5,6]),
# Permutation([2,1,4,5,3,7,6]),
# Permutation([2,1,5,3,4,7,6]),
# Permutation([3,1,2,5,4,7,6]),
# Permutation([2,1,4,3,6,5,8,7])]
#
# perm_bound    = 8
# verify_bound  = 9
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = None
# remove       = False
#
# # Grids
# max_rule_size = (4, 4)
# max_non_empty = 4
# max_rules     = None

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
