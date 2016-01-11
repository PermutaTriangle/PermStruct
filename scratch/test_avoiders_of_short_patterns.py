import permstruct
import permstruct.dag

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

# Avoidance of one classical pattern of length 1
# As is expected the first dag suffices

# perm_prop     = lambda p: p.avoids([1])

# perm_bound    = 6
# inp_dag       = permstruct.dag.N_P(perm_bound)
# # inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
# max_rule_size = (1, 1)
# max_non_empty = 1
# max_rules     = 100
# ignored       = 0

#------------------------------------------------#

# Avoidance of one classical pattern of length 2
# As expected the first dag suffices. Using the X1 and X2
# versions will require more rules, as there are special
# cases which can be combined by the N_P_X dag

# perm_prop     = lambda p: p.avoids([1,2])

# perm_bound    = 6
# inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X1(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X2(perm_prop, perm_bound)
# max_rule_size = (2, 2)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#------------------------------------------------#

# Avoidance of two classical patterns of length 2
# As expected this find the unique rule that only generates
# the permutation 1

perm_prop     = lambda p: p.avoids([1,2]) and p.avoids([2,1])

perm_bound    = 6
inp_dag       = permstruct.dag.N_P(perm_bound)
max_rule_size = (2, 2)
max_non_empty = 3
max_rules     = 100
ignored       = 1

#------------------------------------------------#

if not overlays:
    permstruct.exhaustive(perm_prop,
                          perm_bound,
                          inp_dag,
                          max_rule_size,
                          max_non_empty,
                          max_rules,
                          ignore_first = ignored)

else:
    permstruct.exhaustive_with_overlays(perm_prop,
                                        perm_bound,
                                        inp_dag,
                                        max_rule_size,
                                        max_non_empty,
                                        max_rules,
                                        overlay_dag,
                                        max_overlay_cnt,
                                        max_overlay_size,
                                        min_rule_size=(1,1))
