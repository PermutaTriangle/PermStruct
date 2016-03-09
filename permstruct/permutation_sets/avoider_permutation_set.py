from permuta import Permutation
from permuta.misc import ordered_set_partitions, flatten
from .permutation_set import PermutationSet
from .static_permutation_set import StaticPermutationSet
from .point_permutation_set import PointPermutationSet
from .input_permutation_set import InputPermutationSet
from itertools import product
from copy import deepcopy

class AvoiderPermutationSet(PermutationSet):
    def __init__(self, avoid):
        self.avoid = sorted([ list(a) for a in avoid ])
        super(AvoiderPermutationSet, self).__init__(description='Av(%s)' % self.avoid)
        self.length = -1
        self.permutations = {}

    def _assure_length(self, l):
        if l <= self.length:
            return
        if l == 0:
            self.permutations[0] = [ tuple() ]
        else:
            self._assure_length(l-1)
            here = set()
            for p in self.permutations[l-1]:
                for i in range(l):
                    q = p[:i] + (l,) + p[i:]
                    if Permutation(q).avoids(self.avoid):
                        here.add(q)
            self.permutations[l] = list(here)

    def generate_of_length(self, n, input):
        self._assure_length(n)
        return self.permutations[n]

    def contains(self, perm):
        self._assure_length(len(perm))
        return tuple(perm) in self.permutations[len(perm)]

    def __repr__(self):
        return 'AvoiderPermutationSet(%s)' % repr(self.avoid)

    def __eq__(self, other):
        return type(other) is AvoiderPermutationSet and self.avoid == other.avoid

    def __hash__(self):
        return sum( hash(tuple(x)) for x in self.avoid )

    def can_be_alone(self):
        return True

    def __lt__(self, other):
        return self.description < other.description

    def min_length(self, input):
        return 0

