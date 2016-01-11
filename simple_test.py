
from permstruct import generate_all_of_length, generate_rules, generate_rules_upto, matches_rule, find_multiple_rules, I, P, N, empty
from permstruct.permutation_sets import SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from permuta import Permutation, Permutations

def avoids_312_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[j] < perm[k] < perm[i]:
                return False
    return True

avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append(StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 5, description='Av(%s)' % str(p)))

# permProp  = (lambda perm : Permutation(list(perm)).avoids([1,2]))
permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]))
# permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]) and Permutation(list(perm)).avoids([1,2,3]))
# permProp  = (lambda perm : avoids_312_vinc(perm))

incr = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})

n = 3 # height of rules to check
m = 3 # width of rules to check
inp_types = [ I, P, None, incr, decr, incr_nonempty, decr_nonempty ] # input types
# inp_types = [ I, P, None, incr, decr, incr_nonempty, decr_nonempty ] + avoiders_len_3 # input types
inp_cnt = 3 # max number of inputs

rules = generate_rules_upto(n, m, inp_types, inp_cnt)
for res in find_multiple_rules(rules, 5, 3, permProp, 1):
    print("================================")
    for rule, bs in res:
        print(rule)
        print(bin(bs))
        print('')

