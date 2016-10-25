from permstruct.permutation_sets import GeneratingRule
from permstruct import N

class DAG:
    def __init__(self):
        self.elements = []
        self.below = {}
        self.above = {}
        self.ids = {}

    def add_element(self, element):
        id = len(self.elements)
        self.ids[element] = id
        self.elements.append(element)
        self.below[id] = set()
        self.above[id] = set()

    def id(self, element):
        return self.ids[element]

    def put_below(self, above, below):
        self.below[self.id(above)].add(self.id(below))
        self.above[self.id(below)].add(self.id(above))

    def get_below(self, elem):
        return [ self.elements[x] for x in self.below[self.id(elem)] ]

    def get_above(self, elem):
        return [ self.elements[x] for x in self.above[self.id(elem)] ]

    def get_parents(self, elem):
        return [ self.elements[s] for s in self.above[self.id(elem)] ]

    def get_reachable_above(self, elem):
        vis = set()
        def dfs(cur):
            if cur in vis:
                return
            vis.add(cur)
            for nxt in self.above[cur]:
                dfs(nxt)
        dfs(self.id(elem))
        return [ self.elements[s] for s in vis ]

    def get_transitive_reduction(self):
        res = DAG()
        for t in self.elements:
            res.add_element(t)
        def dfs(cur,mark):
            if cur in vis:
                return
            if mark:
                vis.add(cur)
            for nxt in self.above[cur]:
                dfs(nxt,True)
        for cur in range(len(self.elements)):
            vis = set()
            for nxt in self.above[cur]:
                dfs(nxt,False)
            for nxt in self.above[cur]:
                if nxt not in vis:
                    res.put_below(self.elements[nxt], self.elements[cur])
        return res

    def get_topological_order(self):
        res = []
        done = set()
        def dfs(cur):
            if cur in done:
                return
            for t in self.above[cur]:
                dfs(t)
            res.append(self.elements[cur])
            done.add(cur)
        for i in range(len(self.elements)):
            dfs(i)
        return res

