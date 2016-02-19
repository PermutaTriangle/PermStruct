from .permutation_set import PermutationSet

class Length0PermutationSet(PermutationSet):
    """A permutation set containing only the single permutation of length 0."""

    def __init__(self):
        super(Length0PermutationSet, self).__init__(description='empty permutation')

    # When we implement get_generating_function, this is probably what it will
    # look like:
    # def get_generating_function(self):
    #     return 1

    def generate_of_length(self, n, input):

        if n == 0:
            yield tuple()

    def contains(self, perm):
        return len(perm) == 0

    def min_length(self, input):
        return 0

    def __repr__(self):
        return 'Length0PermutationSet()'

    def __eq__(self, other):
        return type(self) is type(other)

    def __hash__(self):
        return hash(tuple([repr(self), 12387841212314]))

