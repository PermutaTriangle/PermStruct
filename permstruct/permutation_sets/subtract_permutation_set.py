from permuta.misc import ordered_set_partitions, flatten
from .permutation_set import PermutationSet
from .static_permutation_set import StaticPermutationSet
from .point_permutation_set import PointPermutationSet
from .input_permutation_set import InputPermutationSet
from itertools import product
from copy import deepcopy

class SubtractPermutationSet(PermutationSet):
    def __init__(self, main, sub, alone_ok=True):
        super(SubtractPermutationSet, self).__init__(description=main.description + ''.join([ ' - ' + (x.description if x is not None else 'empty permutation') for x in sub ]))
        self.main = main
        self.sub = sub
        self.length = -1
        self.permutations = {}
        self.alone_ok = alone_ok

    def _assure_length(self, l, input):
        if l in self.permutations:
            return
        mainp = set()
        here = set()
        for p in self.main.generate_of_length(l, input):
            mainp.add(p)
            here.add(p)
        for s in self.sub:
            if s is None:
                if l == 0:
                    st = [ Permutation() ]
                else:
                    st = [ ]
            else:
                st = s.generate_of_length(l, input)
            for p in st:
                assert p in mainp, "Permutation set %s is invalid. Perhaps perm_bound is too small?" % self.description
                if p in here:
                    here.remove(p)
        self.permutations[l] = list(here)

    def generate_of_length(self, n, input):
        self._assure_length(n, input)
        return self.permutations[n]

    def contains(self, perm):
        # XXX: Shouldn't input be a parameter here?
        input = {}
        self._assure_length(len(perm), input)
        return tuple(perm) in self.permutations[len(perm)]

    def __repr__(self):
        return 'SubtractPermutationSet(%s, %s)' % (repr(self.main), repr(self.sub))

    def __eq__(self, other):
        return type(other) is SubtractPermutationSet and self.main == other.main and sorted(self.sub) == sorted(other.sub)

    def __hash__(self):
        return hash(tuple([ hash(self.main), sum( hash(x) for x in self.sub ) ]))

    def can_be_alone(self):
        return self.alone_ok

    def __lt__(self, other):
        return self.description < other.description

    def min_length(self, input):
        l = 0
        while True:
            self._assure_length(l, input)
            if self.permutations[l]:
                return l
            l += 1
