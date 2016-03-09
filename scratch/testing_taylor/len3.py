from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

# Avoidance of classical patterns of length 3

#------------------------------------------------#
#               1 pattern                        #
#------------------------------------------------#

# -- Wilf-class 1 -- #

# # The permutations ================================================== > FAILURE!
# We are expecting to fail this until we introduce the mutation rules
# patts = [Permutation([1,2,3])]
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
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# # The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2])]
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
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

#------------------------------------------------#
#               2 patterns                       #
#------------------------------------------------#

# -- Wilf-class 1 -- #

# # The permutations ================================================== > SUCCESS!
# # This class is a bit weird since it is finite. But we can still do it!
patts = [Permutation([1,2,3]), Permutation([3,2,1])]

perm_bound    = 7
verify_bound  = 10
ignored       = 0

# The dag
max_len_patt = None
upper_bound  = None
remove       = False

# Grids
max_rule_size = (3, 3)
max_non_empty = 4 # <--------------------------------- Note!
max_rules     = None

# -- Wilf-class 2 -- #

# # The permutations ================================================== > SUCCESS!
# This can also be done with (3,3) rules, 3 non-empty and remove=True
# patts = [Permutation([1,2,3]), Permutation([2,3,1])]
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
# max_rule_size = (4, 4)
# max_non_empty = 4
# max_rules     = None

# -- Wilf-class 3 -- #

# # The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,2,3]), Permutation([1,3,2])]
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
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# # The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([3,1,2])]
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
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([2,3,1]), Permutation([3,1,2])]
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
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

#------------------------------------------------#
#               3 patterns                       #
#------------------------------------------------#

# We use Simion and Schmidt to eliminate symmetric cases

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,2,3]), Permutation([1,3,2]), Permutation([2,1,3])]
# patts = [Permutation([1,2,3]), Permutation([1,3,2]), Permutation([2,3,1])]
# patts = [Permutation([1,3,2]), Permutation([2,1,3]), Permutation([2,3,1])]
# patts = [Permutation([1,2,3]), Permutation([1,3,2]), Permutation([3,1,2])]
# patts = [Permutation([1,2,3]), Permutation([2,3,1]), Permutation([3,1,2])]
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
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

#------------------------------------------------#
#               4 patterns                       #
#------------------------------------------------#

# We use Simion and Schmidt to eliminate symmetric cases

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([2,3,1]), Permutation([1,3,2]), Permutation([3,1,2]), Permutation([2,1,3])]
# patts = [Permutation([2,3,1]), Permutation([3,2,1]), Permutation([1,3,2]), Permutation([3,1,2])]
# patts = [Permutation([3,1,2]), Permutation([3,2,1]), Permutation([1,3,2]), Permutation([2,1,3])]
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
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None
#
# ===================================================

settings = StructSettings(
        perm_bound=perm_bound,
        verify_bound=verify_bound,
        max_rule_size=max_rule_size,
        max_non_empty=max_non_empty,
        max_rules=max_rules,
        verbosity=StructLogger.INFO)
settings.set_input(StructInput.from_avoidance(settings, patts))
settings.set_dag(taylor_dag(settings,
                    max_len_patt=max_len_patt,
                    remove=remove,
                    upper_bound=upper_bound))

exhaustive(settings)
