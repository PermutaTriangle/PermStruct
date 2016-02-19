
from .permutation_sets import PointPermutationSet, InputPermutationSet, SimpleGeneratingRule, GeneratingRule, OverlayGeneratingRule, StaticPermutationSet, UniversePermutationSet, EmptyPermutationSet
from permuta import Permutation, Permutations
from permuta.misc import binary_search
from copy import deepcopy
from .misc.cache import Cache
import marshal

# def generate_small_input(perm_prop):
#     bound = 2
#     ocreated = {}
#     for l in range(bound+1):
#         ocreated.setdefault(l, [])
#         for perm in Permutations(l):
#             if perm_prop(perm):
#                 ocreated[l].append(perm)
#     return ocreated

def generate_all_of_length(max_n, S, inp, min_n=0):

    inp = deepcopy(inp)

    for n in range(min_n,max_n+1):
        inp.setdefault(n, [])
        for perm in S.generate_of_length(n, inp):
            inp[n].append(perm)

    return inp

def find_allowed_neighbors_classical_perm_prop(settings):

    neighb = {}
    for i in range(len(settings.sets)):
        for j in range(len(settings.sets)):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue

                    neighb.setdefault((settings.sets[i], di, dj), set())

                    a = min(0, di)
                    b = min(0, dj)
                    G = GeneratingRule({ (-a, -b): settings.sets[i], (di-a, dj-b): settings.sets[j] })

                    ok = True
                    for l in range(settings.perm_bound+1):
                        for perm in G.generate_of_length(l, settings.sinput.permutations):
                            perm = Permutation(list(perm))
                            if not settings.sinput.contains(perm):
                                ok = False
                                break
                        if not ok:
                            break
                    if ok:
                        neighb[(settings.sets[i], di, dj)].add(settings.sets[j])
    return neighb


def find_allowed_neighbors(settings):
    small_bound = 2
    small_perms = [[] for i in range(len(settings.sets))]
    for l in range(small_bound+1):
        for i in range(len(settings.sets)):
            if settings.sets[i]:
                for perm in settings.sets[i].generate_of_length(l, settings.sinput.permutations):
                    small_perms[i].append(perm)
    for i in range(len(settings.sets)):
        small_perms[i] = sorted(small_perms[i])

    key = small_perms
    if not settings.ignore_cache and Cache.contains(key):
        neighb = Cache.get(key)
    else:
        neighb = {}

        for i in range(len(settings.sets)):
            for j in range(len(settings.sets)):
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == 0 and dj == 0:
                            continue

                        # neighb.setdefault((cur_elem, di, dj), set())
                        neighb.setdefault((i, di, dj), set())

                        a = min(0, di)
                        b = min(0, dj)
                        # G = GeneratingRule({ (-a, -b): cur_elem, (di-a, dj-b): other_elem })
                        G = GeneratingRule({ (-a, -b): settings.sets[i], (di-a, dj-b): settings.sets[j] })

                        ok = True
                        for l in range(settings.perm_bound+1):
                            perms = list(G.generate_of_length(l, settings.sinput.permutations))
                            if len(perms) != len(set(perms)):
                                ok = False
                                break
                        if ok:
                            # neighb[(cur_elem, di, dj)].add(other_elem)
                            neighb[(i, di, dj)].add(j)

        if not settings.ignore_cache:
            Cache.put(key,neighb)

    res = {}
    for (i,di,dj),v in neighb.items():
        res[(settings.sets[i],di,dj)] = set([ settings.sets[j] for j in v ])
    return res


