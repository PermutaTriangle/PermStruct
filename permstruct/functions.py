
from .permutation_sets import PointPermutationSet, InputPermutationSet, SimpleGeneratingRule, GeneratingRule, OverlayGeneratingRule, StaticPermutationSet, UniversePermutationSet, EmptyPermutationSet
from permuta import Permutation, Permutations
from permuta.misc import binary_search, TrieMap, ProgressBar
from permuta.math import signum
from copy import deepcopy
from .misc.cache import Cache
import sys
import time

class RuleDeath:
    PERM_PROP = 0
    OVERLAP = 1
    ALIVE = 2

def verify_cover(settings, rules):

    check_from = settings.perm_bound+1
    check_to = settings.verify_bound

    while True:
        for l in range(check_from, check_to+1):
            curinp = settings.sinput.get_permutations(upto=l)
            found = set()
            for rule in rules:
                for p in rule.generate_of_length(l, curinp):
                    if p in found:
                        settings.logger.log('Overlap: %s' % repr(p))
                        settings.logger.log('\n%s' % rule)
                        return RuleDeath.OVERLAP
                    if not settings.sinput.contains(p):
                        settings.logger.log('Perm prop: %s' % repr(p))
                        settings.logger.log('\n%s' % rule)
                        return RuleDeath.PERM_PROP
                    found.add(p)
            if len(found) != settings.sinput.count_of_length(l):
                settings.logger.log('Perm prop: not everything generated in length %d' % l)
                return RuleDeath.PERM_PROP
        settings.logger.log('Cover verified up to length %d' % check_to)
        check_from = check_to + 1
        if settings.ask_verify_higher:
            sys.stdout.write("Next verify_bound (or 0 to stop): ")
            check_to = int(sys.stdin.readline().strip())
        if check_from > check_to:
            break
    return RuleDeath.ALIVE

def generate_all_of_length(max_n, S, inp, min_n=0):

    inp = deepcopy(inp)

    for n in range(min_n,max_n+1):
        inp.setdefault(n, [])
        for perm in S.generate_of_length(n, inp):
            inp[n].append(perm)

    return inp

def _find_allowed_neighbors(settings, is_ok):
    neighb = {}
    for i in range(len(settings.sets)):
        for j in range(i, len(settings.sets)):
            grid = [ [ True ]*3 for _ in range(3) ]
            grid[1][1] = False
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if not grid[di+1][dj+1]:
                        continue

                    neighb.setdefault((settings.sets[i], di, dj), set())
                    neighb.setdefault((settings.sets[j], -di, -dj), set())

                    a = min(0, di)
                    b = min(0, dj)
                    G = GeneratingRule({ (-a, -b): settings.sets[i], (di-a, dj-b): settings.sets[j] })

                    if not is_ok(G):
                        grid[di+1][dj+1] = False
                        if (di+dj)%2 == 0:
                            grid[1][dj+1] = False
                            grid[di+1][1] = False
                    else:
                        neighb[(settings.sets[i], di, dj)].add(settings.sets[j])
                        neighb[(settings.sets[j], -di, -dj)].add(settings.sets[i])
    return neighb

def find_allowed_neighbors_classical_perm_prop(settings):

    # Finding the length of the longest pattern in the basis
    mx = 0
    for p in settings.sinput.avoidance:
        mx = max(mx, len(p))

    def is_ok(G):
        for l in range(mx+1):
            for perm in G.generate_of_length(l, settings.sinput.permutations):
                perm = Permutation(list(perm))
                if not settings.sinput.contains(perm):
                    return False
        return True
    return _find_allowed_neighbors(settings, is_ok)

def find_allowed_neighbors(settings):
    def is_ok(G):
        for l in range(settings.perm_bound+1):
            perms = list(G.generate_of_length(l, settings.sinput.permutations))
            if len(perms) != len(set(perms)):
                return False
        return True
    return _find_allowed_neighbors(settings, is_ok)

