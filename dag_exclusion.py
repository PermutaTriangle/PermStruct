
from permstruct import *
from permstruct.lib import *
from permstruct.permutation_sets import *
import sys

avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append(StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 6, description='Av(%s)' % str(p)))

incr = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})

inputs = [
    StaticPermutationSet({ Permutation([]) }),
    P,
    incr_nonempty,
    decr_nonempty,
    incr,
    decr,
] + avoiders_len_3 + [ I, StaticPermutationSet({}) ]

dag = {
    # 0: [ 1, 2, 11 ],
    # 1: [ 3 ],
    # 2: [ 4 ],
    # 3: [ 6, 7, 8, 9, 10 ],
    # 4: [ 5, 6, 7, 8, 9 ],
    # 5: [  ],
    # 6: [  ],
    # 7: [  ],
    # 8: [  ],
    # 9: [  ],
    # 10: [  ],
    # 11: [  ], # input

    0: [4, 5],
    1: [2, 3],
    2: [4],
    3: [5],
    4: [7,8,9,10,11],
    5: [6,7,8,9,10],
    6: [ ],
    7: [ ],
    8: [ ],
    9: [ ],
    10: [ ],
    11: [ ], # input
    12: [ ],
    13: [0, 1, 12]

}

max_len = 6
ignore_first = 1
n_range = (1, 3)
m_range = (1, 3)

# perm_prop = lambda perm: Permutation(perm).avoids([ 2, 3, 1 ])
perm_prop = lambda perm: Permutation(perm).avoids([2, 1])
perm_created = { n: [ tuple(perm) for perm in Permutations(n) if perm_prop(perm) ] for n in range(max_len + 1) }
perm_set = { perm for n in range(max_len + 1) for perm in perm_created[n] }


visited = set()
def walk(n, m, cur, bad):

    if cur in visited:
        return

    visited.add(cur)

    # print(cur, bad)
    # print(n, m)

    if not bad:
        rule = GeneratingRule({ (i,j): inputs[t] for i, j, t in cur })
        print(rule)

        for i in range(ignore_first, max_len + 1):
            for perm in rule.generate_of_length(i, perm_created):
                if perm not in perm_set:
                    bad = True
                    break

            if bad:
                break

        print('done')

    for i in range(len(cur)):
        for child in dag[cur[i][2]]:
            walk(n, m, tuple([ (cur[j][0], cur[j][1], child) if i == j else cur[j] for j in range(len(cur)) ]), bad)


for n in range(n_range[0], n_range[1] + 1):
    for m in range(m_range[0], m_range[1] + 1):
        for subset in range(2 ** (n * m)):

            use = { (i // m, i % m) for i in range(n * m) if (subset & (1 << i)) != 0 }

            ok = True
            for i in range(n):
                if not any( (i,j) in use for j in range(m) ):
                    ok = False
                    break

            for j in range(m):
                if not any( (i,j) in use for i in range(n) ):
                    ok = False
                    break

            if not ok:
                continue

            # print(use)

            # print(n, m)
            # for i in range(n):
            #     sys.stdout.write('|')
            #     for j in range(m):
            #         sys.stdout.write('P' if (i,j) in use else ' ')
            #         sys.stdout.write('|')

            #     sys.stdout.write('\n')

            # print('')

            visited = set()
            walk(n, m, tuple([ (i, j, 0) for i, j in use ]), False)


