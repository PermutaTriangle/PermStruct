
class PermutationSet(object):

    def __init__(self, description=None):
        self.description = description

    def get_of_length(self, n):
        raise NotImplementedError()

    def generating_function(self):
        raise NotImplementedError()

    def contains(self, perm):
        raise NotImplementedError()

