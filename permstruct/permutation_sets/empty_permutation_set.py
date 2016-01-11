from .permutation_set import PermutationSet
from permuta import Permutations

class EmptyPermutationSet(PermutationSet):
    """A permutation set representing no permutations."""

    def __init__(self):
        super(EmptyPermutationSet, self).__init__(description='empty permutation set')

    def generate_of_length(self, n, input):
        return []

    def contains(self, perm):
        return False

    def __repr__(self):
        return 'EmptyPermutationSet()'

