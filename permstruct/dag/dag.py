from permstruct.permutation_sets import GeneratingRule
from permstruct import N

class DAG:
    def __init__(self):
        self.elements = []
        self.below = {}
        self.ids = {}

    def add_element(self, element):
        id = len(self.elements)
        self.ids[element] = id
        self.elements.append(element)
        self.below[id] = set()

    def id(self, element):
        return self.ids[element]

    def put_below(self, above, below):
        self.below[self.id(above)].add(self.id(below))

