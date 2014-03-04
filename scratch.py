
import bisect
from sage.combinat.permutation import Permutation, Permutations
from permutation_sets import Point, Input, SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from permstruct import generate_all_of_length, generate_rules, generate_rules_upto, matches_rule, I, P, N, empty
import sys
sys.setrecursionlimit(10**9)

# Increasing permutations
incr_gen = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing')

# Decreasing permutations
decr_gen = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing')

# avoids_132 = StaticPermutationSet.from_predicate(lambda x: x.avoids([1,3,2]), 6, N)
avoids_231 = GeneratingRule([
    [N, P, N],
    [N, N, I],
    [I, N, N],
], description='Av(231)')

avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append(StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 5, description='Av(%s)' % str(p)))

# Avoiders of 231 and 312
# avoid_231_312 = SimpleGeneratingRule(Permutation([1,3,2]), [I, P, decr_gen.to_static(10, empty)])

# avoid_231_312_G = GeneratingRule([
#     [N, P, N],
#     [N, N, decr_gen.to_static(10, empty)],
#     [I, N, N],
# ])

# avoid_vinc_3_12_ = GeneratingRule([
#     [N, P, N],
#     [I, N, decr_gen.to_static(10,empty)]
# ])


# print(generate_all_of_length(6, incr, empty))
# print(generate_all_of_length(6, decr, empty))
# print(generate_all_of_length(5, avoid_231_312, empty))

# res = generate_all_of_length(10, avoid_231_312, empty)
# for i in range(1, 11):
#     assert len(res[i]) == 2**(i-1)


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

permProp  = (lambda perm : perm.avoids([1,2,3]))
# permProp  = (lambda perm : perm.avoids([2,1]))
# permProp  = (lambda perm : perm.avoids([1,2,3]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]))
# permProp  = (lambda perm : perm.avoids([1,2,3]) and perm.avoids([2,3,1]))
# permProp  = (lambda perm : perm.avoids([1,4,2,3]) and perm.avoids([3,2,1]))
# permProp  = (lambda perm : perm.avoids([1,3,2,4]))
# permProp  = (lambda perm : perm.avoids([1,3,2,4]))
permCount = (lambda n : len(filter(lambda x : permProp(x), Permutations(n))) )

incr = incr_gen.to_static(8, empty)
incr_nonempty = incr_gen.to_static(8, {1:[Permutation([1])]}, description='increasing nonempty')
decr = decr_gen.to_static(8, empty)
decr_nonempty = decr_gen.to_static(8, {1:[Permutation([1])]}, description='decreasing nonempty')

# incr_nonempty = incr_gen.to_static(8, {1:[Permutation([1])]})
# decr_nonempty = decr_gen.to_static(8, {1:[Permutation([1])]})
# incr_nonempty = incr_gen.to_static(8, {1:[(1,)]})
# decr_nonempty = decr_gen.to_static(8, {1:[(1,)]})

# avoids_132 = avoids_132.to_static(8, empty)


# for n in range(1, 4+1):
#     for m in range(1, 4+1):


# rule = GeneratingRule([
#     [decr,N,N],
#     [N,P,N],
#     [I,N,N]
# ])

# print(list(generet))

def display_rule(rule):
    n = max( i for i,j in rule.rule )+1
    m = max( j for i,j in rule.rule )+1
    arr = [ [ ' ' for j in range(2*m+1) ] for i in range(2*n+1) ]
    labels = {}

    for i in range(2*n+1):
        for j in range(2*m+1):
            a = i % 2 == 0
            b = j % 2 == 0
            if a and b:
                arr[i][j] = '+'
            elif a:
                arr[i][j] = '-'
            elif b:
                arr[i][j] = '|'

    for i,j in rule.rule:
        if rule.rule[(i,j)] == I:
            arr[2*i+1][2*j+1] = 'I'
        elif rule.rule[(i,j)] == P:
            arr[2*i+1][2*j+1] = 'O'
        else:
            if rule.rule[(i,j)] not in labels:
                labels[rule.rule[(i,j)]] = str(len(labels) + 1)

            # arr[2*i+1][2*j+1] = 'S'
            arr[2*i+1][2*j+1] = labels[rule.rule[(i,j)]]

    for row in arr:
        print(''.join(row))

    for k, v in sorted(labels.items(), key=lambda x: x[1]):
        print('%s: %s' % (v, k.description))

def binary_search(a, x):
    i = bisect.bisect_left(a, x)
    return i != len(a) and a[i] == x

def find_multiple_rules(rules, atoms, B, max_cnt, permProp):

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

        # created = deepcopy(atoms)
        # print("Testing")
        # display_rule(rule)

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
            display_rule(rule)
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

# print('A')
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]))
permProp  = (lambda perm : Permutation(list(perm)).avoids([1,2,3]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]) and Permutation(list(perm)).avoids([1,3,2]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([1,2,3]) and Permutation(list(perm)).avoids([2,3,1]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]) and Permutation(list(perm)).avoids([4,3,2,1]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([1,3,2,4]))
rules = list(generate_rules_upto(3, 3, [ I, P, None, incr, decr, decr_nonempty ] + avoiders_len_3, 3))
# rules = list(generate_rules_upto(3, 3, [ I, P, None, incr, decr, decr_nonempty, incr_nonempty ], 3))
# rules = list(generate_rules_upto(3, 3, [ I, P, None, incr, decr, decr_nonempty, incr_nonempty ] + avoiders_len_3, 3))

# for rule in rules:
#     display_rule(rule)
#     print('')

res = find_multiple_rules(rules, empty, 5, 4, permProp)

rescnt = 0
for x in res:
    print('=======================================')
    print('Result:')
    rescnt += 1
    for rule, bs in x:
        display_rule(rule)
        print(bin(bs))
        print('')

print('=======================================')
print('Number of results: %d' % rescnt)


# if res is None:
#     print('None')
# else:
#     print(len(res))
#     for rule, bs in res:
#         display_rule(rule)
#         print(bin(bs))
#         print('')

# for r, b in find_multiple_rules(rules, empty, 3, permProp):
#     print(r, b)

def main():
    n = 3
    m = 3
    cnt = 4

    rules = generate_rules(n, m, [ I, P, None, incr, decr ], cnt)
    for rule in rules:

        # if matches_rule(rule, [Permutation([])], 5, permProp, permCount):
        if matches_rule(rule, [()], 5, permProp, permCount):
            print(rule.rule)

# if __name__ == '__main__':
#     main()

