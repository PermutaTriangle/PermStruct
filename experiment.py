
from permstruct import generate_all_of_length, generate_rules, generate_rules_upto, matches_rule, find_multiple_rules, I, P, N, empty
from permstruct.permutation_sets import SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from permstruct.lib import Permutation, Permutations
import bisect

def avoids_312_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[j] < perm[k] < perm[i]:
                return False
    return True

def contains_mesh_pattern(p, patt):
    (q, s) = patt
    s = set(s)

    def flatten(x):
        n = len(x)
        res = list(range(n))
        for at, (k, i) in enumerate(sorted( (x[i], i) for i in range(n) )):
            res[i] = at
        return res

    def contains(i, now):
        if len(now) == len(q):
            st = sorted(now)
            x = 0
            for k in p:
                if x < len(now) and k == now[x]:
                    x += 1
                else:
                    y = bisect.bisect_left(st, k)
                    if (x,y) in s:
                        return False
            return True

        if i == len(p):
            return False

        nxt = now + [p[i]]
        if flatten(nxt) == flatten(q[:len(nxt)]):
            if contains(i+1, nxt):
                return True

        return contains(i+1, now)

    return contains(0, [])


avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append(StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 5, description='Av(%s)' % str(p)))

incr = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})



# rule = GeneratingRule([
#     [decr, N, N],
#     [N, N, decr_nonempty],
#     [N, P, N],
#     [N, N, decr]
# ])

# rule = GeneratingRule([
#     # [N, incr, incr],
#     # [incr, incr, N],
#     # [N, N, incr, incr],
#     # [N, incr, incr, N],
#     # [incr, incr, N, N],
# 
#     [N, I],
#     [incr, incr]
# ])
# 
# # rule2 = GeneratingRule([
# #     [decr_nonempty, decr, N],
# #     [N, N, P],
# #     [N, decr, N]
# # ])
# 
# res = generate_all_of_length(6, rule, empty)
# # res2 = generate_all_of_length(6, rule2, empty)
# 
# 
# for k in range(6+1):
#     # res[k] += res2[k]
# 
#     # print(k, len(res[k]), len(set(res[k])), { tuple(p) for p in Permutations(k) if p.avoids([1,2,3]) } - set(res[k]))
#     # print(k, len(res[k]), len(set(res[k])), { tuple(p) for p in Permutations(k) if p.avoids([3,2,1]) } - set(res[k]))
#     # print(k, len(res[k]), len(set(res[k])), res[k], res2[k])
#     print(k, len(set(res[k])), len(res[k]))



permProp  = (lambda perm : Permutation(list(perm)).avoids([1,2]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([1,2,3]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]) and Permutation(list(perm)).avoids([1,2,3]))
# permProp  = (lambda perm : avoids_312_vinc(perm))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,4,1]) and not contains_mesh_pattern(perm, ( Permutation([3,2,4,1]), [ (1,4) ] )))

n = 2 # height of rules to check
m = 2 # width of rules to check
inp_types = [ I, P, None, incr, decr, incr_nonempty, decr_nonempty ] # input types
# inp_types += avoiders_len_3 # adding avoiders of a pattern of length 3 to input types
inp_cnt = 4 # max number of inputs

rules = generate_rules_upto(n, m, inp_types, inp_cnt)
for res in find_multiple_rules(rules, 5, 3, permProp, 1):
    print("================================")
    for rule, bs in res:
        print(rule)
        print(bin(bs))
        print('')


