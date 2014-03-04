
from sage.combinat.permutation import Permutation
from permutation_set import PermutationSet

class Input(PermutationSet):
    """A permutation set representing the input permutations."""

    def __init__(self):
        # PermutationSet.__init__(self, description='input')
        self.description = description

    # When we implement get_generating_function, this is probably what it will
    # look like:
    # def get_generating_function(self):
    #     return A

    def generate_of_length(self, n, input):
        return input.get(n, [])

    def __repr__(self):
        return 'Input()'

