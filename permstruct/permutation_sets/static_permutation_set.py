
from permuta import Permutation, Permutations
from .permutation_set import PermutationSet

class StaticPermutationSet(PermutationSet):
    """A static set of permutations."""

    def __init__(self, perms, gf=None, description=None, alone_ok=True):
        super(StaticPermutationSet, self).__init__(description=description)

        self.perms = dict()
        self.gf = gf
        self.alone_ok = alone_ok

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
        return tuple(perm) in self.perms.get(len(tuple(perm)), set())

    def generate_of_length(self, n, input):
        return self.perms.get(n, [])

    def min_length(self, input):
        for k in sorted(self.perms.keys()):
            if self.perms[k]:
                return k
        assert False

    def can_be_alone(self):
        return self.alone_ok

    def _sorted_seq(self):
        return sorted( p for k,v in self.perms.items() for p in v )

    def __eq__(self, other):
        return type(self) is type(other) and self._sorted_seq() == other._sorted_seq() and self.description == other.description and self.can_be_alone() == other.can_be_alone()

    def __hash__(self):
        return hash(tuple(self._sorted_seq()))

    def __lt__(self, other):
        if self.description != other.description:
            return self.description < other.description
        if self._sorted_seq() != other._sorted_seq():
            return self._sorted_seq() < other._sorted_seq()
        if self.can_be_alone() != other.can_be_alone():
            return self.can_be_alone() < other.can_be_alone()
        return False

