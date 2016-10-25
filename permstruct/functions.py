
from .permutation_sets import PointPermutationSet, InputPermutationSet, SimpleGeneratingRule, GeneratingRule, OverlayGeneratingRule, StaticPermutationSet, UniversePermutationSet, EmptyPermutationSet
from permuta import Permutation, Permutations
from permuta.misc import binary_search, TrieMap, ProgressBar
from permuta.misc.triemap import TrieNode
from permuta.math import signum
from copy import deepcopy
from .misc.cache import Cache
from functools import reduce
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

def populate_rule_set_old(settings, rule_set):
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


# XXX: toggle the comments on the following three lines to switch to the old implementation
# populate_rule_set = populate_rule_set_old
# def populate_rule_set2(settings, rule_set):
def populate_rule_set(settings, rule_set):
    assert settings.sinput.is_classical

    # print('meow')
    # populate_rule_set_old(settings, rule_set)
    # print('moo')

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
                        key = [ (x,y,pps) for x in range(n-1,-1,-1) for y in range(m-1,-1,-1) if rule[x][y] is not None ]
                        valid[key] = True


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
                            assert rule_set.add_rule(g) != RuleDeath.PERM_PROP

                    nxt.append([ [ rule[x][y] for y in range(m) ] for x in range(n) ])
            cur = nxt
            ProgressBar.finish()

    # def dfs(cur,d):
    #     print(cur.end)
    #     for (k,nxt) in cur.down.items():
    #         print(' '*d + '%s' % repr(k))
    #         dfs(nxt, d+1)
    # dfs(valid.root,0)

    def disp(cur, elems):
        if cur.end:
            print(GeneratingRule({ k:v for (k,v) in elems }))
            print('')
        for (k,v) in sorted(cur.down.items(),key=lambda x:(x[0][0],x[0][1]))[::-1]:
            disp(v, elems | set([ ((k[0],k[1]), k[2]) ]))
    # disp(valid.root, set([]))

    dag = settings.dag.get_transitive_reduction()
    for s in dag.get_topological_order():
        if s is None or type(s) is PointPermutationSet:
            continue
        # TODO: shouldn't this just be the immediate parents?
        # above = { a for a in dag.get_reachable_above(s) if a is not None and a != s }
        above = { a for a in dag.get_parents(s) if a is not None and a != s }
        # above_directly = { a for a in dag.get_parents(s) if a is not None }
        rule = [ [ None for y in range(m) ] for x in range(n) ]

        def intersect(cur, pos):
            if settings.filter_rule_incrementally and not generates_subset(GeneratingRule(rule)):
                return None

            here = TrieNode()
            here.end = all( c.end for c in cur )
            if here.end:
                si = pos[0]
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
                    res = rule_set.add_rule(g,True)
                    if res == RuleDeath.PERM_PROP:
                        return None
                    elif res != RuleDeath.ALIVE:
                        here.end = False

            found = False
            for (i,j,s2) in reduce(lambda x,y: x&y, [ c.down.keys() for c in cur ]):
                rule[i][j] = s2

                ok = True
                if ok:
                    # make sure the current type is an allowed neighbor of all (not necessarily immediate) neighbors
                    for ci in range(i,n):
                        for cj in range(m):
                            if (ci, cj) > (i, j):
                                di = signum(ci-i)
                                dj = signum(cj-j)
                                if s2 not in allowed_neighbors_cpp[(rule[ci][cj], -di, -dj)]:
                                    ok = False
                                    break
                        if not ok:
                            break
                if ok and type(s2) is not PointPermutationSet:
                    # check if any of my immediate neighbors are neither empty nor a point
                    # in that case, we can only put a point in the current box
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ci, cj = i+di, j+dj
                            if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
                                if rule[ci][cj] is not None and type(rule[ci][cj]) is not PointPermutationSet:
                                    ok = False
                                    break
                        if not ok:
                            break

                if ok:
                    rest = intersect([ c.down[(i,j,s2)] for c in cur ], (i,j))
                    if rest is not None:
                        found = True
                        here.down[(i,j,s2)] = rest
                rule[i][j] = None

            if not found and not here.end:
                return None
            return here

        def promote(cur):
            for ((i,j,s2),nxt) in cur.down.items():
                rule[i][j] = s2
                promote(nxt)
                rule[i][j] = None
            add = {}
            for ((i,j,s2),nxt) in cur.down.items():
                rule[i][j] = s
                cur_mn = sum( 0 if rule[x][y] is None else rule[x][y].min_length(settings.sinput.permutations) for x in range(n) for y in range(m) )
                if cur_mn <= settings.mn_at_most and s2 in above and (i,j,s) not in cur.down and (i,j,s) not in add:
                    if all( (i,j,a) in cur.down for a in above ):

                        ok = True
                        if ok:
                            # make sure the current type is an allowed neighbor of all (not necessarily immediate) neighbors
                            for ci in range(i,n):
                                for cj in range(m):
                                    if (ci, cj) > (i, j):
                                        di = signum(ci-i)
                                        dj = signum(cj-j)
                                        if s not in allowed_neighbors_cpp[(rule[ci][cj], -di, -dj)]:
                                            ok = False
                                            break
                                if not ok:
                                    break
                        if ok:
                            # check if any of my immediate neighbors are neither empty nor a point
                            # in that case, we can only put a point in the current box
                            for di in range(-1, 2):
                                for dj in range(-1, 2):
                                    ci, cj = i+di, j+dj
                                    if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
                                        if rule[ci][cj] is not None and type(rule[ci][cj]) is not PointPermutationSet:
                                            ok = False
                                            break
                                if not ok:
                                    break

                        if ok:
                            add[(i,j,s)] = intersect([ cur.down[(i,j,a)] for a in above ], (i,j))

                rule[i][j] = None
            for (k,v) in add.items():
                if v is not None:
                    cur.down[k] = v

        # print(s, above)
        promote(valid.root)
        # disp(valid.root, set([]))

    # import sys
    # sys.exit(0)

    # settings.logger.log('Number of point grids: %d' % len(valid))
    # settings.logger.log('Generating rules, %d iterations' % valid.height())
    # cur = [ ([ [ None for j in range(m) ] for i in range(n) ], valid.root) ]
    # it = 1
    # while cur:
    #     settings.logger.log('Iteration %d' % it)
    #     it += 1
    #     ProgressBar.create(len(cur))
    #     nxt = []
    #     for (tmp,node) in cur:
    #         ProgressBar.progress()
    #         for ((i,j),node2) in node.down.items():
    #             rule = [ [ tmp[x][y] for y in range(m) ] for x in range(n) ]
    #
    #             ss = set(ssets)
    #             ss.remove(None)
    #
    #             for ci in range(i,n):
    #                 for cj in range(m):
    #                     if (ci, cj) > (i, j):
    #                         di = signum(ci-i)
    #                         dj = signum(cj-j)
    #                         ss &= allowed_neighbors_cpp[(rule[ci][cj], -di, -dj)]
    #                         if not ss:
    #                             break
    #                 if not ss:
    #                     break
    #             if not ss:
    #                 continue
    #
    #             must_be_point = False
    #             for di in range(-1, 2):
    #                 for dj in range(-1, 2):
    #                     ci, cj = i+di, j+dj
    #                     if (ci, cj) > (i, j) and 0 <= ci < n and 0 <= cj < m:
    #                         if rule[ci][cj] is not None and type(rule[ci][cj]) is not PointPermutationSet:
    #                             must_be_point = True
    #                             break
    #                 if must_be_point:
    #                     break
    #
    #             if must_be_point:
    #                 ss &= set([ pps ])
    #             if not ss:
    #                 continue
    #
    #             at_most = settings.mn_at_most - sum( 0 if rule[x][y] is None else rule[x][y].min_length(settings.sinput.permutations) for x in range(n) for y in range(m) )
    #
    #             # TODO: if i == 0 and column j is empty, then ss.remove(None)
    #
    #             for s in ss:
    #                 if s.min_length(settings.sinput.permutations) > at_most:
    #                     continue
    #                 rule[i][j] = s
    #
    #                 if node2.end:
    #                     si = i
    #                     sj = None
    #                     for y in range(m):
    #                         found = False
    #                         for x in range(si,n):
    #                             if rule[x][y] is not None:
    #                                 found = True
    #                                 break
    #                         if found:
    #                             sj = y
    #                             break
    #                     assert sj is not None
    #                     g = GeneratingRule({ (x-si,y-sj): rule[x][y] for x in range(si,n) for y in range(sj,m) })
    #                     ok = True
    #                     if (si,sj) == (n-1,m-1) and not rule[si][sj].can_be_alone():
    #                         ok = False
    #                     if ok:
    #                         if rule_set.add_rule(g) == RuleDeath.PERM_PROP:
    #                             continue
    #                 elif settings.filter_rule_incrementally and not generates_subset(GeneratingRule(rule)):
    #                     continue
    #
    #                 nxt.append(([ [ rule[x][y] for y in range(m) ] for x in range(n) ], node2))
    #     cur = nxt
    #     ProgressBar.finish()


X = InputPermutationSet()
P = PointPermutationSet()
S = UniversePermutationSet()
E = EmptyPermutationSet()
N = None
empty = { 0: [()] }
