
from .permutation_set import PermutationSet
from permstruct.lib import Permutations

class UniversePermutationSet(PermutationSet):
    """A permutation set representing all permutations."""

    def __init__(self):
        super(UniversePermutationSet, self).__init__(description='universe permutation set')

    def generate_of_length(self, n, input):
        return [ tuple(p) for p in Permutations(n) ]

    def __repr__(self):
        return 'UniversePermutationSet()'
