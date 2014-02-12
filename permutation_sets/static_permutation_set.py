
from sage.combinat.permutation import Permutation, Permutations
from permutation_set import PermutationSet

class StaticPermutationSet(PermutationSet):
    """A static set of permutations."""

    def __init__(self, perms, gf=None):
        self.perms = dict()
        self.gf = gf

        for perm in perms:
            n = len(perm)
            self.perms.setdefault(n, [])
            self.perms[n].append(perm)

    @staticmethod
    def from_predicate(predicate, max_n, gf=None):

        perms = []
        for n in range(max_n+1):
            for perm in Permutations(n):
                if predicate(perm):
                    perms.append(perm)

        return StaticPermutationSet(perms, gf)

    def generating_function(self):

        if self.gf is None:
            raise NotImplementedError()

        return self.gf

    def generate_of_length(self, n, input):
        return self.perms.get(n, [])

