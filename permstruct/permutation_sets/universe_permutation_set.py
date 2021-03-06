
from .permutation_set import PermutationSet
from permuta import Permutations

class UniversePermutationSet(PermutationSet):
    """A permutation set representing all permutations."""

    def __init__(self):
        super(UniversePermutationSet, self).__init__(description='universe permutation set')

    def generate_of_length(self, n, input):
        return [ p for p in Permutations(n) ]

    def contains(self, perm):
        return True

    def min_length(self, input):
        return 0

    def __repr__(self):
        return 'UniversePermutationSet()'