def populate_rule_set(settings, rule_set):
    assert settings.sinput.is_classical

    # settings.logger.log('Generate allowed neighbors, overlap')
    # allowed_neighbors = find_allowed_neighbors(settings)

    settings.logger.log('Generate allowed neighbors, perm prop')
    allowed_neighbors_cpp = find_allowed_neighbors_classical_perm_prop(settings)

    ssets = set(settings.sets)
    n = settings.max_rule_size[0]
    m = settings.max_rule_size[1]

    for s in ssets:
        if type(s) is PointPermutationSet:
            pps = s
            break

    def generates_subset(rule):
        for l in range(settings.perm_bound+1):
            for p in rule.generate_of_length(l, settings.sinput.permutations):
                if not settings.sinput.contains(p):
                    return False
        return True

    # Special case: the empty rule
    rule_set.add_rule(GeneratingRule({ (0,0): None }))

    settings.logger.log('Generating point rules')
    valid = TrieMap()
    cur = [ [ [ None for j in range(m) ] for i in range(n) ] ]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            settings.logger.log('Cell (%d,%d)' % (i,j))
            ProgressBar.create(len(cur))
            nxt = []
            for rule in cur:
                ProgressBar.progress()

                left = settings.max_non_empty - sum( rule[x][y] is not None for x in range(n) for y in range(m) )
                at_most = settings.mn_at_most - sum( 0 if rule[x][y] is None else rule[x][y].min_length(settings.sinput.permutations) for x in range(n) for y in range(m) )

                ss = set([ None, pps ])
                for s in ss:
                    if s is not None:
                        if left == 0 or s.min_length(settings.sinput.permutations) > at_most:
                            continue
                    rule[i][j] = s

                    if j == 0:
                        found = False
                        for y in range(m):
                            if rule[i][y] is not None:
                                found = True
                                break
                        if not found:
                            continue

                    if rule[i][j] is not None and not generates_subset(GeneratingRule(rule)):
                        continue

                    is_done = True
                    for x in range(i,n):
                        for y in range(j):
                            if rule[x][y] is not None:
                                is_done = False
                                break
                        if not is_done:
                            break

                    if is_done:
                        for y in range(j,m):
                            found = False
                            for x in range(i,n):
                                if rule[x][y] is not None:
                                    found = True
                                    break
                            if not found:
                                is_done = False
                                break

                    if is_done and any( rule[i][y] is not None for y in range(j,m) ):
                        key = [ (x,y) for x in range(n-1,-1,-1) for y in range(m-1,-1,-1) if rule[x][y] is not None ]
                        valid[key] = True

                    nxt.append([ [ rule[x][y] for y in range(m) ] for x in range(n) ])
            cur = nxt
            ProgressBar.finish()

    settings.logger.log('Number of point grids: %d' % len(valid))
    settings.logger.log('Generating rules, %d iterations' % valid.height())
    cur = [ ([ [ None for j in range(m) ] for i in range(n) ], valid.root) ]
    it = 1
    while cur:
        settings.logger.log('Iteration %d' % it)
        it += 1
        ProgressBar.create(len(cur))
        nxt = []
        for (tmp,node) in cur:
            ProgressBar.progress()
            for ((i,j),node2) in node.down.items():
                rule = [ [ tmp[x][y] for y in range(m) ] for x in range(n) ]

                ss = set(ssets)
                ss.remove(None)

                for ci in range(i,n):
                    for cj in range(m):
                        if (ci, cj) > (i, j):
                            di = signum(ci-i)
                            dj = signum(cj-j)
                            ss &= allowed_neighbors_cpp[(rule[ci][cj], -di, -dj)]
                            if not ss:
                                break
                    if not ss:
                        break
                if not ss:
                    continue

                must_be_point = False
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ci, cj = i+di, j+dj
                        if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
                            if rule[ci][cj] is not None and type(rule[ci][cj]) is not PointPermutationSet:
                                must_be_point = True
                                break
                    if must_be_point:
                        break

                if must_be_point:
                    ss &= set([ pps ])
                if not ss:
                    continue

                at_most = settings.mn_at_most - sum( 0 if rule[x][y] is None else rule[x][y].min_length(settings.sinput.permutations) for x in range(n) for y in range(m) )

                # TODO: if i == 0 and column j is empty, then ss.remove(None)

                for s in ss:
                    if s.min_length(settings.sinput.permutations) > at_most:
                        continue
                    rule[i][j] = s

                    if node2.end:
                        si = i
                        sj = None
                        for y in range(m):
                            found = False
                            for x in range(si,n):
                                if rule[x][y] is not None:
                                    found = True
                                    break
                            if found:
                                sj = y
                                break
                        assert sj is not None
                        g = GeneratingRule({ (x-si,y-sj): rule[x][y] for x in range(si,n) for y in range(sj,m) })
                        ok = True
                        if (si,sj) == (n-1,m-1) and not rule[si][sj].can_be_alone():
                            ok = False
                        if ok:
                            if rule_set.add_rule(g) == RuleDeath.PERM_PROP:
                                continue
                    elif settings.filter_rule_incrementally and not generates_subset(GeneratingRule(rule)):
                        continue

                    nxt.append(([ [ rule[x][y] for y in range(m) ] for x in range(n) ], node2))
        cur = nxt
        ProgressBar.finish()


X = InputPermutationSet()
P = PointPermutationSet()
S = UniversePermutationSet()
E = EmptyPermutationSet()
N = None
empty = { 0: [()] }