# def generate_rules(settings, n, m,
#         allowed_neighbors=None,
#         use_allowed_neighbors=True,
#         allowed_neighbors_cpp=None,
#     ):
#
#     if allowed_neighbors is None and use_allowed_neighbors:
#         allowed_neighbors = find_allowed_neighbors(settings)
#     if not use_allowed_neighbors:
#         allowed_neighbors = None
#
#     if settings.sinput.is_classical and allowed_neighbors_cpp is None:
#         allowed_neighbors_cpp = find_allowed_neighbors_classical_perm_prop(settings)
#
#     # key = (n,m,perm_bound, sets, cnt, allowed_neighbors)
#     # print('a')
#     # if Cache.contains(key):
#     #     res = Cache.get(key)
#     #     print('b cache')
#     #     return res
#
#     def valid(rule):
#         if n == 1 and m == 1:
#             # edge case: all 1x1 rules are valid
#             if rule[0][0] and not rule[0][0].can_be_alone():
#                 return False
#             return True
#
#         if all( x is None for x in rule[0] ):
#             return False
#
#         for y in range(m):
#             found = False
#             for x in range(n):
#                 if rule[x][y] is not None:
#                     found = True
#                     break
#
#             if not found:
#                 return False
#
#         return True
#
#     def signum(n):
#         return 1 if n > 0 else -1 if n < 0 else 0
#
#     ssets = set(settings.sets)
#     def gen(i, j):
#         if j == m:
#             for rule in gen(i + 1, 0):
#                 if i + 1 == n or any( x is not None for x in rule[i + 1] ):
#                     yield rule
#         elif i == n:
#             yield [ [ None for y in range(m) ] for x in range(n) ]
#         else:
#             for trule in gen(i, j + 1):
#                 rule = [ [ trule[x][y] for y in range(m) ] for x in range(n) ]
#                 left = settings.max_non_empty - sum( rule[x][y] is not None for x in range(n) for y in range(m) )
#                 at_most = settings.mn_at_most - sum( 0 if rule[x][y] is None else rule[x][y].min_length(settings.sinput.permutations) for x in range(n) for y in range(m) )
#
#                 ss = set(ssets)
#                 if use_allowed_neighbors:
#                     for di in range(-1, 2):
#                         for dj in range(-1, 2):
#                             ci, cj = i+di, j+dj
#                             if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
#                                 curs = allowed_neighbors[(rule[ci][cj], -di, -dj)]
#                                 ss &= curs
#
#                 if allowed_neighbors_cpp is not None:
#                     for ci in range(i,n):
#                         for cj in range(m):
#                             if (ci, cj) > (i, j):
#                                 di = signum(ci-i)
#                                 dj = signum(cj-j)
#                                 curs = allowed_neighbors_cpp[(rule[ci][cj], -di, -dj)]
#                                 ss &= curs
#
#                 for s in ss:
#                     if s is not None:
#                         if left == 0 or s.min_length(settings.sinput.permutations) > at_most:
#                             continue
#                     rule[i][j] = s
#                     yield rule
#
#     res = []
#     a, b = 0, 0
#     for rule in gen(0, 0):
#         # if (n,m) == (3,3):
#         #     print(GeneratingRule(rule))
#         a += 1
#         if valid(rule):
#             b += 1
#             res.append(GeneratingRule(rule))
#
#     # print('b')
#     # Cache.put(key,res)
#     # print('c')
#     return res




