from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag

import sys

# Avoidance of classical patterns of length 2

#------------------------------------------------#
#               1 pattern                        #
#------------------------------------------------#

# -- Wilf-class 1 -- #

# # The permutations ================================================== > SUCCESS!
# patts = [Permutation([1,2])]
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
# max_rule_size = (2, 2)
# max_non_empty = 2
# max_rules     = 100

#------------------------------------------------#
#               2 patterns                        #
#------------------------------------------------#

# -- Wilf-class 1 -- #

# The permutations ================================================== > SUCCESS!
patts = [Permutation([1,2]), Permutation([2,1])]
perm_prop = lambda p: all( p.avoids(q) for q in patts )

perm_bound    = 7
ignored       = 0

# The dag
max_len_patt = None
upper_bound  = 3

# Grids
max_rule_size = (2, 2)
max_non_empty = 2
max_rules     = 100

# Creating the dag
inp_dag = permstruct.dag.taylor_dag(patts, max_len_patt=max_len_patt, perm_bound=perm_bound, remove=True, upper_bound=upper_bound)
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
