import permstruct
import permstruct.dag

import sys


# perm_prop = lambda p: p.avoids([1,2,3])
# perm_prop = lambda p: p.avoids([1,3,2,4])
# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,1,3,4])
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,3,2,1])
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,2,1])
# perm_prop = lambda p: True
perm_prop = lambda p: p.avoids([2,3,1])
# perm_prop = lambda p: p.avoids([1,2])
# perm_prop = lambda p: p.avoids([1])

perm_bound = 6

# inp_dag = permstruct.dag.elementary(perm_prop, perm_bound)
# inp_dag = permstruct.dag.incr_decr(perm_prop, perm_bound)
# overlay_dag = permstruct.dag.elementary(perm_prop, perm_bound)
# overlay_dag = permstruct.dag.x_dag(perm_prop, perm_bound)
# inp_dag = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# inp_dag = permstruct.dag.decr_dag(perm_prop, perm_bound)
# inp_dag = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# inp_dag = permstruct.dag.classic_avoiders_length_3_with_input_without_incrdecr(perm_prop, perm_bound)
inp_dag = permstruct.dag.len_3_pairs(perm_prop, perm_bound)

# Found 19525 rules, 86 of which are valid, 72 of which are distinct
# Found 12445 rules, 86 of which are valid, 72 of which are distinct
# Found 3361 rules, 86 of which are valid, 72 of which are distinct

# Found 19525 rules, 93 of which are valid, 82 of which are distinct
# Found 15217 rules, 93 of which are valid, 82 of which are distinct

# Found 724411 rules, 86 of which are valid, 72 of which are distinct
# Found 184507 rules, 86 of which are valid, 72 of which are distinct
# Found 30727 rules, 86 of which are valid, 72 of which are distinct


# for k, v in permstruct.find_allowed_neighbors(inp_dag.elements).items():
#     print('------------------------')
#     print(k)
#     for x in v:
#         print(x)
# 
# 
# sys.exit(0)


# sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (4, 4), 6, 6, ignore_first=1)
# sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (4, 4), 4, 6, ignore_first=1)
# sol_iter = permstruct.construct_rule(perm_prop, perm_bound, inp_dag, (3, 3), 4, 100)
sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (3, 3), 3, 100)
# sol_iter = permstruct.construct_rule(perm_prop, perm_bound, inp_dag, (3, 3), 4, 100)
# sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (3, 3), 4, 100)
# sol_iter = permstruct.exhaustive_with_overlays(perm_prop, perm_bound, inp_dag, (2, 3), 4, 4, overlay_dag, 1, (1, 3), min_rule_size=(2,3))
# sol_iter = permstruct.exhaustive_with_overlays(perm_prop, perm_bound, inp_dag, (2, 3), 4, 5, overlay_dag, 1, (1, 3), min_rule_size=(2,3))

# permstruct.exhaustive(perm_prop, perm_bound, dag, (3, 3), 4, 5)

# for sol in sol_iter:
# 
#     print '===================================='
#     print ""
#     for rule in sol:
#         print(rule)
#         print ""
# 
