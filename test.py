

from permstruct import *
from permstruct.permutation_sets import *

incr = GeneratingRule([
    [N,P],
    [I,N]
]).to_static(8, empty, description='increasing')

A = GeneratingRule([
    [P,N,N],
    [N,P,incr]
])

B = GeneratingRule([
    [N,N,I],
    [N,P,N],
    [P,N,N],
])

res = empty

for n in range(1,7+1):
    res.setdefault(n, [])

    for perm in A.generate_of_length(n, res):
        res[n].append(perm)

    for perm in B.generate_of_length(n, res):
        res[n].append(perm)

    print('\n'.join(map(str, res[n])))
    # print(n, len(res[n]))

