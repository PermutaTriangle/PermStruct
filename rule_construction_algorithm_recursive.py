
from permuta import Permutation, Permutations
from permuta.misc import flatten, binary_search, choose
from permstruct import I, P, empty, generate_all_of_length
from permstruct.permutation_sets import SimpleGeneratingRule, GeneratingRule, StaticPermutationSet
from itertools import product
import random, sys
from copy import deepcopy

def avoids_312_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[j] < perm[k] < perm[i]:
                return False
    return True

avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append((lambda perm: perm.avoids(p),StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 6, description='Av(%s)' % str(p))))
    # avoiders_len_3.append((lambda perm: len(perm) >= 3 and perm.avoids(p),StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 6, description='Av(%s)' % str(p))))

incr = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [I, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [I, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})



max_len = 6
n_range = (2, 3) # number of rows (min, max)
m_range = (2, 3) # numbor of columns (min, max)
max_nonempty = 3

# permProp = lambda perm: perm.avoids([1,2])
# permProp = lambda perm: perm.avoids([2,3,1])
# permProp = lambda perm: perm.avoids([1,3,2,4])
# permProp  = lambda perm : perm.avoids([2,3,1]) and perm.avoids([1,2,3])
# permProp = avoids_312_vinc

inputs = [
    (permProp, I),
    (lambda perm: len(perm) == 1, P),
    (lambda perm: perm == Permutation(sorted(perm)), incr),
    (lambda perm: perm == Permutation(sorted(perm)[::-1]), decr),
    (lambda perm: len(perm) >= 1 and perm == Permutation(sorted(perm)), incr_nonempty),
    (lambda perm: len(perm) >= 1 and perm == Permutation(sorted(perm)[::-1]), decr_nonempty),
    # (permProp, I),
    # (lambda perm: len(perm) == 1, P),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)), incr),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)[::-1]), decr),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)), incr_nonempty),
    # (lambda perm: len(perm) >= 3 and perm == Permutation(sorted(perm)[::-1]), decr_nonempty),
]

# inputs += avoiders_len_3

indent = 0
old_print = print
def print(*args):
    global indent
    s = '\n'.join([ ' ' * indent + line for line in ' '.join(map(str, args)).split('\n') ])
    old_print(s)

def construct_rule(permSet, left, ignore_first):

    # print(left)
    # input()

    if sum( 1 for p in left if len(p) >= ignore_first ) == 0:
        return []

    # pick the main permutation to work with, currently just chooses one of the
    # largest ones randomly
    B = max(map(len, left))
    main_perms = [ p for p in left if len(p) == B ]
    random.shuffle(main_perms)
    main_perm = main_perms[0]

    ok_rules = {}
    tried_rules = set()
    for n in range(n_range[0], n_range[1] + 1):
        for m in range(m_range[0], m_range[1] + 1):
            for xsep in choose(B - 1, n - 1):
                for ysep in choose(B - 1, m - 1):

                    arr = [ [ [] for j in range(m) ] for i in range(n) ]

                    nonempty_cnt = 0
                    ok = True
                    for i in range(n):
                        for j in range(m):
                            for k in range(0 if j == 0 else ysep[j-1] + 1, (B - 1 if j == m - 1 else ysep[j]) + 1):
                                if (0 if i == 0 else xsep[i-1] + 1) <= B - main_perm[k] <= (B - 1 if i == n - 1 else xsep[i]):
                                    arr[i][j].append(main_perm[k])

                            if arr[i][j]:
                                nonempty_cnt += 1
                                if nonempty_cnt > max_nonempty:
                                    ok = False
                                    break

                        if not ok:
                            break

                    if not ok:
                        continue

                    nonempty = []
                    for i in range(n):
                        for j in range(m):
                            if arr[i][j]:
                                arr[i][j] = Permutation.to_standard(arr[i][j])
                                cur = []
                                for inp_prop, inp in inputs:
                                    if inp_prop(arr[i][j]):
                                        cur.append((i, j, inp))

                                nonempty.append(cur)

                    for poss in product(*nonempty):
                        rule = GeneratingRule({ (i,j): inp for i, j, inp in poss })
                        perms_left = set()
                        cur_generated = set()

                        ok = True
                        for l in range(B+1):
                            curlevel = []
                            for perm in rule.generate_of_length(l, permSet):
                                if perm not in left:
                                    ok = False
                                    # print('Generated something not in the set (%s)' % str(perm))
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

                            cur_generated |= set(cur)

                        ok = ok and len(cur_generated) > 0

                        if ok:

                            cur_left = left - cur_generated

                            print('current rule:')
                            print(rule)
                            # print('it generated:')
                            # print(cur_generated)
                            # print('\n'.join(map(str,cur_generated)))
                            # print('left:')
                            # print(cur_left)
                            # print('\n'.join(map(str,cur_left)))
                            print('recursing...')

                            global indent
                            indent += 4
                            res = construct_rule(permSet, cur_left, ignore_first)
                            indent -= 4

                            print('ans = ', res)

                            if res is not None:
                                return [rule] + res

    return None

permSet = { n: [ tuple(p) for p in Permutations(n) if permProp(p) ] for n in range(max_len + 1) }
left = { p for n in range(max_len + 1) for p in permSet[n] }

res = construct_rule(permSet, left, 1)
print('res:')

for rule in res:
    print(rule)
    print('')

