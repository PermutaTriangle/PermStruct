from __future__ import print_function
from permuta import *
# from permuta.misc import subsets
from itertools import combinations
import permstruct
import permstruct.dag
from permstruct import *
from permstruct.dag import taylor_dag

import sys

is_classical = True

import random

# Avoidance of a large subset of classical patterns of length 4

num_patts = 22
subset_no = 0 # zero indexed


# s = random.randint(1,1000)
# s = 708
# random.seed(s)
# num_patts = random.randint(1,23)

S4 = list(Permutations(4))
# random.shuffle(L)
patts = list(combinations(S4,num_patts))[subset_no]
patts = list(patts)

print(patts)

perm_bound    = 8
verify_bound  = 10
ignored       = 0

# The dag
max_len_patt = 2
upper_bound  = 1
remove       = True

# Grids
max_rule_size = (4, 4)
max_non_empty = 4
max_rules     = None

# ===================================================

settings = StructSettings(
        perm_bound=perm_bound,
        verify_bound=verify_bound,
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

print('The seed was %d' %s)

'''
Results
num_patts = 24
Finite, so we can do that

num_patts = 23
Obviously finite if the basis B contains both 1234 and 4321. Otherwise assume
that it contains 1234, but not 4321. In this case we clearly have every
decreasing permutation in Av(B), and also every permutation that is shorter
than 4. But there are no other permutations in Av(B).

num_patts = 22
'''
