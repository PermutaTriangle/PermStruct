import permstruct
import permstruct.dag
from permstruct.lib import Permutations
import time

def enume(perm_prop, N):
  for n in range(N+1):
    print sum([1 for perm in Permutations(n) if perm_prop(perm)])
  print 'Done counting!'
  time.sleep(5)

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

# Avoiding one classical pattern of length 3 and two of length 4

#-- Symmetry-class 1 --#

# Info
# SUCCESS!
# Details: A116721
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([1, 3, 2, 4])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 2 --#

# Info
# FAILURE
# Details: A116735
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([1, 3, 4, 2])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 3 --#

# Info
# FAILURE
# Details: A116728
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([2, 1, 3, 4])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 4 --#

# Info
# FAILURE
# Details: A116731
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([2, 1, 4, 3])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 5 --#

# Info
# FAILURE
# Details: A116729
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([2, 3, 1, 4])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 6 --#

# Info
# FAILURE
# Details: A116711
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([2, 3, 4, 1])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 7 --#

# Info -> Symmetry-class 1
# FAILURE
# Details: A116721
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([2, 4, 1, 3])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 8 --#

# Info
# FAILURE
# Details: A116727
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([3, 4, 1, 2])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 9 --#

# Info -> Symmetry-class 4
# FAILURE
# Details: A116731
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 2, 4]) and p.avoids([1, 3, 4, 2])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 10 --#

# Info -> Symmetry-class 4
# FAILURE
# Details: A116731
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 2, 4]) and p.avoids([2, 1, 4, 3])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 11 --#

# Info
# FAILURE
# Details: A116733
#

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 2, 4]) and p.avoids([2, 3, 4, 1])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 12 --#

# Info
# FAILURE
# Details: A027927
#          Number of plane regions after drawing (general position) convex n-gon
#          and all diagonals.
#          G.f.: x^2*(1-3*x+5*x^2-3*x^3+x^4)/(1-x)^5

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 2, 4]) and p.avoids([2, 4, 1, 3])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 13 --#

# Lemma
# Av(321, 132, 3412) is needed as a unit

# Info
# SUCCESS!
# Details: 1, 1, 2, 4, 8, 10, 12, 14, 16
#          NOT ON OEIS

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 2]) and p.avoids([3, 4, 1, 2])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

# Info
# SUCCESS!
# Details: Seems to be A046092 after length 3 (non-inclusive)
#          4 times triangular numbers: 2*n*(n+1)
#          G.f.:   4*x/(1-x)^3
#          E.g.f.: exp(x)*(2*x^2+4*x)
#
#          BUT: There is no mention of permutations or patterns for this
#          sequence!
#
# The exact cover was VERY slow on this problem. We should modify it so it
# covers the short permutations first.

perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 2, 4]) and p.avoids([3, 4, 1, 2])
# enume(perm_prop, 8)

perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
inp_dag       = permstruct.dag.N_P_taylored_for_av_321_1324_3412(perm_bound)
max_rule_size = (5, 5)
max_non_empty = 5
max_rules     = 8
ignored       = 1

#-- Symmetry-class 14 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([1, 4, 2, 3])

#-- Symmetry-class 15 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([2, 1, 4, 3])

#-- Symmetry-class 16 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([2, 3, 1, 4])

#-- Symmetry-class 17 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([2, 3, 4, 1])

#-- Symmetry-class 18 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([2, 4, 1, 3])

#-- Symmetry-class 19 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([3, 1, 2, 4])

#-- Symmetry-class 20 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([3, 1, 4, 2])

#-- Symmetry-class 21 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([3, 4, 1, 2])

#-- Symmetry-class 22 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 3, 4, 2]) and p.avoids([4, 1, 2, 3])

#-- Symmetry-class 23 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 1, 4, 3]) and p.avoids([2, 3, 4, 1])

#-- Symmetry-class 24 --#

# Info
# SUCCESS!
# Details: A000325
#          These seem to be the Grassmannian permutations

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 1, 4, 3]) and p.avoids([2, 4, 1, 3])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 25 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 1, 4, 3]) and p.avoids([3, 4, 1, 2])

#-- Symmetry-class 26 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 3, 4, 1]) and p.avoids([2, 4, 1, 3])

#-- Symmetry-class 27 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 3, 4, 1]) and p.avoids([3, 4, 1, 2])

#-- Symmetry-class 28 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 3, 4, 1]) and p.avoids([4, 1, 2, 3])

#-- Symmetry-class 29 --#

# Info
# SUCCESS!
# Details: A034943

# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 4, 1, 3]) and p.avoids([3, 1, 4, 2])
# enume(perm_prop, 8)

# perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 3
# max_rules     = 100
# ignored       = 1

#-- Symmetry-class 30 --#
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([2, 4, 1, 3]) and p.avoids([3, 4, 1, 2])

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
