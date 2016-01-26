
class PermutationSet(object):

    def __init__(self, description=None):
        self.description = description

    def get_of_length(self, n):
        raise NotImplementedError()

    def generating_function(self):
        raise NotImplementedError()

    def contains(self, perm):
        raise NotImplementedError()

    def min_length(self, input):
        raise NotImplementedError()

    def __hash__(self):
        print(type(self))
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def __lt__(self, other):
        print(type(self), type(other))
        raise NotImplementedError()

