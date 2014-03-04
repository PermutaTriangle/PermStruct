
# from sage.combinat.permutation import Permutation, Permutations
from permutation_sets import Point, Input, SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from copy import deepcopy


def generate_all_of_length(max_n, S, inp):

    inp = deepcopy(inp)

    for n in range(max_n+1):
        inp.setdefault(n, [])
        for perm in S.generate_of_length(n, inp):
            inp[n].append(perm)

    return inp


# TODO: Finish this opmtimized rule generation.
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


I = Input()
P = Point()
N = None
# empty = { 0: [Permutation([])] }
empty = { 0: [()] }

