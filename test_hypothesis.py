
from permstruct import *
from permstruct.permutation_sets import *
from permstruct.lib import Permutation, Permutations

incr_nonempty = GeneratingRule([
    [N,P],
    [I,N]
]).to_static(8, empty, description='increasing nonempty')

B = GeneratingRule([
    [I,N],
    [N,incr_nonempty]
])

C = GeneratingRule([
    [N,I],
    [I,I]
])

A_set = {}
B_set = {}
C_set = {}

for n in range(7+1):

    A_set.setdefault(n, [])
    B_set.setdefault(n, [])
    C_set.setdefault(n, [])

    if n >= 1:
        C_set[n - 1] = sorted(set(A_set[n - 1]) - set(B_set[n - 1]))
        for p in C.generate_of_length(n, C_set):
            C_set[n].append(p)

    for p in Permutations(n):
        if p.avoids([1,3,2,4]):
            A_set[n].append(tuple(p))

    for p in B.generate_of_length(n, A_set):
        B_set[n].append(p)

    C_set[n] = sorted(set(C_set[n]))

    print(n, len(A_set[n]), len(B_set[n]), len(C_set[n]), len(B_set[n]) + len(C_set[n]))

    assert set(B_set[n]) <= set(A_set[n])

    # print(n, len(A_set[n]), len(B_set[n]))
    # print(len(A_set[n]))
    # print('\n'.join(map(str, A_set[n])))
    # print('\n'.join(map(str, A_set[n])))
    # print('\n'.join(map(str, sorted(C_set[n]))))


