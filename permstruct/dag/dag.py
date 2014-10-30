
class DAG:
    def __init__(self):
        self.elements = []
        self.predicates = []
        self.below = {}
        self.ids = {}

    def add_element(self, element, predicate):
        id = len(self.elements)
        self.ids[element] = id
        self.elements.append(element)
        self.predicates.append(predicate)
        self.below[id] = set()

    def id(self, element):
        return self.ids[element]

    def put_below(self, above, below):
        self.below[self.id(above)].add(self.id(below))

