from __future__ import print_function
from permuta import *
from itertools import combinations
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True



# patts =     [  Permutation([1,2,4,3]), Permutation([1,3,4,2]),
# Permutation([1,4,2,3]), Permutation([1,4,3,2]), Permutation([2,1,4,3]),
# Permutation([2,4,1,3]), Permutation([2,4,3,1]), Permutation([3,1,4,2]),
# Permutation([3,2,1,4]), Permutation([3,2,4,1]), Permutation([4,1,3,2]) ]

# patts = [ Permutation([1,2,4,3]), Permutation([1,3,4,2]),
# Permutation([1,4,2,3]), Permutation([1,4,3,2]), Permutation([2,1,3,4]),
# Permutation([2,1,4,3]), Permutation([2,3,1,4]), Permutation([2,3,4,1]),
# Permutation([2,4,1,3]), Permutation([2,4,3,1]), Permutation([4,1,3,2]) ]

# patts = [ Permutation([1,2,4,3]), Permutation([1,3,4,2]),
# Permutation([1,4,2,3]), Permutation([2,1,3,4]), Permutation([2,1,4,3]),
# Permutation([2,3,1,4]), Permutation([2,3,4,1]), Permutation([2,4,1,3]),
# Permutation([3,1,2,4]), Permutation([3,1,4,2]), Permutation([4,1,2,3]) ]

#==============================================================================#

###############################
##   Olivier Guibert Thesis  ##
###############################

# patts = [ Permutation([1,2,3,4]), Permutation([1,2,4,3]),
# Permutation([1,4,2,3]), Permutation([4,1,2,3]) ]
# # Point over av(123)

patts = [ Permutation([2,3,1,4]), Permutation([2,4,1,3]),
Permutation([3,1,4,2]), Permutation([3,2,4,1]) ]
# remove=True with 6x6 found couver that did not verify: death by overlap.
# remove=True with 4x4 found couver that did not verify: death by perm prop.

print(patts)

perm_bound    = 8
verify_bound  = 10
ignored       = 0

# The dag
max_len_patt = None
upper_bound  = None
remove       = True

# Grids
max_rule_size = (4, 4)
max_non_empty = 4
max_rules     = None

#==============================================================================#


# Avoidance of two length 4 patterns

# patts = [Permutation([4,3,2,1]), Permutation([1,2,3,4])]
# Obviously works since finite sequence.


# patts = [ Permutation([4,3,1,2]), Permutation([1,2,3,4]) ]
# # This is polynomial, no success with these settings.
# # (took about an hour and a half).
# perm_bound    = 8
# verify_bound  = 10
# ignored       = 0
# # The dag
# max_len_patt = 2
# upper_bound  = None
# remove       = True
# # Grids
# max_rule_size = (7, 7)
# max_non_empty = 7
# max_rules     = None


# patts = [ Permutation([4,3,2,1]), Permutation([1,3,2,4]) ]
# # This is polynomial.

# patts = [ Permutation([3,4,1,2]), Permutation([2,1,4,3]) ]
# # This is algebraic (nonrational)
# # Failed with these settings. Found a cover that did not verify at length 8.
# # Took about 20 minutes.
# perm_bound    = 7
# verify_bound  = 10
# ignored       = 0
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True
# # max_len_patt = None
# # upper_bound  = None
# # remove       = True
# # Grids
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = None

# patts = [ Permutation([4,3,2,1]), Permutation([4,1,2,3]) ]
# # This is rational with formula a(n) = (4^n + 2)/3.
# # Nothing found.

# patts = [ Permutation([1,3,2,4]), Permutation([2,1,3,4]) ]
# # The smooth permutations. It is algebraic (nonrational).
#
# print(patts)
#
# perm_bound    = 8
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = None
# remove       = True
#
# # max_len_patt = None
# # upper_bound  = None
# # remove       = True
#
# # Grids
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = None

# # Stack-Sortable Permutations
# patts = [Permutation([2,3,1])]
# print(patts)
#
# perm_bound    = 6
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