def generate_rules(settings, n, m,
        allowed_neighbors=None,
        use_allowed_neighbors=True,
        allowed_neighbors_cpp=None,
    ):

    if allowed_neighbors is None and use_allowed_neighbors:
        allowed_neighbors = find_allowed_neighbors(settings)
    if not use_allowed_neighbors:
        allowed_neighbors = None

    if settings.sinput.is_classical and allowed_neighbors_cpp is None:
        allowed_neighbors_cpp = find_allowed_neighbors_classical_perm_prop(settings)

    # key = (n,m,perm_bound, sets, cnt, allowed_neighbors)
    # print('a')
    # if Cache.contains(key):
    #     res = Cache.get(key)
    #     print('b cache')
    #     return res

    def valid(rule):
        if n == 1 and m == 1:
            # edge case: all 1x1 rules are valid
            if rule[0][0] and not rule[0][0].can_be_alone():
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

    def generates_subset(rule):
        for l in range(settings.perm_bound+1):
            found = set()
            for p in rule.generate_of_length(l, settings.sinput.permutations):
                if p in found or not settings.sinput.contains(p):
                    return False
                found.add(p)
        return True

    def signum(n):
        return 1 if n > 0 else -1 if n < 0 else 0

    ssets = set(settings.sets)
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
                left = settings.max_non_empty - sum( rule[x][y] is not None for x in range(n) for y in range(m) )
                at_most = settings.mn_at_most - sum( 0 if rule[x][y] is None else rule[x][y].min_length(settings.sinput.permutations) for x in range(n) for y in range(m) )

                ss = set(ssets)
                if use_allowed_neighbors:
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ci, cj = i+di, j+dj
                            if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
                                curs = allowed_neighbors[(rule[ci][cj], -di, -dj)]
                                ss &= curs

                if allowed_neighbors_cpp is not None:
                    for ci in range(i,n):
                        for cj in range(m):
                            if (ci, cj) > (i, j):
                                di = signum(ci-i)
                                dj = signum(cj-j)
                                curs = allowed_neighbors_cpp[(rule[ci][cj], -di, -dj)]
                                ss &= curs

                for s in ss:
                    if s is not None:
                        if left == 0 or s.min_length(settings.sinput.permutations) > at_most:
                            continue
                    rule[i][j] = s
                    # if generates_subset(GeneratingRule(rule)):
                    yield rule

    res = []
    a, b = 0, 0
    for rule in gen(0, 0):
        # if (n,m) == (3,3):
        #     print(GeneratingRule(rule))
        a += 1
        if valid(rule):
            b += 1
            res.append(GeneratingRule(rule))

    # print('b')
    # Cache.put(key,res)
    # print('c')
    return res




# def generate_rules_with_overlay(n, m, small_input, sets, cnt, overlay_preds, max_overlay_cnt, max_overlay_size):
#
#     def gen(rule, i, j, last, left):
#
#         if j == m:
#             for orule in gen(rule, i + 1, 0, last, left):
#                 yield orule
#         elif i == n:
#             yield OverlayGeneratingRule(dict(rule.rule), [])
#         else:
#             for orule in gen(rule, i, j + 1, (0, 0), left):
#                 yield orule
#
#             if left > 0:
#                 for h in range(1, max_overlay_size[0] + 1):
#                     for w in range(1, max_overlay_size[1] + 1):
#                         if (h, w) != (1, 1) and (h, w) > last and i+h <= n and j+w <= m:
#
#                             overlay_coords = set([ (row, col) for row in range(i, i + h) for col in range(j, j + w) ])
#
#                             for orule in gen(rule, i, j, (h, w), left - 1):
#                                 for inp in overlay_preds:
#                                     if inp is None:
#                                         continue
#
#                                     orule2 = OverlayGeneratingRule(deepcopy(orule.rule), deepcopy(orule.overlay) + [ (deepcopy(overlay_coords), inp) ])
#                                     yield orule2
#
#
#
#     for rule in generate_rules(n, m, small_input, sets, cnt, None, use_allowed_neighbors=False):
#         for overlay_rule in gen(rule, 0, 0, (0, 0), max_overlay_cnt):
#             yield overlay_rule


def generate_rules_upto(settings):

    ignore_cache = settings.ignore_cache
    if settings.sinput.is_classical:
        # Classical optimizations depend on the perm prop (and not only the
        # smallest elements), so this is probably for the best
        ignore_cache = True

    # key = (settings.min_rule_size,settings.max_rule_size,small_input,settings.sets,cnt,allowed_neighbors,use_allowed_neighbors,mn_at_most)
    # if not ignore_cache and Cache.contains(key):
    #     ans = Cache.get(key)
    # else:

    allowed_neighbors = find_allowed_neighbors(settings)

    if settings.sinput.is_classical:
        allowed_neighbors_cpp = find_allowed_neighbors_classical_perm_prop(settings)
    else:
        allowed_neighbors_cpp = None

    rev = { v:i for i,v in enumerate(settings.sets) }
    ans = []
    for nn in range(settings.min_rule_size[0], settings.max_rule_size[0]+1):
        for mm in range(settings.min_rule_size[1], settings.max_rule_size[1]+1):
            settings.logger.log('Generating rules of size (%d,%d)' % (nn,mm))
            for res in generate_rules(settings, nn, mm,
                    allowed_neighbors=allowed_neighbors,
                    use_allowed_neighbors=True,
                    allowed_neighbors_cpp=allowed_neighbors_cpp):
                ans.append({ (x,y):rev[v] for (x,y),v in res.rule.items() })

    # if not ignore_cache:
    #     Cache.put(key,ans)

    for i in range(len(ans)):
        ans[i] = GeneratingRule({ (x,y):settings.sets[v] for (x,y),v in ans[i].items() })
    return ans



