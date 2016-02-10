from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag

import sys

# Avoidance of classical patterns of length 3

#---------------------------------------------------------------------------#
#               1 pattern of length 3         1 pattern of length 4         #
#---------------------------------------------------------------------------#

# We are able to do every Av(132,q) where q has length 4 EXECpT ONE!!!!!. Out of the remaining
# 8 classes of the form Av(321,q) we can only do two, q = 1234 (trivial, but
# takes a very long time to find the set cover) and q = 2134. Hopefully we can
# do more with mutation rules

                    # -- Wilf-class 1 -- #

# # The permutations ================================================== > ?!
# # Finite and not very interesting
# # perhaps we must use inp_dag = permstruct.dag.N_P(perm_bound)
# patts = [Permutation([3,2,1]), Permutation([1,2,3,4])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
#
# # Grids
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = 30

                    # -- Wilf-class 2 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([3,2,1]), Permutation([2,1,3,4])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 2
# upper_bound  = 1
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 30

                    # -- Wilf-class 3 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,3,2,1])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# max_rule_size = (4, 4)
# max_non_empty = 4
# max_rules     = None

                    # -- Wilf-class 5 -- #

# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([1,3,4,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# max_rules     = None

                    # -- Wilf-class 6 -- #

# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([2,1,4,3])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# max_rules     = None

                    # -- Wilf-class 7 -- #

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([4,3,1,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# max_rules     = None

# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([3,4,1,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# max_rules     = None

# The permutations ================================================== > FAILURE!
# patts = [Permutation([3,2,1]), Permutation([3,1,4,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# max_rules     = None

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([1,2,3,4])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
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

# The permutations ================================================== > FAILURE!
patts = [Permutation([1,3,2]), Permutation([3,4,1,2])]
perm_prop = lambda p: all( p.avoids(q) for q in patts )

perm_bound    = 7
ignored       = 0

# The dag
max_len_patt = 2
upper_bound  = 2
remove       = True

# Grids
max_rule_size = (3, 3)
max_non_empty = 3
max_rules     = None

# Creating the dag
# inp_dag       = permstruct.dag.N_P_X1_mon(perm_prop, perm_bound)
inp_dag = permstruct.dag.taylor_dag(patts, max_len_patt=max_len_patt, perm_bound=perm_bound, remove=remove, upper_bound=upper_bound)
for el in inp_dag.elements:
    print(el.description if el is not None else 'None')

# Finding the rules and running exact cover
sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, max_rule_size, max_non_empty, max_rules, ignore_first=ignored)

for sol in sol_iter:

    print('====================================')
    print("")
    for rule in sol:
        print(rule)
        print("")
