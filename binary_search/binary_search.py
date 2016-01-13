
from permstruct import *
from permuta import *
from permuta.misc import *
from permstruct.permutation_sets import *
import sys
from itertools import product
import random

#  _____________________________________________________________
# / Hi Bjarki in the future. Don't forget to try adjusting just \
# | the upper bound (and make the lower bound just the trivial  |
# \ empty rule). Baiiiiii                                       /
#  -------------------------------------------------------------
#       \
#        \
#         \
#       ▄  ▄▄▄▄▄▄▄▄▄▄
#    ▄  █▄█████▄▄██▄█▄▄
#  █▄█▄▄█████▄███▄▄███▄▄▄
#  ▀▄███▄███▄▄▄▄▄██▄████▄█
#    ▀▄▄▄▄▄▄█████▄█████▄██
#      ▄▄▄███▄▄▄▄████▄▄▄██
#      ▄█▄██▄██▄▄█▄▄█▄▄██▀
#      █▄▄█▄█▄██▄█████▄▀█      ▄▄▄▄▄▄▄▄▄▄▄
#      █▄███▄██▄▄████▄▄      ▄▄█▄█▄▄▄▄▄▄▄▄▄▄
#      ▀▄▄▄▄█████▄███▄▀     ▄▄▄█▄▄▄▄▄███▄▄▀ ▀
#         ▀▀▀▀█▄▄████   ▄▄▄▄▄▄▄█▄████▄▄██▄▄
#             ███████▄▄▄███▄██   ▀▄███▄▄███▄▄
#             ███████▄▄▄▄█▄▄█▄█    ██████████
#              ███████▄▄▄▄█▄███    ███████████
#               ▄▄██▄▄▄▄▄▄████     ███████████
#               █▄████▀▀▄▄▄▄█▄▄▄   ▀▄████████
#               ██████   ██▄▄███    ▀▄███████
#              ███████   ██████▄▄     ████▄▄██  ▄█
#             ▄▄██████   ████████      ▀▄██▄▄█▄▄██
#            █▄███████   ███████▄▄       ▀▄▄▄▄▄▄▀
#            ▀▀█▄███▄▀   ▀▀▀██████
#              ▀▀▀▀▀▀       ▀▀▀▀▀▀

avoiders_len_3 = []
for p in Permutations(3):
    avoiders_len_3.append(StaticPermutationSet.from_predicate(lambda x: x.avoids(p), 7, description='Av(%s)' % str(p)))

incr = SimpleGeneratingRule(Permutation([1,2]), [X, P], description='increasing').to_static(8, empty)
decr = SimpleGeneratingRule(Permutation([2,1]), [X, P], description='decreasing').to_static(8, empty)

incr_nonempty = SimpleGeneratingRule(Permutation([1,2]), [X, P], description='increasing nonempty').to_static(8, {1:[Permutation([1])]})
decr_nonempty = SimpleGeneratingRule(Permutation([2,1]), [X, P], description='decreasing nonempty').to_static(8, {1:[Permutation([1])]})

inputs = (
        [
            StaticPermutationSet({}, description='empty set'),
            S,
            StaticPermutationSet({ () }, description='empty permutation'),
            P,
            X,
            # incr_nonempty,
            # decr_nonempty,
            incr,
            decr,
            # N,
        ]
        # + avoiders_len_3
)


# for i, inp in enumerate(inputs):
#     print(i, inp.description)
# 
# sys.exit(0)

def avoids_312_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[j] < perm[k] < perm[i]:
                return False
    return True

def avoids_231_vinc(perm):
    for i in range(len(perm)):
        j = i + 1
        for k in range(j+1, len(perm)):
            if perm[k] < perm[i] < perm[j]:
                return False
    return True

def avoids_123_vinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            k = j + 1
            if k < len(perm) and perm[i] < perm[j] < perm[k]:
                return False
    return True

