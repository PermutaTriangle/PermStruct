
from permstruct import *
from permstruct.lib import *
from permstruct.permutation_sets import *
import sys

try:
    from queue import Queue
except:
    from Queue import Queue

avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append(StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 6, description='Av(%s)' % str(p)))

incr = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})

inputs = [
    N,
    P,
    incr_nonempty,
    decr_nonempty,
    incr,
    decr,
# ] + avoiders_len_3 + [ I, StaticPermutationSet({}, description='empty set') ]
] + [ I, StaticPermutationSet({}, description='empty set') ]

# dag = {
#     # 0: [ 1, 2, 11 ],
#     # 1: [ 3 ],
#     # 2: [ 4 ],
#     # 3: [ 6, 7, 8, 9, 10 ],
#     # 4: [ 5, 6, 7, 8, 9 ],
#     # 5: [  ],
#     # 6: [  ],
#     # 7: [  ],
#     # 8: [  ],
#     # 9: [  ],
#     # 10: [  ],
#     # 11: [  ], # input
# 
#     0: [4, 5], # empty permutation
#     1: [2, 3],
#     2: [4],
#     3: [5],
#     4: [7,8,9,10,11],
#     5: [6,7,8,9,10],
#     6: [ ],
#     7: [ ],
#     8: [ ],
#     9: [ ],
#     10: [ ],
#     11: [ ],
#     12: [ ], # input
#     13: [0, 1, 12] # empty set
# 
# }

dag = {
    0: [4, 5], # empty permutation
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: [],
    6: [ ], # input
    7: [0, 1, 6] # empty set

}

rev_dag = { k: [] for k in dag.keys() }

for k, v in dag.items():
    for c in v:
        rev_dag[c].append(k)


max_len = 6
ignore_first = 1
# n_range = (1, 3)
# m_range = (1, 3)

n_range = (2, 3)
m_range = (2, 3)

perm_prop = lambda perm: Permutation(perm).avoids([ 2, 3, 1 ])
# perm_prop = lambda perm: Permutation(perm).avoids([2, 1])
# perm_prop = lambda perm: Permutation(perm).avoids([1, 3, 2, 4])
# perm_prop = lambda perm: Permutation(perm).avoids([1, 2, 3])
perm_created = { n: [ tuple(perm) for perm in Permutations(n) if perm_prop(perm) ] for n in range(max_len + 1) }
perm_set = { perm for n in range(max_len + 1) for perm in perm_created[n] }


visited = set()
bad_vertices = set()

def under_bad(n, m, cur):

    cur_visited = set()
    cur_visited.add(cur)
    q = Queue()
    q.put(cur)

    while not q.empty():

        c = q.get()
        if c in bad_vertices:
            return True

        if c in visited:
            continue

        for i in range(len(c)):
            for parent in rev_dag[c[i]]:
                nxt = tuple([ parent if i == j else c[j] for j in range(len(c)) ])
                if nxt not in cur_visited:
                    cur_visited.add(nxt)
                    q.put(nxt)

    return False


def walk(n, m, cur):

    if cur in visited:
        return

    if under_bad(n, m, cur):
        visited.add(cur)
        bad_vertices.add(cur)
        return

    visited.add(cur)
    bad = False

    any_empty_set = any( x == 7 for x in cur )
    empty_rows = { row for row in range(n) if all( cur[row * m + col] == 0 for col in range(m) ) }
    empty_cols = { col for col in range(m) if all( cur[row * m + col] == 0 for row in range(n) ) }

    if not any_empty_set:
        di = { (i,j): inputs[cur[i * m + j]] for i in range(n) for j in range(m) if inputs[cur[i * m + j]] is not None }
        if di:
            rule = GeneratingRule({ (i,j): inputs[cur[i * m + j]] for i in range(n) for j in range(m) if inputs[cur[i * m + j]] is not None })
            # print(rule)

            bs = 0
            cur_no = 0
            gen_any = False
            for l in range(ignore_first, max_len + 1):
                gen_perms = []
                for perm in rule.generate_of_length(l, perm_created):
                    if perm not in perm_set:
                        bad = True
                        break

                    gen_perms.append(perm)

                if bad:
                    break

                gen_perms = sorted(gen_perms)
                for a, b in zip(gen_perms, gen_perms[1:]):
                    if a == b:
                        bad = True
                        break

                if bad:
                    break

                i = 0
                j = 0

                while i < len(gen_perms) and j < len(perm_created[l]):
                    if gen_perms[i] < perm_created[l][j]:
                        assert False

                    if gen_perms[i] > perm_created[l][j]:
                        cur_no += 1
                        j += 1

                    if perm_created[l][j] == gen_perms[i]:
                        bs |= 1 << cur_no
                        cur_no += 1
                        i += 1
                        j += 1

                if gen_perms:
                    gen_any = True

            if not bad and gen_any and not empty_rows and not empty_cols:
                print(rule)
                print(bin(bs))
                print('done')
                print('')

    if bad:
        bad_vertices.add(cur)
        return

    for i in range(len(cur)):
        r, c = divmod(i, m)
        if (any_empty_set and cur[i] != 7) or (empty_rows and r not in empty_rows and empty_cols and c not in empty_cols):
            continue

        for child in dag[cur[i]]:
            walk(n, m, tuple([ child if i == j else cur[j] for j in range(len(cur)) ]))


def main():
    for n in range(n_range[0], n_range[1] + 1):
        for m in range(m_range[0], m_range[1] + 1):
            if n == 3 and m == 3:
                continue

            visited = set()
            walk(n, m, tuple([ 7 for i in range(n) for j in range(m) ]))

if __name__ == '__main__':
    main()

