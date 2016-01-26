
from .permutation_set import PermutationSet

class PointPermutationSet(PermutationSet):
    """A permutation set containing only the single permutation of length 1."""

    def __init__(self):
        super(PointPermutationSet, self).__init__(description='point permutation set')

    # When we implement get_generating_function, this is probably what it will
    # look like:
    # def get_generating_function(self):
    #     return x

    def generate_of_length(self, n, input):

        if n == 1:
            yield (1,)

    def contains(self, perm):
        return len(perm) == 1

    def min_length(self, input):
        return 1

    def __repr__(self):
        return 'PointPermutationSet()'

    def __eq__(self, other):
        return type(self) is type(other)

    def __hash__(self):
        return hash(tuple([repr(self), 12387841212314]))

