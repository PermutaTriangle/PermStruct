import permstruct
import permstruct.dag
from permuta import Permutations

# Since we usually don't want overlays:
overlays = False

# In most of the test cases below we do not include symmetries


# R = [[2,3,1], [1,5,4,3,2]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)
# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X1_taylored_for_av_231_15432(perm_prop, perm_bound)
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# R = [[2,3,1], [1,5,4,2,3]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)
# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X1_taylored_for_av_231_15423(perm_prop, perm_bound)
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# R = [[2,3,1], [1,5,3,2,4]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)
# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X1_taylored_for_av_231_15324(perm_prop, perm_bound)
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# R = [[2,3,1], [1,5,2,3,4]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)
# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X1_taylored_for_av_231_15234(perm_prop, perm_bound)
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# R = [[2,3,1], [1,2,5,3,4]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)
# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_231_12534(perm_prop, perm_bound)
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# for n in range(6):
# 	for perm in Permutations(n):
# 		if perm.avoids([2,3,1]):
# 			print perm,
# 	print ""
# 	print ""

#------------------------------------------------#

# Avoiding two classical patterns of length 4
# JUST THE CLASSES WITH POLYNOMIAL GENERATING FUNCTIONS TO BEGIN WITH

#-- Wilf class 1 --#

# This one is finite like Av(123, 321) so we can do it if we
# allow enough rules, and allow them to be large enough
# perm_prop = lambda p: p.avoids([4,3,2,1]) and p.avoids([1,2,3,4])

#-- Wilf class 2 --#

# No success with
# perm_bound = 6
# dag = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# max_rule_size = (4, 4)
# max_non_empty = 5
# perm_prop = lambda p: p.avoids([4,3,1,2]) and p.avoids([1,2,3,4])

#-- Wilf class 5 --#

#perm_prop = lambda p: p.avoids([4,3,2,1]) and p.avoids([1,3,2,4])

#-- Separable --#

# R = [[2,4,1,3], [3,1,4,2], [2,1,4,3], [3,4,1,2]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_prop = lambda p: p.avoids([2,4,1,3]) and p.avoids([3,1,4,2])
# perm_prop = lambda p: p.avoids([2,1,4,3]) and p.avoids([3,4,1,2])

# perm_prop = lambda p: p.avoids([4,2,3,1]) and p.avoids([3,2,4,1])

# Atkinson, big example from p. 31
# No luck
# R = [[1,2,3,4], [1,2,4,3], [1,3,2,4], [2,1,3,4], [1,4,5,2,3], [3,4,1,2,5], [3,5,1,6,2,4], [3,5,6,1,2,4], [4,5,1,6,2,3], [4,5,6,1,2,3]]
# perm_prop = lambda p: all( p.avoids(x) for x in R)
# perm_bound    = 7
# inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

# Obtained by a rifle shuffle of a deck of cards. See Atkinson p. 29
# Note that we have already done Av(321,2143). See Prop 3.4. Might be
# good to illustrate how Struct can do most of the work here.
perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,1,4,3]) and p.avoids([2,4,1,3])
# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,1,4,3]) and p.avoids([2,4,1,3]) and p.avoids([3,1,4,2])
perm_bound    = 7
inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
max_rule_size = (3, 3)
max_non_empty = 3
max_rules     = 100
ignored       = 1

#------------------------------------------------#

# The following classical patterns of length 4 are broken down
# by Wilf-classes

# Can we do any of these?

#-- Wilf class 1 --#

# perm_prop = lambda p: p.avoids([1,3,4,2])
# perm_prop = lambda p: p.avoids([2,4,1,3])

#-- Wilf class 2 --#

# perm_prop = lambda p: p.avoids([1,2,3,4])
# perm_prop = lambda p: p.avoids([1,2,4,3])
# perm_prop = lambda p: p.avoids([1,4,3,2])
# perm_prop = lambda p: p.avoids([2,1,4,3])

#-- Wilf class 3 --#

# perm_prop = lambda p: p.avoids([1,3,2,4])

# Nothing non-trivial found with the settings below
# Will at least need to allow avoiders of a single pattern
# of length 3
# perm_bound    = 7
# inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

# def is_Baxter(perm):
#     n = len(perm)
#     if n <= 3: return True

#     for i in range(n-3):
#         for j in range(i+1,n-2):
#             for k in range(j+2,n):
#                 if (perm[j+1] < perm[i] < perm[k] < perm[j]) or (perm[j] < perm[k] < perm[i] < perm[j+1]):
#                     return False
#     return True

# perm_prop = lambda p: is_Baxter(p)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#------------------------------------------------#

# perm_bound = 6

# inp_dag = permstruct.dag.elementary(perm_prop, perm_bound)
# inp_dag = permstruct.dag.incr_decr(perm_prop, perm_bound)
# overlay_dag = permstruct.dag.elementary(perm_prop, perm_bound)
# overlay_dag = permstruct.dag.x_dag(perm_prop, perm_bound)
# inp_dag = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# inp_dag = permstruct.dag.decr_dag(perm_prop, perm_bound)
# inp_dag = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# inp_dag = permstruct.dag.classic_avoiders_length_3_with_input_without_incrdecr(perm_prop, perm_bound)
# inp_dag = permstruct.dag.len_3_pairs(perm_prop, perm_bound)

# max_rule_size = (1, 1)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 0

# For exhaustive_with_overlays
# overlay_dag = permstruct.dag.x_dag(perm_prop, perm_bound)
# max_overlay_cnt = 1
# max_overlay_size = (1, 3)

# overlays = False

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