def avoids_312_covinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            for k in range(j+1, len(perm)):
                if perm[j] < perm[k] < perm[i] and perm[i] == 1 + perm[k]:
                    return False
    return True

def avoids_132_covinc(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            for k in range(j+1, len(perm)):
                if perm[i] < perm[k] < perm[j] and perm[j] == 1 + perm[k]:
                    return False
    return True

B = 7
permProp = lambda perm: perm.avoids([2,3,1])
# permProp = lambda perm: perm.avoids([2,1])
# permProp = lambda perm: perm.avoids([1,3,2,4])
# permProp = lambda perm: perm.avoids([1,2,3])
# permProp = lambda p: avoids_231_vinc(p) and p.avoids([1,2,3])
# permProp = avoids_312_vinc
# permProp = lambda p: avoids_123_vinc(p) and avoids_312_covinc(p)
# permProp = lambda p: avoids_132_covinc(p) and avoids_123_vinc(p)
n = 3
m = 3

# for l in range(10):
#     cnt = 0
#     for p in Permutations(l):
#         if permProp(p):
#             cnt += 1
# 
#     print(cnt)
# 
# import sys
# sys.exit(0)


inputPermSet = StaticPermutationSet.from_predicate(permProp, B)
inputPermSet = { l: inputPermSet.generate_of_length(l, {}) for l in range(B + 1) }
inputPermSetSet = set([ p for l in range(B + 1) for p in inputPermSet[l] ])



# for l in range(B):
#     print(inputs[1].generate_of_length(l, inputPermSet))
# 
# sys.exit(0)

input_sets = [
    set([ p for l in range(B + 1) for p in i.generate_of_length(l, inputPermSet) ]) if i is not None else set([]) for i in inputs
]


# for i in range(len(inputs)):
#     print(i, inputs[i])
#     print(input_sets[i])


below = { i: set() for i in range(len(inputs)) }
above = { i: set() for i in range(len(inputs)) }

for i in range(len(inputs)):
    for j in range(len(inputs)):
        if i == j:
            continue

        # if input_sets[i] >= input_sets[j] or (i == 3 or j == 2):
        if input_sets[i] >= input_sets[j]:
            # print(i, '>=', j)
            below[j].add(i)
            above[i].add(j)

        # print(inputs[i], inputs[j])
        # print(input_sets[i])
        # print(input_sets[j])


above[3].add(2)
below[2].add(3)

# print(above)
# print(below)

between = { }

for i in range(len(inputs)):
    for j in range(len(inputs)):


        s = set()

        if i != j:
            for k in range(len(inputs)):
                if (k in below[i] and k in above[j]) or (k in below[j] and k in above[i]):
                    s.add(k)

        # if 2 in s: s.add(3)
        # if 3 in s: s.add(2)

        between[(i,j)] = s


between[(2,2)].add(3)

# print(sorted(between.items()))
# sys.exit(0)

def pick(x, y, lo, hi, arr):

    # if 2 in arr: arr.add(3)
    # if 3 in arr: arr.add(2)

    arr.add(4)

    # print(arr)
    arr = list(arr)
    # if 3 in arr:
    #     return 3
    res = random.choice(arr)
    # print('(%d,%d): between %d and %d, %s, %d' % (x, y, lo, hi, repr(arr), res))
    return res

def rule_from_arr(arr):
    return GeneratingRule([ [ inputs[arr[row][col]] for col in range(m) ] for row in range(n) ])

while True:
    print('starting')
    lo = [ [ 2 for col in range(m) ] for row in range(n) ]
    lo_set = { () }
    # lo = [ [ 0 for col in range(m) ] for row in range(n) ]
    hi = [ [ 1 for col in range(m) ] for row in range(n) ]


    tried = set()
    cnt = 0

    done = False

    # for it in range(50):
    while cnt < 10000:

        # if any( 3 in lo[row] for row in range(n) ) or any( 3 in hi[row] for row in range(n) ):
        #     print('lo', lo)
        #     print('hi', hi)

        # print('lo', lo)
        # print('hi', hi)
        x,y = random.choice([ (i,j) for i in range(n) for j in range(m) ])
        if lo[x][y] == hi[x][y]:
            # print('picked same again')
            continue

        # mid = [ [ pick(row, col, lo[row][col], hi[row][col], between[( lo[row][col], hi[row][col] )] | set([ lo[row][col], hi[row][col] ])) for col in range(m) ] for row in range(n) ]
        # print(lo)
        # print(hi)
        # mid = [ [ pick(row, col, lo[row][col], hi[row][col], between[( lo[row][col], hi[row][col] )] | set([ lo[row][col] ])) if (row,col) == (x,y) else lo[row][col] for col in range(m) ] for row in range(n) ]
        mid = [ [ pick(row, col, lo[row][col], hi[row][col], between[( lo[row][col], hi[row][col] )] ) if (row,col) == (x,y) else lo[row][col] for col in range(m) ] for row in range(n) ]

        state = (tuple([ tuple(row) for row in lo ]), tuple([ tuple(row) for row in mid ]))
        if state in tried:
            cnt += 1
            continue

        tried.add(state)
        cnt = 0

        # if any( 3 in mid[row] for row in range(n) ):
        #     print('mid', mid)

        # print('mid', mid)

        mid_rule = rule_from_arr(mid)

        gen = { 0: [()], 1: [(1,)] }
        overlap = False
        for l in range(2, B + 1):
            gen.setdefault(l, [])
            for p in mid_rule.generate_of_length(l, gen):
            # for p in mid_rule.generate_of_length(l, inputPermSet):
                gen[l].append(p)

            if len(gen[l]) != len(set(gen[l])):
                overlap = True
                break

        if overlap:
            # print('overlap')
            continue

        mid_perms = { p for l in range(B + 1) for p in gen[l] }

        if not (lo_set <= mid_perms):
            # print('stepping sideways')
            continue


        # print('Hi')
        # print(rule_from_arr(hi))

        # print('Mid')
        # print(rule_from_arr(mid))

        # print('mid_perms')
        # print(mid_perms)
        # print('input', inputPermSetSet)


        # print('mid_perms', mid_perms)


        if mid_perms == inputPermSetSet:
            done = True
            lo = mid
            lo_set = mid_perms
            hi = mid

            print('Doooooooooooooooooonneeeeeeeeeeee!')

            break

        if mid_perms <= inputPermSetSet:
            # print('found new lower')
            lo = mid
            lo_set = mid_perms
        # elif inputPermSetSet <= mid_perms:
        #     print('found new higher')
        #     hi = mid
        # else:
        #     print('wat')
        #     assert False


        # print('Lo')
        # print(rule_from_arr(lo))


        # gen = { 0: [()], 1: [(1,)] }
        # lo_rule = rule_from_arr(lo)
        # for l in range(2, B + 1):
        #     gen.setdefault(l, [])
        #     for p in lo_rule.generate_of_length(l, gen):
        #     # for p in lo_rule.generate_of_length(l, inputPermSetSet):
        #         gen[l].append(p)

        # print(' '.join( str(len(v)) for k, v in gen.items() ))

        # print(lo)

    # print('Lo')
    # print(rule_from_arr(lo))
    # print('Hi')
    # print(rule_from_arr(hi))


    print(rule_from_arr(lo))

    gen = { 0: [()], 1: [(1,)] }
    lo_rule = rule_from_arr(lo)
    for l in range(2, B + 1):
        gen.setdefault(l, [])
        for p in lo_rule.generate_of_length(l, gen):
        # for p in lo_rule.generate_of_length(l, inputPermSetSet):
            gen[l].append(p)

    print(' '.join( str(len(v)) for k, v in gen.items() ))

    if done:
        break

