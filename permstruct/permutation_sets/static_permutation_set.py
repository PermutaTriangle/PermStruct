
from permstruct.lib import Permutation, Permutations
from .permutation_set import PermutationSet

class StaticPermutationSet(PermutationSet):
    """A static set of permutations."""

    def __init__(self, perms, gf=None, description=None):
        super(StaticPermutationSet, self).__init__(description=description)

        self.perms = dict()
        self.gf = gf

        for perm in perms:
            n = len(perm)
            self.perms.setdefault(n, [])
            self.perms[n].append(tuple(perm))

    @staticmethod
    def from_predicate(predicate, max_n, gf=None, description=None):

        perms = []
        for n in range(max_n+1):
            for perm in Permutations(n):
                if predicate(perm):
                    perms.append(tuple(perm))

        return StaticPermutationSet(perms, gf, description)

    def generating_function(self):

        if self.gf is None:
            raise NotImplementedError()

        return self.gf

    def contains(self, perm):
        # print('checking if ', perm, ' in self: ', tuple(perm) in self.perms)
        # print(self.perms)
        return tuple(perm) in self.perms[len(tuple(perm))]

    def generate_of_length(self, n, input):
        return self.perms.get(n, [])

