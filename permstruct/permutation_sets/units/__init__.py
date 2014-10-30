from permstruct import empty, X, P
from permstruct.permutation_sets import SimpleGeneratingRule, StaticPermutationSet
from permstruct.lib import Permutation

def incr(n):
    return SimpleGeneratingRule(Permutation([1,2]), [X, P], description='increasing').to_static(n, empty)

def decr(n):
    return SimpleGeneratingRule(Permutation([2,1]), [X, P], description='decreasing').to_static(n, empty)


def incr_nonempty(n):
    return SimpleGeneratingRule(Permutation([1,2]), [X, P], description='increasing nonempty').to_static(n, {1:[Permutation([1])]})

def decr_nonempty(n):
    return SimpleGeneratingRule(Permutation([2,1]), [X, P], description='decreasing nonempty').to_static(n, {1:[Permutation([1])]})


def classical_avoiders(p, n):
    return StaticPermutationSet.from_predicate(lambda x: x.avoids(p), n, description='Av(%s)' % str(p))

