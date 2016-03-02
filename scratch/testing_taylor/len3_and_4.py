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
# 8 classes of the form Av(321,q) we can only do two, q = 1234 (trivial, but
# takes a very long time to find the set cover) and q = 2134. Hopefully we can
# do more with mutation rules

                    # -- Wilf-class 1 -- #

# The permutations ================================================ > SUCCESS!
# Finite and not very interesting
# perhaps we must use inp_dag = permstruct.dag.N_P(perm_bound)
# patts = [Permutation([3,2,1]), Permutation([1,2,3,4])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = False
#
# # Grids
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = 100

                    # -- Wilf-class 2 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([3,2,1]), Permutation([2,1,3,4])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = True
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 30

                    # -- Wilf-class 3 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,3,2,1])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = True
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 30

                    # -- Wilf-class 4 -- #

# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([1,3,2,4])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
# remove       = True
#
# # Grids
# max_rule_size = (4, 4)
# max_non_empty = 5
# max_rules     = None

                    # -- Wilf-class 5 -- #

# The permutations ================================================== > FAILURE! (Didn't wait for exact cover to finish)
patts = [Permutation([3,2,1]), Permutation([1,3,4,2])]

perm_bound    = 10
verify_bound  = 13
ignored       = 0

# The dag
max_len_patt = 2
upper_bound  = 1
# remove       = True
remove       = False

# Grids
max_rule_size = (8,8)
max_non_empty = 8
max_rules     = None

                    # -- Wilf-class 6 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([3,2,1]), Permutation([2,1,4,3])]
#
# perm_bound    = 9
# verify_bound  = 10
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = True
# # remove       = False
#
# # Grids
# max_rule_size = (7,7)
# max_non_empty = 7
# max_rules     = None

                    # -- Wilf-class 7 -- #5

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,3,1,2])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = True
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,2,3,1])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = True
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

                    # -- Wilf-class 8 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([3,2,1,4])]
#
# perm_bound    = 7
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

                    # -- Wilf-class 9 -- #

# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([2,3,4,1])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
# remove       = True
#
# # Grids
# max_rule_size = (4, 4)
# max_non_empty = 5
# max_rules     = None

# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([3,4,1,2])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 2
# remove       = True
#
# # Grids
# max_rule_size = (5, 5)
# max_non_empty = 5
# max_rules     = None

# The permutations ================================================== > FAILURE! (Didn't wait for exact cover to finish)
# patts = [Permutation([3,2,1]), Permutation([3,1,4,2])]
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
# remove       = True
#
# # Grids
# max_rule_size = (4, 4)
# max_non_empty = 4
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([1,2,3,4])]
#
# perm_bound    = 7
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
# remove       = True
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = None

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