# def generate_rules_upto(settings):
#     allowed_neighbors = find_allowed_neighbors(settings)
#     if settings.sinput.is_classical:
#         allowed_neighbors_cpp = find_allowed_neighbors_classical_perm_prop(settings)
#     else:
#         allowed_neighbors_cpp = None
#
#     def valid(rule):
#         if n == 1 and m == 1:
#             # edge case: all 1x1 rules are valid
#             if rule[0][0] and not rule[0][0].can_be_alone():
#                 return False
#             return True
#
#         if all( x is None for x in rule[0] ):
#             return False
#
#         for y in range(m):
#             found = False
#             for x in range(n):
#                 if rule[x][y] is not None:
#                     found = True
#                     break
#
#             if not found:
#                 return False
#
#         return True
#
#     def signum(n):
#         return 1 if n > 0 else -1 if n < 0 else 0
#
#     ssets = set(settings.sets)
#     def gen(i, j):
#         if j == m:
#             for rule in gen(i + 1, 0):
#                 if i + 1 == n or any( x is not None for x in rule[i + 1] ):
#                     yield rule
#         elif i == n:
#             yield [ [ None for y in range(m) ] for x in range(n) ]
#         else:
#             for trule in gen(i, j + 1):
#                 rule = [ [ trule[x][y] for y in range(m) ] for x in range(n) ]
#                 left = settings.max_non_empty - sum( rule[x][y] is not None for x in range(n) for y in range(m) )
#                 at_most = settings.mn_at_most - sum( 0 if rule[x][y] is None else rule[x][y].min_length(settings.sinput.permutations) for x in range(n) for y in range(m) )
#
#                 ss = set(ssets)
#                 if use_allowed_neighbors:
#                     for di in range(-1, 2):
#                         for dj in range(-1, 2):
#                             ci, cj = i+di, j+dj
#                             if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
#                                 curs = allowed_neighbors[(rule[ci][cj], -di, -dj)]
#                                 ss &= curs
#
#                 if allowed_neighbors_cpp is not None:
#                     for ci in range(i,n):
#                         for cj in range(m):
#                             if (ci, cj) > (i, j):
#                                 di = signum(ci-i)
#                                 dj = signum(cj-j)
#                                 curs = allowed_neighbors_cpp[(rule[ci][cj], -di, -dj)]
#                                 ss &= curs
#
#                 for s in ss:
#                     if s is not None:
#                         if left == 0 or s.min_length(settings.sinput.permutations) > at_most:
#                             continue
#                     rule[i][j] = s
#                     yield rule
#
#     res = []
#     a, b = 0, 0
#     for rule in gen(0, 0):
#         a += 1
#         if valid(rule):
#             b += 1
#             res.append(GeneratingRule(rule))
#
#     return res



# def generate_rules_with_overlay_upto(min_rule_size, max_rule_size, small_input, sets, cnt, overlay_preds, max_overlay_cnt, max_overlay_size):
#
#     for nn in range(min_rule_size[0], max_rule_size[0]+1):
#         for mm in range(min_rule_size[1], max_rule_size[1]+1):
#             for res in generate_rules_with_overlay(nn, mm, small_input, sets, cnt, overlay_preds, max_overlay_cnt, max_overlay_size):
#                 yield res


X = InputPermutationSet()
P = PointPermutationSet()
S = UniversePermutationSet()
E = EmptyPermutationSet()
N = None
empty = { 0: [()] }

