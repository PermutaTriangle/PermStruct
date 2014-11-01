import permstruct
import permstruct.dag

# perm_prop = lambda p: p.avoids([1])
# perm_prop = lambda p: p.avoids([1,2]) and p.avoids([2,1])
# perm_prop = lambda p: p.avoids([1,2])
perm_prop = lambda p: p.avoids([2,3,1])
# perm_prop = lambda p: p.avoids([1,2,3])

#------------------------------------------------#

# The following classical patterns of length 4 are broken down
# by Wilf-classes

# perm_prop = lambda p: p.avoids([1,3,4,2])
# perm_prop = lambda p: p.avoids([2,4,1,3])

# perm_prop = lambda p: p.avoids([1,2,3,4])
# perm_prop = lambda p: p.avoids([1,2,4,3])
# perm_prop = lambda p: p.avoids([1,4,3,2])
# perm_prop = lambda p: p.avoids([2,1,4,3])

# perm_prop = lambda p: p.avoids([1,3,2,4])

#------------------------------------------------#

# Pairs of classical patterns of length 3

# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([3,2,1])
# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([2,3,1])
# perm_prop = lambda p: p.avoids([1,2,3]) and p.avoids([1,3,2])

#------------------------------------------------#

perm_bound = 6

# dag = permstruct.dag.elementary(perm_prop, perm_bound)
dag = permstruct.dag.decr_dag(perm_prop, perm_bound)

max_rule_size = (3, 3)
max_non_empty = 3
max_rules     = 1

# For exhaustive_with_overlays
overlay_dag = permstruct.dag.x_dag(perm_prop, perm_bound)
max_overlay_cnt = 1
max_overlay_size = (1, 3)

overlays = False

if not overlays:
    permstruct.exhaustive(perm_prop,
                          perm_bound,
                          dag,
                          max_rule_size,
                          max_non_empty,
                          max_rules)

else:
    permstruct.exhaustive_with_overlays(perm_prop,
                                        perm_bound,
                                        dag,
                                        max_rule_size,
                                        max_non_empty,
                                        max_rules,
                                        overlay_dag,
                                        max_overlay_cnt,
                                        max_overlay_size,
                                        min_rule_size=(1,1))

