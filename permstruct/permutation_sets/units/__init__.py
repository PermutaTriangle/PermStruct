from permstruct import empty, X, P
from permstruct.permutation_sets import SimpleGeneratingRule, StaticPermutationSet
from permuta import Permutation

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

def input_without_incr(perm_prop, n):
    return StaticPermutationSet.from_predicate(lambda x: perm_prop(x) and not x.avoids([2,1]), n, description='input without incr')

def input_without_decr(perm_prop, n):
    return StaticPermutationSet.from_predicate(lambda x: perm_prop(x) and not x.avoids([1,2]), n, description='input without decr')


def classical_avoiders_2(p1, p2, n):
    return StaticPermutationSet.from_predicate(lambda x: x.avoids(p1) and x.avoids(p2), n, description='Av(%s, %s)' % (str(p1), str(p2)))

def classical_avoiders_2_nonempty(p1, p2, n):
    return StaticPermutationSet.from_predicate(lambda x: len(x) > 0 and x.avoids(p1) and x.avoids(p2), n, description='Av(%s, %s) nonempty' % (str(p1), str(p2)))


def from_predicate(pred, desc, n):
    return StaticPermutationSet.from_predicate(pred, n, description=desc)


# A "How To Add a thing" tutorial by Bjarki
# - Step 1:
# def meow(p, n):
#     return StaticPermutationSet.from_predicate(lambda x: x.meow(), n, description='meow(%s)' % str(p))
# - Step 2:
# ????
# - Step 3: Profit!!!!

