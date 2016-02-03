
from .permutation_sets import PointPermutationSet, InputPermutationSet, SimpleGeneratingRule, GeneratingRule, OverlayGeneratingRule, StaticPermutationSet, UniversePermutationSet, EmptyPermutationSet
from permuta import Permutation, Permutations
from permuta.misc import binary_search
from copy import deepcopy
from .misc.cache import Cache
import marshal

def generate_small_input(perm_prop):
    bound = 2
    ocreated = {}
    for l in range(bound+1):
        ocreated.setdefault(l, [])
        for perm in Permutations(l):
            if perm_prop(perm):
                ocreated[l].append(perm)
    return ocreated

def generate_all_of_length(max_n, S, inp, min_n=0):

    inp = deepcopy(inp)

    for n in range(min_n,max_n+1):
        inp.setdefault(n, [])
        for perm in S.generate_of_length(n, inp):
            inp[n].append(perm)

    return inp


# TODO: Finish this optimized rule generation.
# def generate_rules_2(n, m, sets):
# 
#     assert n <= m
# 
#     used = [False] * n
# 
#     def gen(at):
# 


def find_allowed_neighbors(small_input, sets, ignore_cache=False):
    # TODO: Only hash small permutations in sets?
    key = (small_input, sets)
    if not ignore_cache and Cache.contains(key):
        neighb = Cache.get(key)
    else:
        neighb = {}
        max_check = max(small_input.keys())

        for i in range(len(sets)):
            for j in range(len(sets)):
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue

                        # neighb.setdefault((cur_elem, di, dj), set())
                        neighb.setdefault((i, di, dj), set())

                        a = min(0, di)
                        b = min(0, dj)
                        # G = GeneratingRule({ (-a, -b): cur_elem, (di-a, dj-b): other_elem })
                        G = GeneratingRule({ (-a, -b): sets[i], (di-a, dj-b): sets[j] })

                        ok = True
                        for l in range(max_check+1):
                            # perms = list(G.generate_of_length(l, ocreated))
                            perms = list(G.generate_of_length(l, small_input))
                            if len(perms) != len(set(perms)):
                                ok = False
                                break
                        if ok:
                            # neighb[(cur_elem, di, dj)].add(other_elem)
                            neighb[(i, di, dj)].add(j)

        if not ignore_cache:
            Cache.put(key,neighb)

    res = {}
    for (i,di,dj),v in neighb.items():
        res[(sets[i],di,dj)] = set([ sets[j] for j in v ])
    return res


def generate_rules(n, m, small_input, sets, cnt,
        allowed_neighbors=None,
        use_allowed_neighbors=True,
        mn_at_most=None):

    if allowed_neighbors is None and use_allowed_neighbors:
        allowed_neighbors = find_allowed_neighbors(small_input, sets)
    if not use_allowed_neighbors:
        allowed_neighbors = None

    # key = (n,m,perm_bound, sets, cnt, allowed_neighbors)
    # print('a')
    # if Cache.contains(key):
    #     res = Cache.get(key)
    #     print('b cache')
    #     return res

    def valid(rule):
        if n == 1 and m == 1:
            # edge case: all 1x1 rules are valid
            if not rule[0][0] or not rule[0][0].can_be_alone():
                return False
            return True

        if all( x is None for x in rule[0] ):
            return False

        for y in range(m):
            found = False
            for x in range(n):
                if rule[x][y] is not None:
                    found = True
                    break

            if not found:
                return False

        return True

    ssets = set(sets)
    def gen(i, j):
        if j == m:
            for rule in gen(i + 1, 0):
                if i + 1 == n or any( x is not None for x in rule[i + 1] ):
                    yield rule
        elif i == n:
            yield [ [ None for y in range(m) ] for x in range(n) ]
        else:
            for trule in gen(i, j + 1):
                rule = [ [ trule[x][y] for y in range(m) ] for x in range(n) ]
                left = cnt - sum( rule[x][y] is not None for x in range(n) for y in range(m) )
                at_most = mn_at_most - sum( 0 if rule[x][y] is None else rule[x][y].min_length(small_input) for x in range(n) for y in range(m) )

                ss = set(ssets)
                if use_allowed_neighbors:
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ci, cj = i+di, j+dj
                            if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
                                curs = allowed_neighbors[(rule[ci][cj], -di, -dj)]
                                ss &= curs

                # for s in sets:
                for s in ss:
                    if s is not None:
                        if left == 0 or s.min_length(small_input) > at_most:
                            continue
                    # if left == 0 and s is not None:
                    #     continue

                    rule[i][j] = s
                    yield rule

    res = []
    a, b = 0, 0
    for rule in gen(0, 0):
        a += 1
        if valid(rule):
            b += 1
            res.append(GeneratingRule(rule))

    # print('b')
    # Cache.put(key,res)
    # print('c')
    return res


