
# from sage.combinat.permutation import Permutation, Permutations
# from permutation_sets import Point, Input, SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
# from permstruct import generate_all_of_length, generate_rules, matches_rule, I, P, N, empty

from permstruct import generate_all_of_length, generate_rules, generate_rules_upto, matches_rule, find_multiple_rules, I, P, N, empty
from permstruct.permutation_sets import SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from permstruct.lib import Permutation, Permutations

permProp  = (lambda perm : Permutation(list(perm)).avoids([2,3,1]))
permCount = (lambda n : len(list(filter(lambda x : permProp(x), Permutations(n)))) )

incr = SimpleGeneratingRule(Permutation([1,2]), [I, P]).to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P]).to_static(8, empty)

n = 3 # height of rules to check
m = 3 # width of rules to check
inp_types = [ I, P, None, incr, decr ] # input types
inp_cnt = 4 # max number of inputs

for rule in generate_rules(n, m, inp_types, inp_cnt):
    if matches_rule(rule, [()], 5, permProp, permCount):
        print('Found rule:')
        print(rule)
        print('')

