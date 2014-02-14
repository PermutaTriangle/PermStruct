
from sage.combinat.permutation import Permutation, Permutations
from permutation_sets import Point, Input, SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from permstruct import generate_all_of_length, generate_rules, matches_rule, I, P, N, empty

# Increasing permutations
incr_gen = SimpleGeneratingRule(Permutation([1,2]), [I, P])

# Decreasing permutations
decr_gen = SimpleGeneratingRule(Permutation([2,1]), [I, P])

avoids_132 = StaticPermutationSet.from_predicate(lambda x: x.avoids([1,3,2]), 6, N)

# Avoiders of 231 and 312
avoid_231_312 = SimpleGeneratingRule(Permutation([1,3,2]), [I, P, decr_gen.to_static(10, empty)])

avoid_231_312_G = GeneratingRule([
    [N, P, N],
    [N, N, decr_gen.to_static(10, empty)],
    [I, N, N],
])

avoid_vinc_3_12_ = GeneratingRule([
    [N, P, N],
    [I, N, decr_gen.to_static(10,empty)]
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

# permProp  = (lambda perm : perm.avoids([1,2,3]))
# permProp  = (lambda perm : perm.avoids([1,2,3]))
# permProp  = (lambda perm : perm.avoids([2,3,1]))
# permProp  = (lambda perm : perm.avoids([1,2,3]) and perm.avoids([1,3,2]))
permProp  = (lambda perm : perm.avoids([1,4,2,3]) and perm.avoids([3,2,1]))
# permProp  = (lambda perm : perm.avoids([1,3,2,4]))
# permProp  = (lambda perm : perm.avoids([1,3,2,4]))
permCount = (lambda n : len(filter(lambda x : permProp(x), Permutations(n))) )

incr = incr_gen.to_static(8, empty)
decr = decr_gen.to_static(8, empty)

incr_nonempty = incr_gen.to_static(8, {1:[Permutation([1])]})
decr_nonempty = decr_gen.to_static(8, {1:[Permutation([1])]})

# avoids_132 = avoids_132.to_static(8, empty)


# for n in range(1, 4+1):
#     for m in range(1, 4+1):


rule = GeneratingRule([
    [decr,N,N],
    [N,P,N],
    [I,N,N]
])

def main():
    n = 4
    m = 4
    cnt = 4

    rules = generate_rules(n, m, [ I, P, None, incr, decr ], cnt)
    for rule in rules:

        if matches_rule(rule, [Permutation([])], 5, permProp, permCount):
            print(rule.rule)

if __name__ == '__main__':
    main()

