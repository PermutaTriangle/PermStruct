import permstruct
import permstruct.dag

# Since we usually don't want overlays:
overlays = False

#------------------------------------------------#

# The permutation classes equinumerous to the Smooth class, see the
# paper "The permutation classes equinumerous to the Smooth class" by
# Miklos Bona

# I have not tested these extensively, but we probably need something more
# powerful

# perm_prop     = lambda p: p.avoids([1,3,2,4]) and p.avoids([2,1,4,3])
# perm_prop     = lambda p: p.avoids([1,3,4,2]) and p.avoids([2,4,3,1])
perm_prop     = lambda p: p.avoids([1,3,4,2]) and p.avoids([3,2,4,1])
# perm_prop     = lambda p: p.avoids([1,3,4,2]) and p.avoids([2,3,1,4])
# perm_prop     = lambda p: p.avoids([1,3,2,4]) and p.avoids([2,4,1,3])

perm_bound    = 8
# inp_dag       = permstruct.dag.N_P_X2_mon2(perm_prop, perm_bound)
inp_dag       = permstruct.dag.classic_avoiders_length_3(perm_prop, perm_bound)
# inp_dag       = permstruct.dag.len_3_pairs(perm_prop, perm_bound)
max_rule_size = (4, 4)
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