def generate_rules_with_overlay(n, m, small_input, sets, cnt, overlay_preds, max_overlay_cnt, max_overlay_size):

    def gen(rule, i, j, last, left):

        if j == m:
            for orule in gen(rule, i + 1, 0, last, left):
                yield orule
        elif i == n:
            yield OverlayGeneratingRule(dict(rule.rule), [])
        else:
            for orule in gen(rule, i, j + 1, (0, 0), left):
                yield orule

            if left > 0:
                for h in range(1, max_overlay_size[0] + 1):
                    for w in range(1, max_overlay_size[1] + 1):
                        if (h, w) != (1, 1) and (h, w) > last and i+h <= n and j+w <= m:

                            overlay_coords = set([ (row, col) for row in range(i, i + h) for col in range(j, j + w) ])

                            for orule in gen(rule, i, j, (h, w), left - 1):
                                for inp in overlay_preds:
                                    if inp is None:
                                        continue

                                    orule2 = OverlayGeneratingRule(deepcopy(orule.rule), deepcopy(orule.overlay) + [ (deepcopy(overlay_coords), inp) ])
                                    yield orule2



    for rule in generate_rules(n, m, small_input, sets, cnt, None, use_allowed_neighbors=False):
        for overlay_rule in gen(rule, 0, 0, (0, 0), max_overlay_cnt):
            yield overlay_rule


def generate_rules_upto(min_rule_size, max_rule_size, small_input, sets, cnt,
        allowed_neighbors=None,
        use_allowed_neighbors=True,
        ignore_cache=False,
        mn_at_most=None):

    key = (min_rule_size,max_rule_size,small_input,sets,cnt,allowed_neighbors,use_allowed_neighbors,mn_at_most)
    if not ignore_cache and Cache.contains(key):
        ans = Cache.get(key)
    else:
        if allowed_neighbors is None:
            allowed_neighbors = find_allowed_neighbors(small_input, sets)

        rev = { v:i for i,v in enumerate(sets) }
        ans = []
        for nn in range(min_rule_size[0], max_rule_size[0]+1):
            for mm in range(min_rule_size[1], max_rule_size[1]+1):
                for res in generate_rules(nn, mm, small_input, sets, cnt, allowed_neighbors, use_allowed_neighbors, mn_at_most=mn_at_most):
                    ans.append({ (x,y):rev[v] for (x,y),v in res.rule.items() })
        if not ignore_cache:
            Cache.put(key,ans)
    for i in range(len(ans)):
        ans[i] = GeneratingRule({ (x,y):sets[v] for (x,y),v in ans[i].items() })
    return ans

def generate_rules_with_overlay_upto(min_rule_size, max_rule_size, small_input, sets, cnt, overlay_preds, max_overlay_cnt, max_overlay_size):

    for nn in range(min_rule_size[0], max_rule_size[0]+1):
        for mm in range(min_rule_size[1], max_rule_size[1]+1):
            for res in generate_rules_with_overlay(nn, mm, small_input, sets, cnt, overlay_preds, max_overlay_cnt, max_overlay_size):
                yield res

def matches_rule(rule, atoms, B, permProp = (lambda perm : True), permCount = (lambda n : 0)):

    created = {}

    # Putting the atoms in the dictionary by length
    for atom in atoms:
        created.setdefault(len(atom),[])
        created[len(atom)].append(atom)

    for n in range(B+1):

        # Need to be careful if there are atoms of length n
        created.setdefault(n,[])

        for perm in rule.generate_of_length(n, created):
            if not permProp(perm):
                return False

            created[n].append(perm)

        if len(set(created[n])) != len(created[n]):
            return False

        if permCount(n) != len(created[n]):
            return False

    return True

def find_multiple_rules(rules, B, max_cnt, permProp, ignore_first=0, allow_overlap_in_first=False):

    validcnt = 0
    ball = 0
    permset = [ [] for _ in range(B+1) ]
    ocreated = {}
    for n in range(B+1):
        ocreated.setdefault(n, [])
        for perm in Permutations(n):
            if permProp(perm):
                permset[n].append(tuple(perm))
                ocreated[n].append(perm)
                ball |= 1 << validcnt
                validcnt += 1

    okrules = []

    for rule in rules:

        created = deepcopy(ocreated)

        bs = 0
        ok = True
        curcnt = 0
        for n in range(B+1):
            curlevel = []
            for perm in rule.generate_of_length(n, created):

                # if not permProp(perm):
                if not binary_search(permset[n], perm):
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
            while i < len(cur) and j < len(permset[n]):
                # bs <<= 1
                if permset[n][j] < cur[i]:
                    j += 1
                    curcnt += 1
                elif cur[i] == permset[n][j]:
                    bs |= 1 << curcnt
                    # bs |= 1
                    i += 1
                    j += 1
                    curcnt += 1
                else:
                    assert False

            assert i == len(cur)

            while j < len(permset[n]):
                curcnt += 1
                # bs <<= 1
                j += 1

        if ok:
            # print(rule)
            # import sys
            # for i in range(validcnt - 1, -1, -1):
            #     if (bs & (1 << i)) == 0:
            #         sys.stdout.write('0')
            #     else:
            #         sys.stdout.write('1')

            # sys.stdout.write('\n')

            # print(bin(bs))
            # print('')

            okrules.append((rule, bs))


    # print('Number of ok rules: %d' % len(okrules))

    curcover = []
    care = ball & ~((1 << ignore_first) - 1)
    def exact_cover(at, left, done):
        if (done & care) == (ball & care):
            yield list(curcover)
        elif not (left == 0 or at == len(okrules)):
            if (okrules[at][1] & done & (care if allow_overlap_in_first else ball)) == 0:
                curcover.append(okrules[at])
                for res in exact_cover(at + 1, left - 1, done | okrules[at][1]):
                    yield res

                curcover.pop()

            for res in exact_cover(at + 1, left, done):
                yield res

    return exact_cover(0, max_cnt, 0)



X = InputPermutationSet()
P = PointPermutationSet()
S = UniversePermutationSet()
E = EmptyPermutationSet()
N = None
empty = { 0: [()] }

