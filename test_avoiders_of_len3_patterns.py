import permstruct
import permstruct.dag

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#


# Avoidance of one classical pattern of length 3

# This is really fast. If one uses the X1 or X2 versions
# then rules split into special cases

# perm_prop     = lambda p: p.avoids([2,3,1])

# perm_bound    = 6
# inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
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
# inp_dag       = permstruct.dag.N_P(perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Wilf class 2 --#

# Here we *must* use mon1 as mon is not specific enough.
# More precisely we must have a non-empty decreasing unit

# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([2,3,1])

# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 2
# max_rules     = 100
# ignored       = 1

#-- Wilf class 3 --#

# X_mon is fastest, the others give special cases
# The outputted rules for the second perm_prop lead to (trivial)
# different representations of the enumerations sequence, 2^(n-1)

# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([1,3,2])
# perm_prop = lambda p: p.avoids([1,3,2]) and p.avoids([3,1,2])
perm_prop = lambda p: p.avoids([2,3,1]) and p.avoids([3,1,2])

perm_bound    = 7
inp_dag       = permstruct.dag.N_P_X_mon(perm_prop, perm_bound)
max_rule_size = (3, 3)
max_non_empty = 3
max_rules     = 100
ignored       = 1

#------------------------------------------------#

# Triples of classical patterns of length 3

# We use Simion and Schmidt to elminate symmetric cases
# The first one of these gives the Fibonacci enumeration, via the usual
# generating function.

# For some of these mon1 gives simpler smaller rules

# R = [[1,2,3], [1,3,2], [2,1,3]]
# # R = [[1,2,3], [1,3,2], [2,3,1]]
# # R = [[1,3,2], [2,1,3], [2,3,1]]
# # R = [[1,2,3], [1,3,2], [3,1,2]]
# # R = [[1,2,3], [2,3,1], [3,1,2]]
# # We ignore the case when {123, {321} subset R
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#------------------------------------------------#

# Triples of classical patterns of length 3

# We use Simion and Schmidt to elminate symmetric cases
# Some of these are the Fibonacci numbers - what formulas
# can we discover for them?

# For some of these mon1 gives simpler smaller rules

# R = [[1,2,3], [1,3,2], [2,1,3]]
# R = [[1,2,3], [1,3,2], [2,3,1]]
# R = [[1,3,2], [2,1,3], [2,3,1]]
# R = [[1,2,3], [1,3,2], [3,1,2]]
# R = [[1,2,3], [2,3,1], [3,1,2]]
# We ignore the case when {123, {321} subset R
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#------------------------------------------------#

# Four classical patterns of length 3

# We use Simion and Schmidt to elminate symmetric cases

# The N_P_X dag is not enough to do the first class, since that class is the
# union of the increasing and the decreasing permutations. Perhaps we need to
# use a recursive version of instruct (= learnstruct) on it, or use a local
# self-referential rule. Another way around might be to allow subtraction of
# rules.

# R = [[2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3]]
# R = [[2, 3, 1], [3, 2, 1], [1, 3, 2], [3, 1, 2]]
# R = [[3, 1, 2], [3, 2, 1], [1, 3, 2], [2, 1, 3]]
# We ignore the case when {123, {321} subset R
# perm_prop = lambda p: all( p.avoids(x) for x in R)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
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
