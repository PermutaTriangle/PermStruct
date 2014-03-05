
from permutation_set import PermutationSet

class InputPermutationSet(PermutationSet):
    """A permutation set representing the input permutations."""

    def __init__(self):
        super().__init__(description='input permutation set')

    # When we implement get_generating_function, this is probably what it will
    # look like:
    # def get_generating_function(self):
    #     return A

    def generate_of_length(self, n, input):
        return input.get(n, [])

    def __repr__(self):
        return 'InputPermutationSet()'

