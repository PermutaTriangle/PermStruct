import permstruct
import permstruct.dag

# Since we usually don't want overlays:
overlays = False

# In most of the test cases below we do not include symmetries

def avoids_132_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[i] < perm[k] < perm[i]:
                return False
    return True

def avoids_231_dotted(perm):
  if len(perm) < 2: return True

  for i in range(len(perm)):
    for j in range(i+1,len(perm)):
      if j < len(perm) and perm[i] > perm[j]:
        if all(not(perm[j] < perm[k] < perm[i]) for k in range(i)) and all(perm[k] < perm[j] for k in range(i+1,j)):
           return False
  return True

#------------------------------------------------#

# Avoidance of one classical pattern of length 1

perm_prop     = lambda p: p.avoids([1,3,2]) and avoids_231_dotted(p)
perm_prop     = lambda p: p.avoids([1,2,3]) and avoids_132_vinc(p)

perm_bound    = 7
# inp_dag       = permstruct.dag.elementary(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.elementary_X_minus_epsilon(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.incr_decr_nonempty_X_minus_epsilon(perm_prop, perm_bound)
inp_dag       = permstruct.dag.taylored_for_av_132_231_dotted(perm_prop, perm_bound)
max_rule_size = (4, 4)
max_non_empty = 4
max_rules     = 20
ignored       = 0

# overlay_dag = permstruct.dag.x_dag(perm_prop, perm_bound)
# max_overlay_cnt = 1
# max_overlay_size = (1, 3)

# overlays = True

#------------------------------------------------#

# Avoidance of one classical pattern of length 2

# perm_prop     = lambda p: p.avoids([1,2])

# perm_bound    = 6
# inp_dag       = permstruct.dag.elementary(perm_prop, perm_bound)
# max_rule_size = (2, 2)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#------------------------------------------------#

# Avoidance of two classical patterns of length 2

# perm_prop     = lambda p: p.avoids([1,2]) and p.avoids([2,1])

# perm_bound    = 6
# inp_dag       = permstruct.dag.elementary(perm_prop, perm_bound)
# max_rule_size = (2, 2)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#------------------------------------------------#

# Avoidance of one classical pattern of length 3

# This is really fast, e.g., with

# perm_prop     = lambda p: p.avoids([2,3,1])

# perm_bound    = 6
# inp_dag       = permstruct.dag.elementary(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# Note that the overlays are still a bit broken - and they
# can not use our neighborhood restrictions
# perm_prop = lambda p: p.avoids([1,2,3])

# perm_bound    = 6
# inp_dag       = permstruct.dag.decr_dag(perm_prop, perm_bound)
# max_rule_size = (2, 3)
# max_non_empty = 3
# max_rules     = 10
# ignored       = 1

# overlay_dag = permstruct.dag.x_dag(perm_prop, perm_bound)
# max_overlay_cnt = 1
# max_overlay_size = (1, 3)

# overlays = True

#------------------------------------------------#

# Pairs of classical patterns of length 3

#-- Wilf class 1 --#

# This class is a bit special, since it is finite. But it does
# look like we can do it, e.g., with

# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([3,2,1])

# perm_bound    = 7
# inp_dag       = permstruct.dag.elementary(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Wilf class 2 --#

# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([2,3,1])

# perm_bound    = 7
# inp_dag       = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 2
# max_rules     = 100
# ignored       = 1

#-- Wilf class 3 --#

# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([1,3,2])
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,1,2])
# perm_prop = lambda p: p.avoids([2,3,1]) and p.avoids([3,1,2])

# perm_bound    = 7
# inp_dag       = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#------------------------------------------------#

# Avoiding one classical pattern of length 3 and one of length 4

#-- Wilf class 1 --#

# This one is finite like Av(123, 321) so we can do it if we
# allow enough rules, and allow them to be large enough.
# The following settings ARE NOT ENOUGH!

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([1,2,3,4])

# perm_bound    = 7
# inp_dag       = permstruct.dag.elementary(perm_prop, perm_bound)
# max_rule_size = (5, 5)
# max_non_empty = 6
# max_rules     = 100
# ignored       = 1

#-- Wilf class 2 --#

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,1,3,4])

# perm_bound    = 6
# inp_dag       = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Wilf class 3 --#

# Note the two inp_dag options. Both work, but the taylored one
# is much faster.

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,3,2,1])

# perm_bound    = 7
# inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_4321(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Wilf class 4 --#

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([1,3,2,4])

# Might need to special case the 21, instead of the full decreasing
# because of the avoiding 321 thing .... This might also be needed
# in others where this 321 occurs

# perm_bound    = 7
# inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# # inp_dag       = permstruct.dag.incr_decr_nonempty(perm_prop, perm_bound)
# max_rule_size = (4, 4)
# max_non_empty = 6
# max_rules     = 100
# ignored       = 1

#-- Wilf class 5 --#

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([1,3,4,2])

#-- Wilf class 6 --#

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,1,4,3])

#-- Wilf class 7 --#

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,3,1,2])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_4312(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,2,3,1])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_4231(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Wilf class 8 --#

# Note that we can reuse the dag taylored for Av(132, 4321)
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,2,1,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_4321(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- Wilf class 9 --#

# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([2,3,4,1])
# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([3,4,1,2])
# perm_prop = lambda p: p.avoids([3,2,1]) and p.avoids([3,1,4,2])

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([1,2,3,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_1234(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,2,1,3])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_4213(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# Note that we can reuse the dag taylored for Av(132, 1234)
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([4,1,2,3])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_1234(perm_prop, perm_bound)
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
# inp_dag       = permstruct.dag.taylored_for_av_132_4312(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 10
# ignored       = 1

# Note that we can reuse the dag taylored for Av(132, 4213)
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([2,1,3,4])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_4213(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,4,1,2])

# perm_bound    = 7
# # inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.taylored_for_av_132_3412(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

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
