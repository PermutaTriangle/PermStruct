from __future__ import print_function
from permuta import *
import permstruct
import permstruct.dag

import sys


# perm_prop = lambda p: p.avoids([1,2,3])
# perm_prop = lambda p: p.avoids([1,3,2,4])
# perm_prop = lambda p: p.avoids([2,3,1])
# perm_prop = lambda p: p.avoids([2,1,4,3]) and p.avoids([3,1,4,2]) and p.avoids([1,4,3,2]) and p.avoids([1,3,4,2]) and p.avoids([1,3,2,4])
# perm_prop = lambda p: p.avoids([2,4,3,1]) and p.avoids([2,1,4,3]) and p.avoids([3,1,4,2]) and p.avoids([4,1,3,2]) and p.avoids([1,4,3,2]) and p.avoids([1,3,4,2]) and p.avoids([1,3,2,4]) and p.avoids([1,4,2,3]) and p.avoids([1,2,4,3])
# perm_prop = lambda p: p.avoids([4,2,1,3]) and p.avoids([2,1,4,3])
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,3,2,1])
# perm_prop = lambda p: p.avoids([1,2])

patts = [Permutation([1,2])]

# patts = [Permutation([1,3,2]), Permutation([4,3,2,1])]
# patts = [Permutation([3,2,1]), Permutation([1,3,2,4])]
# patts = [Permutation([3,2,1]), Permutation([1,3,2,4]), Permutation([3,4,1,2])]
perm_prop = lambda p: all( p.avoids(q) for q in patts )
perm_bound = 7

# inp_dag = permstruct.dag.N_P_X_mon(perm_prop, perm_bound)
# inp_dag = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# inp_dag = permstruct.dag.N_P_X1_mon1_taylored_for_av_4213_2143(perm_prop, perm_bound)
# inp_dag = permstruct.dag.N_P_X_mon1_taylored_for_av_132_4321(perm_prop, perm_bound)
# inp_dag = permstruct.dag.taylor_dag([Permutation([1,3,2]), Permutation([4,3,2,1])], perm_bound)
# inp_dag = permstruct.dag.N_P_X_mon1_taylored_for_av_132_4321(perm_prop, perm_bound)
inp_dag = permstruct.dag.taylor_dag(patts, max_len_patt=None, perm_bound=perm_bound, remove=True, upper_bound=3)
for el in inp_dag.elements:
    print(el.description if el is not None else 'None')

# sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (2,3), 3, 5, lower_bound=0.2)
# sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (3,3), 3, 100)
sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (2,2), 2, 100)


# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_mon1_taylored_for_av_132_4321(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

for sol in sol_iter:

    print('====================================')
    print("")
    for rule in sol:
        print(rule)
        print("")
