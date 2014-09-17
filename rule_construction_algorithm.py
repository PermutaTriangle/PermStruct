
from permstruct.lib import Permutation, Permutations, flatten, binary_search, choose, exact_cover
from permstruct import I, P, empty, generate_all_of_length
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

incr = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})



max_len = 6
n_range = (2, 3) # number of rows (min, max)
m_range = (2, 3) # numbor of columns (min, max)
max_nonempty = 4

# permProp = lambda perm: perm.avoids([1,2])
# permProp = lambda perm: perm.avoids([2,3,1])
# permProp = lambda perm: perm.avoids([1,4,2,3])
permProp  = lambda perm : perm.avoids([2,3,1]) and perm.avoids([1,2,3])
# permProp = avoids_312_vinc
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



inputs = [
    (permProp, I),
    (lambda perm: len(perm) == 1, P),
    (lambda perm: perm == Permutation(sorted(perm)), incr),
    (lambda perm: perm == Permutation(sorted(perm)[::-1]), decr),
    (lambda perm: len(perm) >= 1 and perm == Permutation(sorted(perm)), incr_nonempty),
    (lambda perm: len(perm) >= 1 and perm == Permutation(sorted(perm)[::-1]), decr_nonempty),
    # (permProp, I),
    # (lambda perm: len(perm) == 1, P),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)), incr),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)[::-1]), decr),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)), incr_nonempty),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)[::-1]), decr_nonempty),
]

# inputs += avoiders_len_3

def construct_rule(B, max_cnt, permProp, ignore_first=0, allow_overlap_in_first=False):

    validcnt = 0
    ball = 0
    permset = [ [] for _ in range(B+1) ]
    ocreated = {}
    for l in range(B+1):
        ocreated.setdefault(l, [])
        for perm in Permutations(l):
            if permProp(perm):
                permset[l].append(tuple(perm))
                ocreated[l].append(perm)
                ball |= 1 << validcnt
                validcnt += 1

    # pick the main permutation to work with, currently just chooses one of the
    # largest ones randomly
    main_perms = list(permset[B])
    random.shuffle(main_perms)
    main_perms = main_perms[:10] # TODO: do something
    # main_perms = main_perms[:20] # TODO: do something
    # print(len(main_perms))

    ok_rules = {}
    tried_rules = set()
    for n in range(n_range[0], n_range[1] + 1):
        for m in range(m_range[0], m_range[1] + 1):
            for xsep in choose(B - 1, n - 1):
                for ysep in choose(B - 1, m - 1):
                    for main_perm in main_perms:

                        arr = [ [ [] for j in range(m) ] for i in range(n) ]

                        nonempty_cnt = 0
                        ok = True
                        for i in range(n):
                            for j in range(m):
                                for k in range(0 if j == 0 else ysep[j-1] + 1, (B - 1 if j == m - 1 else ysep[j]) + 1):
                                    if (0 if i == 0 else xsep[i-1] + 1) <= B - main_perm[k] <= (B - 1 if i == n - 1 else xsep[i]):
                                        arr[i][j].append(main_perm[k])

                                if arr[i][j]:
                                    nonempty_cnt += 1
                                    if nonempty_cnt > max_nonempty:
                                        ok = False
                                        break

                            if not ok:
                                break

                        if not ok:
                            continue

                        nonempty = []
                        for i in range(n):
                            for j in range(m):
                                if arr[i][j]:
                                    arr[i][j] = Permutation.to_standard(arr[i][j])
                                    cur = []
                                    for inp_prop, inp in inputs:
                                        if inp_prop(arr[i][j]):
                                            cur.append((i, j, inp))

                                    nonempty.append(cur)

                        for poss in product(*nonempty):
                            rule = GeneratingRule({ (i,j): inp for i, j, inp in poss })
                            if rule in tried_rules:
                                continue

                            tried_rules.add(rule)

                            bs = 0
                            ok = True
                            curcnt = 0
                            for l in range(B+1):
                                curlevel = []
                                for perm in rule.generate_of_length(l, ocreated):
                                    # if not permProp(perm):
                                    if not binary_search(permset[l], perm):
                                        ok = False
                                        # print('Generated something not in the set (%s)' % str(perm))
                                        break

                                    curlevel.append(perm)

                                if not ok:
                                    break

                                cur = sorted(curlevel)
                                for a,b in zip(cur, cur[1:]):
                                    if a == b:
                                        ok = False
                                        # print('Generated something more than once (%s)' % str(a))
                                        break

                                if not ok:
                                    break

                                i = 0
                                j = 0
                                while i < len(cur) and j < len(permset[l]):
                                    if permset[l][j] < cur[i]:
                                        j += 1
                                        curcnt += 1
                                    elif cur[i] == permset[l][j]:
                                        bs |= 1 << curcnt
                                        i += 1
                                        j += 1
                                        curcnt += 1
                                    else:
                                        assert False

                                assert i == len(cur)
                                curcnt += len(permset[l]) - j

                            if ok:
                                print(rule)
                                print(''.join( '0' if (bs & (1 << i)) == 0 else '1' for i in range(validcnt - 1, -1, -1) ))
                                print('')

                                ok_rules.setdefault(bs, [])
                                ok_rules[bs].append(rule)

    print('Finding exact cover...')

    bss = list(ok_rules.keys())

    used_idx = set()
    print('Found:')
    for res in exact_cover(bss, validcnt, max_cnt, ignore_first, allow_overlap_in_first):
        print(', '.join(map(str, res)))
        used_idx |= set(res)

    print('')
    print('Index:')
    for i, b in enumerate(bss):
        if i not in used_idx:
            continue

        print('%3d: ' % i)
        print(''.join( '0' if (b & (1 << i)) == 0 else '1' for i in range(validcnt - 1, -1, -1) ))


        for rule in ok_rules[b]:
            print('')
            print(rule)

        print('')

    return []


res = construct_rule(max_len, 4, permProp, 1)
# print('res:')

# for rule in res:
#     print(rule)
#     print('')

