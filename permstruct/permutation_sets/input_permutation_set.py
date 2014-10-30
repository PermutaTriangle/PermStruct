
from .permutation_set import PermutationSet

class InputPermutationSet(PermutationSet):
    """A permutation set representing the input permutations."""

    def __init__(self, predicate=None):
        super(InputPermutationSet, self).__init__(description='input permutation set')
        self.predicate = predicate

    # When we implement get_generating_function, this is probably what it will
    # look like:
    # def get_generating_function(self):
    #     return A

    def generate_of_length(self, n, input):
        return input.get(n, [])

    def contains(self, perm):
        assert self.predicate is not None
        return self.predicate(perm)

    def __repr__(self):
        return 'InputPermutationSet()'

