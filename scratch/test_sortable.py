import permstruct
import permstruct.dag
from permstruct.lib import Permutations

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

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

# Stack-sorting

#-- 1-pass --#

# The perm_props are of course the same

# perm_prop = lambda p: p.avoids([2,3,1])
# perm_prop = lambda p: stack_sort(p) == range(1,len(p)+1)

# perm_bound    = 7
# # inp_dag       = permstruct.dag.N_P_X(perm_prop, perm_bound)
# max_rule_size = (3, 3)
# max_non_empty = 4
# max_rules     = 100
# ignored       = 1

#-- 2-passes --#

# No luck with any of the dags below

perm_prop = lambda p: stack_sort(stack_sort(p)) == range(1,len(p)+1)

perm_bound    = 7
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
max_rule_size = (3, 3)
max_non_empty = 4
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
