from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag

import sys

# Avoidance of classical patterns of length 3

#------------------------------------------------#
#               1 pattern                        #
#------------------------------------------------#

# -- Wilf-class 1 -- #

# # The permutations ================================================== > FAILURE!
# We are expecting to fail this until we introduce the mutation rules
# patts = [Permutation([1,2,3])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100

# # The permutations ================================================== > SUCCESS!
# # TODO: The dag that is created is too big, it contains incr and decr. We
# # should iteratively enlarge it: Special case the elements/add elements
# patts = [Permutation([1,3,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100

#------------------------------------------------#
#               2 patterns                       #
#------------------------------------------------#

# -- Wilf-class 1 -- #

# # The permutations ================================================== > SUCCESS!
# # This class is a bit weird since it is finite. But we can still do it!
# patts = [Permutation([1,2,3]), Permutation([3,2,1])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = None
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 4 # <--------------------------------- Note!
# max_rules     = 100

# -- Wilf-class 2 -- #

# # The permutations ================================================== > SUCCESS!
patts = [Permutation([1,2,3]), Permutation([2,3,1])]
perm_prop = lambda p: all( p.avoids(q) for q in patts )

perm_bound    = 7
ignored       = 4

# The dag
max_len_patt = None
upper_bound  = 3

# Grids
max_rule_size = (3, 3)
max_non_empty = 3
max_rules     = 100

# -- Wilf-class 3 -- #

# # The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,2,3]), Permutation([1,3,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100

# # The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,3,2]), Permutation([3,1,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([2,3,1]), Permutation([3,1,2])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100

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
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100

#------------------------------------------------#
#               4 patterns                       #
#------------------------------------------------#

# We use Simion and Schmidt to eliminate symmetric cases

# The permutations ================================================== > SUCCESS!
# patts = [Permutation([2,3,1]), Permutation([1,3,2]), Permutation([3,1,2]), Permutation([2,1,3])]
# patts = [Permutation([2,3,1]), Permutation([3,2,1]), Permutation([1,3,2]), Permutation([3,1,2])]
# patts = [Permutation([3,1,2]), Permutation([3,2,1]), Permutation([1,3,2]), Permutation([2,1,3])]
# perm_prop = lambda p: all( p.avoids(q) for q in patts )
#
# perm_bound    = 7
# ignored       = 0
#
# # The dag
# max_len_patt = 3
# upper_bound  = 3
#
# # Grids
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
#
# # Creating the dag
inp_dag = permstruct.dag.taylor_dag(patts, max_len_patt=max_len_patt, perm_bound=perm_bound, remove=False, upper_bound=upper_bound)
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
