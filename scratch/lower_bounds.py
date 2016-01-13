import permstruct
import permstruct.dag

import sys


# perm_prop = lambda p: p.avoids([1,2,3])
perm_prop = lambda p: p.avoids([1,3,2,4])
# perm_prop = lambda p: p.avoids([2,3,1])
perm_bound = 6

# inp_dag = permstruct.dag.N_P_X_mon(perm_prop, perm_bound)
inp_dag = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)

sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (2,3), 3, 5, lower_bound=0.2)
# sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (3,3), 3, 100)

for sol in sol_iter:

    print '===================================='
    print ""
    for rule in sol:
        print(rule)
        print ""

