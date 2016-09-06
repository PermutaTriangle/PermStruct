from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

#---------------------------------------------------------------------------#
#               1 pattern of length 3         1 pattern of length 4         #
#---------------------------------------------------------------------------#

# We are able to do every Av(132,q) where q has length 4. Out of the remaining
# 8 classes of the form Av(321,q) we can only do two, q = 1234 (trivial) and
# q = 2134. Hopefully we can do more with mutation rules

                    # -- Wilf-class 1 -- #

# The permutations ================================================ > SUCCESS!
# Finite and not very interesting
# patts = [Permutation([3,2,1]), Permutation([1,2,3,4])]
#
# perm_bound    = 7
# verify_bound  = 12
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = False
#
# # Grids
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = None

                    # -- Wilf-class 2 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([3,2,1]), Permutation([2,1,3,4])]
#
# perm_bound    = 8
# verify_bound  = 12
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = False # True (3, 3) 4 works
#
# # Grids
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = None

                    # -- Wilf-class 3 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,3,2,1])]
#
# perm_bound    = 9
# verify_bound  = 15
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = False # True (3,3) 4, max_len_patt = 3, upper_bound  = 2

# # Grids
# max_rule_size = (8, 8)
# max_non_empty = 8
# max_rules     = None

                    # -- Wilf-class 4 -- # Success with remove=True, need to try 999 with remove=False

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([3,2,1]), Permutation([1,3,2,4])]
#
# perm_bound    = 12
# # perm_bound=12 gives a cover that verifies in 15
# # perm_bound=11 does not work, not everything generated in 12
# # perm_bound=10 does not work, not everything generated in 11
# verify_bound  = 15
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = True
#
# # Grids
# max_rule_size = (9, 9)
# max_non_empty = 9
# max_rules     = None

                    # -- Wilf-class 5 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([3,2,1]), Permutation([1,3,4,2])]
#
# perm_bound    = 9
# verify_bound  = 13
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = False
#
# # Grids
# max_rule_size = (5,5)
# max_non_empty = 6
# max_rules     = None

                    # -- Wilf-class 6 -- # Success with remove=True, need to try 888 with remove=False

# The permutations ================================================== > SUCCESS!
patts = [Permutation([3,2,1]), Permutation([2,1,4,3])]

perm_bound    = 9
verify_bound  = 12
ignored       = 0

# The dag
max_len_patt = 2
upper_bound  = 1
remove       = False # True (5, 5) 5 works

# Grids
max_rule_size = (8,8)
max_non_empty = 8
max_rules     = None

                    # -- Wilf-class 7 -- # Success for 2/2

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,3,1,2])]
#
# perm_bound    = 9
# verify_bound  = 12
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False # True (4,4) 4
#
# # Grids
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,2,3,1])]
#
# perm_bound    = 8
# verify_bound  = 11
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False # True (3,3) 3
#
# # Grids
# max_rule_size = (5, 5)
# max_non_empty = 5
# max_rules     = None

                    # -- Wilf-class 8 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([3,2,1,4])]
#
# perm_bound    = 8
# verify_bound  = 11
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

                    # -- Wilf-class 9 -- # Success for 7/9

# The permutations ================================================== > FAILURE!
# We know mutation rules for this set, so perhaps there are no covers
# patts = [Permutation([3,2,1]), Permutation([2,3,4,1])]
#
# No covers
# The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True

# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = None

# No covers
# The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = True

# max_rule_size = (8, 8)
# max_non_empty = 8
# max_rules     = None

# # No covers
# perm_bound    = 10
# verify_bound  = 12
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True
#
# # Grids
# max_rule_size = (7, 7)
# max_non_empty = 7
# max_rules     = None

# perm_bound    = 10
# verify_bound  = 12
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True
#
# # Grids
# max_rule_size = (7, 7)
# max_non_empty = 7
# max_rules     = None

# The permutations ================================================== > FAILURE!
# No cover with
# perm_bound    = 8
# verify_bound  = 9
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True
# # Grids
# max_rule_size = (7, 7)
# max_non_empty = 7
# max_rules     = None

# # No covers
# erm_bound    = 9
# verify_bound  = 11
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = True
#
# # Grids
# max_rule_size = (8, 8)
# max_non_empty = 8
# max_rules     = None

# patts = [Permutation([3,2,1]), Permutation([3,4,1,2])]
#
# perm_bound    = 9
# verify_bound  = 11
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = True
#
# # Grids
# max_rule_size = (8, 8)
# max_non_empty = 8
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([3,2,1]), Permutation([3,1,4,2])]
#
# perm_bound    = 6
# verify_bound  = 12
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = False #True with (4, 4) 4 works
#
# # Grids
# max_rule_size = (5, 5)
# max_non_empty = 5
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([1,2,3,4])]
#
# perm_bound    = 8
# verify_bound  = 11
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,2,1,3])]
#
# perm_bound    = 7
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,1,2,3])]
#
# perm_bound    = 7
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([3,1,2,4])]
#
# perm_bound    = 7
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([2,1,3,4])]
#
# perm_bound    = 7
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = False
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([3,4,1,2])]
#
# perm_bound    = 7
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = False # With remove=True we can use (3,3) 3
#
# # Grids
# max_rule_size = (5, 5)
# max_non_empty = 5
# max_rules     = None

# ===================================================

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
