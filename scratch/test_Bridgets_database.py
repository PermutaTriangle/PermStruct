from __future__ import print_function
from permuta import *
# from itertools import combinations
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

#------------------------------------------------#

# Stuff from Bridget's database
# http://math.depaul.edu/bridget/patterns.html

                        #-- P0004 --#
# The permutations ================================================== > FAILURE!
# patts = [Permutation([2,1,4,3])]
#
# perm_bound    = 7
# verify_bound  = 8
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = None


                        #-- P0007 --#
# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,4,2,1]), Permutation([4,2,3,1]), Permutation([4,3,1,2])]
#
# perm_bound    = 7
# verify_bound  = 8
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True
#
# # Grids
# max_rule_size = (5, 5)
# max_non_empty = 5
# max_rules     = None

                        #-- P0008 --#
# The permutations ================================================== > FAILURE!
patts = [Permutation([3,4,2,1]), Permutation([4,2,3,1]), Permutation([4,3,1,2]), Permutation([4,3,2,1])]

perm_bound    = 6
verify_bound  = 9
ignored       = 0

# The dag
max_len_patt = None
upper_bound  = None
remove       = False

# Grids
max_rule_size = (5, 5)
max_non_empty = 5
max_rules     = None

                        #-- P0009 --#
# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([4,6,7,1,8,2,3,5]), Permutation([4,6,7,8,1,2,3,5]), Permutation([5,6,7,1,8,2,3,4]), Permutation([5,6,7,8,1,2,3,4])]
#
# perm_bound    = 9
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = None
# remove       = True
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

                        #-- P0016 --#
# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([2,3,4,1]), Permutation([3,4,1,2]), Permutation([4,1,2,3])]
#
# perm_bound    = 7
# verify_bound  = 9
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = False
#
# # Grids
# max_rule_size = (6, 6) <------------------ Try larger rules
# max_non_empty = 6
# max_rules     = None

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

                        #-- P0028 --#
# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([2,1,3]), Permutation([4,3,2,1])]

# perm_bound    = 7
# verify_bound  = 8
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = False
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

                        #-- P0029 --#
# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2,4]), Permutation([1,3,4,2]), Permutation([2,4,1,3]), Permutation([2,4,3,1]),
#          Permutation([3,1,2,4]), Permutation([3,1,4,2]), Permutation([4,2,1,3]),
#          Permutation([4,2,3,1])]
#
# perm_bound    = 6
# verify_bound  = 12
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = False
#
# # Grids
# max_rule_size = (5, 5)
# max_non_empty = 5
# max_rules     = None

                        #-- P0030 --#
# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2,4]), Permutation([1,3,4,2]), Permutation([2,1,4,3]), Permutation([2,4,1,3]),
#          Permutation([2,4,3,1]), Permutation([3,1,2,4]), Permutation([3,4,1,2]), Permutation([4,2,1,3]),
#          Permutation([4,2,3,1])]
#
# perm_bound    = 7
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = False
#
# # Grids
# max_rule_size = (5, 5)
# max_non_empty = 5
# max_rules     = None

# ===================================================

settings = StructSettings(
        perm_bound=perm_bound,
        verify_bound=verify_bound,
        ask_verify_higher=True,
        max_rule_size=max_rule_size,
        max_non_empty=max_non_empty,
        max_rules=max_rules,
        verbosity=StructLogger.INFO)
settings.set_input(AvoiderInput(settings, patts))
settings.set_dag(taylor_dag(settings,
                    max_len_patt=max_len_patt,
                    remove=remove,
                    upper_bound=upper_bound))

exhaustive(settings)
