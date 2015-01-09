import permstruct
import permstruct.dag
from permstruct.lib import Permutations
import time

def enume(perm_prop, N):
  for n in range(N+1):
    print sum([1 for perm in Permutations(n) if perm_prop(perm)])
  print 'Done counting!'
  time.sleep(5)

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

def avoids_Anders(p):
  for i in range(len(p)-2):
    for j in range(i+1,len(p)-1):
      if p[i] < p[j] < p[j+1]: return False
  return True

def avoids_Christian(p):
  for i in range(len(p)-2):
    for j in range(i+1,len(p)-1):
      for k in range(j+1,len(p)):
        if (p[i] < p[j]) and (p[k] == p[j]+1): return False
  return True

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

# The increasing perms
# perm_prop = lambda p: list(p) == range(1,len(p)+1)

# The stack-sortable perms
# perm_prop = lambda p: stack_sort(p) == range(1,len(p)+1)

# Anders' example
# perm_prop = lambda p: avoids_Anders(p)

# Christian's example
# perm_prop = lambda p: avoids_Christian(p) and p.avoids([1,3,2])

# Av(321, 1243, 1324)
# perm_prop = lambda p: p.avoids([3, 2, 1]) and p.avoids([1, 2, 4, 3]) and p.avoids([1, 3, 2, 4])

# Av(123)
perm_prop = lambda p: p.avoids([1, 2, 3])
# enume(perm_prop, 8)

perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
inp_dag       = permstruct.dag.N_P_X_mon1(perm_prop, perm_bound)
max_rule_size = (3, 3)
max_non_empty = 4
max_rules     = 100
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
