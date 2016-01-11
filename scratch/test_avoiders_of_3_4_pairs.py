import permstruct
import permstruct.dag
from permuta import Permutations

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

# Avoiding one classical pattern of length 3 and one of length 4

#-- Wilf class 1 --#

# This one is finite like Av(123, 321) so we can do it if we
# allow enough rules, and allow them to be large enough.
# The following settings might be enough, but I haven't waited
# for the exact cover to finish

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([1,2,3,4])

# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P(perm_bound)
# max_rule_size = (6, 6)
# max_non_empty = 6
# max_rules     = 72 # There are only 72 permutations in Av(321, 1234)
# ignored       = 1

#-- Wilf class 2 --#

# mon1 is necessary
# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,1,3,4])

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Wilf class 3 --#

# Note the two inp_dag options. Both work, but the taylored one
# is much faster.

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,3,2,1])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_mon1_taylored_for_av_132_4321(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- Wilf class 4 --#

# Might need to special case the 21, instead of the full decreasing
# because of the avoiding 321 thing .... This might also be needed
# in others where this 321 occurs

# No success :(

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([1,3,2,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_mon1_taylored_for_av_321_1324(perm_prop, perm_bound)
# max_rule_size = (4, 4)
# max_non_empty = 6
# max_rules     = 100
# ignored       = 1

#-- Wilf class 5 --#

# No success :(

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([1,3,4,2])

# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X2_mon2_taylored_for_av_321_1342(perm_prop, perm_bound)
# max_rule_size = (4, 4)
# max_non_empty = 6
# max_rules     = 100
# ignored       = 1

#-- Wilf class 6 --#

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,1,4,3])

# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X_mon2(perm_prop, perm_bound)
# max_rule_size = (5, 5)
# max_non_empty = 6
# max_rules     = 100
# ignored       = 1

#-- Wilf class 7 --#

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,3,1,2])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_mon2_taylored_for_av_132_4312(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,2,3,1])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_132_4231(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- Wilf class 8 --#

# Note that we can reuse the dag taylored for Av(132, 4321)
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,2,1,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_mon1_taylored_for_av_132_4321(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- Wilf class 9 --#

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,3,4,1])
# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([3,4,1,2])
# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1


perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([3,1,4,2])

perm_bound    = 8
inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
max_rule_size = (3, 3)
max_non_empty = 3
max_rules     = 100
ignored       = 1

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([1,2,3,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_132_1234(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,2,1,3])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_132_4213(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# Note that we can reuse the dag taylored for Av(132, 1234)
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,1,2,3])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_132_1234(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# Note that we can reuse the dag taylored for Av(132, 4312)
# Note that we reduce max_rules to 10 (from the usual 100). Having
# it at 100 seemed to really slow the exact cover computation and
# having it at 10 is sufficient to find a ton of rules
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,1,2,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_132_4312(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 10
# ignored       = 1

# Note that we can reuse the dag taylored for Av(132, 4213)
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([2,1,3,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_132_4213(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,4,1,2])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X1_mon(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

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
