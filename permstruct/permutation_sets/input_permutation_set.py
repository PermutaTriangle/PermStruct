
from .permutation_set import PermutationSet

class InputPermutationSet(PermutationSet):
    """A permutation set representing the input permutations."""

    def __init__(self, predicate=None):
        super(InputPermutationSet, self).__init__(description='input permutation set')
        # self.predicate = predicate

    # When we implement get_generating_function, this is probably what it will
    # look like:
    # def get_generating_function(self):
    #     return A

    def generate_of_length(self, n, input):
        return input.get(n, [])

    def contains(self, perm):
        raise NotImplementedError()
        # assert self.predicate is not None
        # return self.predicate(perm)

    def min_length(self, input):
        for k in sorted(input.keys()):
            if len(input[k]) > 0:
                return k
        assert False

    def __repr__(self):
        return 'InputPermutationSet()'

    def __eq__(self, other):
        return type(self) is type(other)

    def __hash__(self):
        return hash(tuple([repr(self), 12387841212314]))

