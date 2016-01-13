import permstruct
import permstruct.dag
from permstruct.lib import Permutations
import time

def enume(perm_prop, N):
  for n in range(N+1):
    print sum([1 for perm in Permutations(n) if perm_prop(perm)])
  print 'Done counting!'
  time.sleep(5)

def is_increasing(w): return list(w) == range(1,len(w)+1)

def loc_max(w):
    '''
    Helper function for stack-sort and bubble-sort. Returns the index of the
    maximal element in w. It is assumed that w is non-empty.
    '''

    m = w[0]
    i = 0
    c = 0

    for j in w[1:]:
        c = c+1
        if j > m:
            m = j
            i = c
    return i, m

def stack_sort(w):
    '''
    Function takes a permutation w and does one pass of stack-sort on it
    '''

    i = len(w)

    if i <= 1:
        return list(w)

    j,J = loc_max(w)

    if j == 0:
        W2 = stack_sort(w[1:i])
        W2.append(J)

        return W2

    if j == i-1:
        W1 = stack_sort(w[0:i-1])
        W1.append(J)

        return W1

    W1 = stack_sort(w[0:j])
    W2 = stack_sort(w[j+1:i])

    W1.extend(W2)
    W1.extend([J])

    return W1

def is_stack_sortable(w): return stack_sort(w) == range(1,len(w)+1)

def avoids_vinc_132(p):
  for i in range(len(p)-2):
    for j in range(i+1,len(p)-1):
      if p[i] < p[j+1] < p[j]: return False
  return True

def avoids_vinc_231(p):
  for i in range(len(p)-2):
    for j in range(i+2,len(p)):
      if p[j] < p[i] < p[i+1]: return False
  return True

# (123, {}, {2})
def avoids_covinc_123(p):
  for i in range(len(p)-2):
    for j in range(i+1,len(p)-1):
      for k in range(j+1,len(p)):
        if (p[i] < p[j]) and (p[k] == p[j]+1): return False
  return True

def avoids_many(perm, patterns):
	return all(perm.avoids(pattern) for pattern in patterns)

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

perm_bound    = 7

# The increasing perms
# perm_prop = is_increasing

# inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
# max_rule_size = (2, 2)


# ------------------------------------------------------------------------------


# 231 avoiding perms
# perm_prop = lambda p: is_stack_sortable(p)

# inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
# max_rule_size = (3, 3)


# ------------------------------------------------------------------------------


# Perms avoiding 231 (with 2 and 3 adjacent)
# perm_prop = lambda p: avoids_vinc_231(p)

# inp_dag       = permstruct.dag.N_P_X_mon(perm_prop, perm_bound)
# max_rule_size = (3, 3)


# ------------------------------------------------------------------------------


# Av(132, 4231)
# perm_prop = lambda p: avoids_many(p,[[1,3,2], [4,2,3,1]])

# inp_dag       = permstruct.dag.N_P_X_taylored_for_av_132_4231(perm_prop, perm_bound)
# max_rule_size = (3, 3)


# ------------------------------------------------------------------------------

# Av(321, 2134)
# perm_prop = lambda p: avoids_many(p,[[3,2,1], [2,1,3,4]])

# inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
# max_rule_size = (3, 3)


# ------------------------------------------------------------------------------


# Av(123)
perm_prop = lambda p: p.avoids([1, 2, 3])

inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
max_rule_size = (4, 4)


# ------------------------------------------------------------------------------

# Av(4213, 2143)
# perm_prop = lambda p: p.avoids([4,2,1,3]) and p.avoids([2,1,4,3])

# inp_dag       = permstruct.dag.N_P_X1_mon1_taylored_for_av_4213_2143(perm_prop, perm_bound)
# max_rule_size = (5, 5)


# ------------------------------------------------------------------------------

# From Masaki's thesis
L = [[4,1,2,3], [4,2,1,3], [4,1,3,2]]
perm_prop = lambda p: avoids_many(p,L)

inp_dag       = permstruct.dag.N_P_X2(perm_prop, perm_bound)
max_rule_size = (6, 6)


max_non_empty = 6
max_rules     = 10
ignored       = 0

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


# Arc permutations
# L = [[1, 3, 2, 4], [1, 3, 4, 2], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [4, 2, 1, 3], [4, 2, 3, 1]]
# perm_prop = lambda p: avoids_many(p,L)

# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# max_rule_size = (4, 4)



# From Lara's table
# L = [[1,3,4,2], [1,4,3,2]]
# L = [[1,4,2,3], [3,1,4,2]]
# L = [[1,2,4,3], [3,1,2,4], [4,3,1,2]]
# L = [[1,2,3,4], [1,2,4,3], [1,4,2,3], [4,1,2,3]]
# L = [[1,2,3,4], [1,3,2,4], [1,3,4,2], [2,1,3,4]]
# L = [[4,3,2,1], [3,4,2,1], [3,2,4,1], [2,4,1,3], [4,2,1,3], [4,1,3,2]]

# perm_prop = lambda p: avoids_many(p, L)

# inp_dag       = permstruct.dag.N_P_X3_mon2(perm_prop, perm_bound)
# max_rule_size = (4, 4)

# ------------------------------------------------------------------------------

# From Bruners binomial paper (http://arxiv.org/pdf/1505.04929v2.pdf)
# L = [[2,4,3,1], [4,2,3,1], [1,4,3,2], [4,1,3,2]]

# Albert et al (The insertion encoding of permutations)
# L = [[3,1,2,4], [4,1,2,3], [3,1,4,2], [4,1,3,2]]

# List found by Bruner and conjectured to be Wilf-equivalent (some known)
# L = [[1,2,3,4], [1,2,4,3], [1,3,2,4], [1,3,4,2]]
# L = [[1,2,3,4], [1,2,4,3], [1,3,4,2], [1,4,2,3]]
# L = [[1,2,3,4], [1,2,4,3], [1,3,4,2], [2,3,4,1]]
# L = [[1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,2,3]]
# L = [[1,2,4,3], [1,3,2,4], [1,3,4,2], [1,4,3,2]]

# L = [[1,2,4,3], [2,1,4,3], [2,4,1,3], [2,4,3,1]]
# L = [[1,3,2,4], [1,3,4,2], [1,4,2,3], [1,4,3,2]]
# L = [[1,3,2,4], [1,3,4,2], [1,4,3,2], [4,1,3,2]]
# L = [[1,3,4,2], [1,4,2,3], [1,4,3,2], [2,4,3,1]]
# L = [[1,3,4,2], [2,4,1,3], [2,4,3,1], [3,1,4,2]]

# perm_prop = lambda p: avoids_many(p, L)

# inp_dag       = permstruct.dag.len_3_pairs_X1(perm_prop, perm_bound)
# max_rule_size = (4, 4)