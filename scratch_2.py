
from permstruct.lib import Permutation, Permutations, flatten, binary_search, choose, exact_cover
from permstruct import X, P, N, empty, generate_all_of_length, construct_rule
from permstruct.permutation_sets import SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from itertools import product
import random, sys
from copy import deepcopy

def avoids_312_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[j] < perm[k] < perm[i]:
                return False
    return True

def avoids_231_vinc(perm):
    for i in range(len(perm)):
        j = i + 1
        for k in range(j+1, len(perm)):
            if perm[k] < perm[i] < perm[j]:
                return False
    return True


def avoids_123_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[i] < perm[j] < perm[k]:
                return False
    return True


def avoids_312_covinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            for k in range(j+1, len(perm)):
                if perm[j] < perm[k] < perm[i] and perm[i] == 1 + perm[k]:
                    return False
    return True


def avoids_132_covinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            for k in range(j+1, len(perm)):
                if perm[i] < perm[k] < perm[j] and perm[j] == 1 + perm[k]:
                    return False
    return True

def avoids_231_bivinc(perm):
    for i in range(0, len(perm)):
        j = i + 1
        for k in range(j+1, len(perm)):
            if perm[k] < perm[j] and perm[i] == 1 + perm[k]:
                return False
    return True

# for l in range(1, 8):
#     cnt = 0
#     for p in Permutations(l):
#         if avoids_231_vinc(p) and p.avoids([1,2,3]):
#             cnt += 1
#             # print(p)
#     print(l, cnt)
# 
# import sys
# sys.exit(0)



avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append((lambda perm: perm.avoids(p),StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 6, description='Av(%s)' % str(p))))
    # avoiders_len_3.append((lambda perm: len(perm) >= 3 and perm.avoids(p),StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 6, description='Av(%s)' % str(p))))

incr = SimpleGeneratingRule(Permutation([1,2]), [X, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [X, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [X, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [X, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})



max_len = 6
n_range = (2, 3) # number of rows (min, max)
m_range = (2, 3) # numbor of columns (min, max)
max_nonempty = 4
max_ec_cnt = 4

# permProp = lambda perm: perm.avoids([1,2])
permProp = lambda perm: perm.avoids([2,3,1])
# permProp = lambda perm: perm.avoids([1,4,2,3])
# permProp = lambda perm: perm.avoids([1,3,4,2])
# permProp  = lambda perm : perm.avoids([2,3,1]) and perm.avoids([1,2,3])
# permProp = avoids_312_vinc
# permProp = avoids_123_vinc
# permProp = avoids_231_bivinc
# permProp = lambda p: avoids_231_vinc(p) and p.avoids([1,2,3])
# permProp = lambda p: avoids_123_vinc(p) and avoids_312_covinc(p)
# permProp = lambda p: avoids_132_covinc(p) and avoids_123_vinc(p)

# for l in range(1, 10):
#     cnt = 0
#     for p in Permutations(l):
#         if permProp(p):
#             cnt += 1
#     print(cnt)
# 
# import sys
# sys.exit(0)



# Cute example
# G = GeneratingRule([
#     [N, N, P],
#     [X, P, N],
# ])


# G = GeneratingRule([
#     [N,P,N],
#     [N,P,N],
#     [X,N,decr],
# ])

# G = GeneratingRule([
#     [N,P,N],
#     [N,P,N],
#     [X,N,decr],
# ])

G = GeneratingRule([
    [decr,N,decr],
    [N,P,N],
])

# +-+-+-+-+
# |1|1|2|1|
# +-+-+-+-+
# |1|o|1|1|
# +-+-+-+-+
# |1|1|o|1|
# +-+-+-+-+
# |1|1|1|X|
# +-+-+-+-+
# 1: empty permutation
# 2: Av([2, 1, 3])
# 1 1 1 3 9 31 111 409

# # res = generate_all_of_length(10, G, {0:[()], 1:[(1,)]}, 2)
# res = generate_all_of_length(10, G, {0:[()]}, 2)
# # print(res)
# for l in res:
#     # print(res)
#     print(len(res[l]))
# 
# import sys
# sys.exit(0)


inputs = [
    (permProp, X),
    (lambda perm: len(perm) == 1, P),
    (lambda perm: perm == Permutation(sorted(perm)), incr),
    (lambda perm: perm == Permutation(sorted(perm)[::-1]), decr),
    (lambda perm: len(perm) >= 1 and perm == Permutation(sorted(perm)), incr_nonempty),
    (lambda perm: len(perm) >= 1 and perm == Permutation(sorted(perm)[::-1]), decr_nonempty),
]

# inputs += avoiders_len_3



construct_rule(permProp,
               max_len,
               n_range,
               m_range,
               max_nonempty,
               max_ec_cnt,
               inputs,
               ignore_first=1,
               allow_overlap_in_first=True)


