from permstruct.lib import ordered_set_partitions, flatten
from permstruct.permutation_sets import PermutationSet, StaticPermutationSet, PointPermutationSet, InputPermutationSet

from permstruct import X, N, P, empty, generate_all_of_length
from permstruct.lib import Permutation, Permutations
from permstruct.permutation_sets import SimpleGeneratingRule, OverlayGeneratingRule

from itertools import product
from copy import deepcopy


incr = SimpleGeneratingRule(Permutation([1,2]), [X, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [X, P], description='decreasing').to_static(8, empty)

def at_most_one_descent(p):
    found = False
    for i in range(1, len(p)):
        if p[i-1] > p[i]:
            if found:
                return False
            found = True
    return True

av123 = set([ tuple(p) for l in range(8) for p in Permutations(l) if p.avoids([1,2,3]) ])
# print(sorted(av123))


# +-+-+-+
# | |o| |
# +-+-+-+
# |X| |1|
# +-+-+-+
# 1: decreasing
# set([(0, 1), (1, 1)]), <function <lambda> at 0x7fd1f7d8f938>
# 0b111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110

# G = OverlayGeneratingRule([
#         [N, P, N],
#         [X, N, decr]
#     ],
#     [ (set([(0,1), (1,1)]), lambda p: p.avoids([1,2,3])) ]
# )

# G = OverlayGeneratingRule([
#         [N, P, N],
#         [X, N, X]
#     ],
#     []
# )
# 

# print(G)

G = OverlayGeneratingRule([
        [X, N, decr],
        [N, P, N]
    ],
    [ (set([(0,0), (0,1), (0,2)]), lambda p: p.avoids([1,2,3])) ]
)

# print(generate_all_of_length(6, G, empty))
for l, perms in sorted(generate_all_of_length(6, G, empty).items()):
    # print(l, perms)
    # print(sorted(perms))
    print(l, len(perms))
    assert len(perms) == len(set(perms))
    # print(perms)
    for perm in perms:
        assert Permutation(perm).avoids([1,2,3])


