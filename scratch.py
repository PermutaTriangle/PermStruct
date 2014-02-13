
from sage.combinat.permutation import Permutation, Permutations
from permutation_sets import Point, Input, SimpleGeneratingRule, GeneratingRule, StaticPermutationSet

def generate_all_of_length(max_n, S, inp):

    inp = dict(inp)

    for n in range(max_n+1):
        for perm in S.generate_of_length(n, inp):
            inp.setdefault(n, [])
            inp[n].append(perm)

    return inp


def generate_rules(n, m, sets):

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

                for set in sets:
                    rule[i][j] = set
                    yield rule

    a, b = 0, 0
    for rule in gen(0, 0):
        a += 1
        if valid(rule):
            b += 1
            yield GeneratingRule(rule)

    print(a, b)


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


# Shorthands, maybe include this in the library?
I = Input()
P = Point()
empty = {0:[Permutation([])]}

# Increasing permutations
incr = SimpleGeneratingRule(Permutation([1,2]), [I, P])

# Decreasing permutations
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P])

avoids_132 = StaticPermutationSet.from_predicate(lambda x: x.avoids([1,3,2]), 6, None)

# Avoiders of 231 and 312
avoid_231_312 = SimpleGeneratingRule(Permutation([1,3,2]), [I, P, decr.to_static(10, empty)])

avoid_231_312_G = GeneratingRule([
    [None, P, None],
    [None, None, decr.to_static(10, empty)],
    [I, None, None],
])

avoid_vinc_3_12_ = GeneratingRule([
    [None, P, None],
    [I, None, decr.to_static(10,empty)]
])


# print(generate_all_of_length(6, incr, empty))
# print(generate_all_of_length(6, decr, empty))
# print(generate_all_of_length(5, avoid_231_312, empty))

res = generate_all_of_length(10, avoid_231_312, empty)
for i in range(1, 11):
    assert len(res[i]) == 2**(i-1)


# permProp = lambda perm: perm == sorted(perm)
# permCount = lambda n: 1

# def permProp(perm):
#     if len(perm) < 3:
#         return True
# 
#     for occ in perm.pattern_positions([3,1,2]):
#         if occ[1] + 1 == occ[2]:
#             return False
# 
#     return True

# permProp  = (lambda perm : perm.avoids([2,3,1]))
# permProp  = (lambda perm : perm.avoids([2,3,1]))
# permProp  = (lambda perm : perm.avoids([1,2,3]) and perm.avoids([1,3,2]))
# permProp  = (lambda perm : perm.avoids([1,3,2,4]))
permProp  = (lambda perm : perm.avoids([1,3,2,4]))
permCount = (lambda n : len(filter(lambda x : permProp(x), Permutations(n))) )

incr = incr.to_static(8, empty)
decr = decr.to_static(8, empty)
# avoids_132 = avoids_132.to_static(8, empty)


# for n in range(1, 4+1):
#     for m in range(1, 4+1):

def main():
    n = 4
    m = 2

    rulecnt = 0
    rules = generate_rules(n, m, [ I, P, None, avoids_132, decr ])
    for rule in rules:
        ok = True
        for y in range(m):
            if sum( rule.rule.get((x,y), None) is not None for x in range(n) ) > 1:
                ok = False
                break

        if not ok:
            continue

        rulecnt += 1

        if matches_rule(rule, [Permutation([])], 5, permProp, permCount):
            print(rule.rule)

    print(n, m, rulecnt)

if __name__ == '__main__':
    main()

