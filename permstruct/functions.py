
from permutation_sets import PointPermutationSet, InputPermutationSet, SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from lib import Permutation, Permutations, binary_search
from copy import deepcopy

def generate_all_of_length(max_n, S, inp):

    inp = deepcopy(inp)

    for n in range(max_n+1):
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


def generate_rules(n, m, sets, cnt):

    def valid(rule):
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

                for set in sets:
                    if left == 0 and set is not None:
                        continue

                    rule[i][j] = set
                    yield rule

    a, b = 0, 0
    for rule in gen(0, 0):
        a += 1
        if valid(rule):
            b += 1
            yield GeneratingRule(rule)

    # print(a, b)


def generate_rules_upto(n, m, sets, cnt):
    for nn in range(1, n+1):
        for mm in range(1, m+1):
            for res in generate_rules(nn, mm, sets, cnt):
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


def find_multiple_rules(rules, B, max_cnt, permProp):

    ball = 0
    permset = [ [] for _ in range(B+1) ]
    ocreated = {}
    for n in range(B+1):
        ocreated.setdefault(n, [])
        for perm in Permutations(n):
            if permProp(perm):
                permset[n].append(tuple(perm))
                ocreated[n].append(perm)

                if n > 0:
                    ball <<= 1
                    ball |= 1

    okrules = []
    for rule in rules:

        created = deepcopy(ocreated)

        bs = 0
        ok = True
        for n in range(1, B+1):
            curlevel = []
            for perm in rule.generate_of_length(n, created):
                # if not permProp(perm):
                if not binary_search(permset[n], perm):
                    ok = False
                    # print('Generated something not in the set')
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
                bs <<= 1
                if permset[n][j] < cur[i]:
                    j += 1
                elif cur[i] == permset[n][j]:
                    bs |= 1
                    i += 1
                    j += 1
                else:
                    assert False

            assert i == len(cur)

            while j < len(permset[n]):
                bs <<= 1
                j += 1

        if ok:
            # print(rule.rule, bs)
            print(rule)
            print(bin(bs))
            print('')

            okrules.append((rule, bs))


    print('Number of ok rules: %d' % len(okrules))

    curcover = []
    def set_cover(at, left, done):
        if done == ball:
            yield list(curcover)
        elif not (left == 0 or at == len(okrules)):
            if (okrules[at][1] & done) == 0:
                curcover.append(okrules[at])
                for res in set_cover(at + 1, left - 1, done | okrules[at][1]):
                    yield res

                curcover.pop()

            for res in set_cover(at + 1, left, done):
                yield res

    return set_cover(0, max_cnt, 0)


I = InputPermutationSet()
P = PointPermutationSet()
N = None
empty = { 0: [()] }

