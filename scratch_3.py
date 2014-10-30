import permstruct
import permstruct.dag

perm_prop = lambda p: p.avoids([1,2,3])
# perm_prop = lambda p: p.avoids([1,2])
perm_bound = 6
# dag = permstruct.dag.elementary(perm_prop, perm_bound)
dag = permstruct.dag.decr_dag(perm_prop, perm_bound)

# sol_iter = permstruct.exhaustive(perm_prop, perm_bound, dag, (3, 3), 4, 4)
# sol_iter = permstruct.exhaustive_with_overlays(perm_prop, perm_bound, dag, (2, 3), 4, 4, dag, 1, (1, 3), min_rule_size=(2,3))
sol_iter = permstruct.exhaustive_with_overlays(perm_prop, perm_bound, dag, (2, 3), 3, 1, permstruct.dag.x_dag(perm_prop, perm_bound), 1, (1, 3), min_rule_size=(2,3))

for sol in sol_iter:

    print '===================================='
    print ""
    for rule in sol:
        print(rule)
        print ""

