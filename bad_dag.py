
class BadDAG(object):

    def __init__(self):
        self.bad = set()

    def mark_bad(self, vertex):
        self.bad.add(vertex)

    def _is_below(self, x, y):
        pass

    def is_bad(self, vertex):
        for b in self.bad:
            if all( self._is_below(x, y) for x, y in zip(b, vertex) ):
                return True

        return False



