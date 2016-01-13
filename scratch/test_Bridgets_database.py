import permstruct
import permstruct.dag
from permstruct.lib import Permutations

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

# Stuff from Bridget's database
# http://math.depaul.edu/bridget/patterns.html

#-- P0004 --#

# Info
# FAILURE with
# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

# R = [[2,1,4,3]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

#-- P0007 --#

# R = [[3,4,2,1], [4,2,3,1], [4,3,1,2]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- P0008 --#

# R = [[3,4,2,1], [4,2,3,1], [4,3,1,2], [4,3,2,1]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- P0016 --#

# Info
# FAILURE
# Details:

# R = [[3,2,1], [2,3,4,1], [3,4,1,2], [4,1,2,3]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- P0028 --#

# Info
# SUCCESS
# Details: This one is very pretty

# R = [[1,3,2], [2,1,3], [4,3,2,1]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- P0029 --#

# R = [[1,3,2,4], [1,3,4,2], [2,4,1,3], [2,4,3,1],
#      [3,1,2,4], [3,1,4,2], [4,2,1,3],
#      [4,2,3,1]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- P0030 --#

# R = [[1,3,2,4], [1,3,4,2], [2,1,4,3], [2,4,1,3],
#      [2,4,3,1], [3,1,2,4], [3,4,1,2], [4,2,1,3],
#      [4,2,3,1]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# # inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
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
