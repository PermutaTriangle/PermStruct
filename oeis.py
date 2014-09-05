
from permstruct import *
from permstruct.lib import *
from permstruct.permutation_sets import *
import copy

avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append(StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 9, description='Av(%s)' % str(p)))

incr_gen = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing')
decr_gen = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing')

incr = incr_gen.to_static(9, empty)
incr_nonempty = incr_gen.to_static(9, {1:[(1,)]}, description='increasing nonempty')
decr = decr_gen.to_static(9, empty)
decr_nonempty = decr_gen.to_static(9, {1:[(1,)]}, description='decreasing nonempty')

out1 = open('output1', 'w')
out2 = open('output2', 'w')

max_n = 9
done = set()

for rule in generate_rules_upto(3, 3, [ I, P, None, incr, decr, decr_nonempty, incr_nonempty ] + avoiders_len_3, 3):

    cur = copy.deepcopy(empty)
    ok = True
    for n in range(max_n + 1):
        cur.setdefault(n, [])
        for perm in rule.generate_of_length(n, cur):
            cur[n].append(perm)

        if len(set(cur[n])) != len(cur[n]):
            ok = False
            break

    if not ok:
        continue

    res = tuple([ len(cur[n]) for n in range(max_n + 1) ])

    out2.write(str(rule) + '\n')
    out2.write(', '.join(map(str, res)) + '\n')

    if res in done:
        continue

    done.add(res)
    out1.write(', '.join(map(str, res)) + '\n')
    print(', '.join(map(str, res)))

out1.close()
out2.close()

