from permuta.misc import ordered_set_partitions, flatten
from .permutation_set import PermutationSet
from .static_permutation_set import StaticPermutationSet
from .point_permutation_set import PointPermutationSet
from .input_permutation_set import InputPermutationSet
from itertools import product
from copy import deepcopy


class GeneratingRule(PermutationSet):
    """A permutation set containing all permutations generated by a generating
    rule."""

    def __init__(self, rule, description=None):
        super(GeneratingRule, self).__init__(description=description)

        # TODO: store rules as a 2d array, and benchmark
        if type(rule) is list:
            self.rule = { (i,j): rule[i][j] for i in range(len(rule)) for j in range(len(rule[i])) if rule[i][j] is not None }
        else:
            self.rule = { (i,j): s for ((i,j), s) in rule.items() if s is not None }


    # When we implement generating_function, this is probably what it will
    # look like (this will not handle inputs in same row/col):
    # def generating_function(self):
    #     gf = 1
    #     for row in self.rule:
    #         for s in row:
    #             gf *= s.generating_function()
    #     gf += 1
    #     return gf

    def generate_of_length(self, n, input):

        rule = list(self.rule.items())
        h = max( k[0] for k,v in rule ) + 1 if rule else 1
        w = max( k[1] for k,v in rule ) + 1 if rule else 1

        def permute(arr, perm):
            res = [None] * len(arr)
            for i in range(len(arr)):
                res[i] = arr[perm[i] - 1]
            return res

        def count_assignments(at, left):

            if at == len(rule):
                if left == 0:
                    yield []
            elif type(rule[at][1]) is PointPermutationSet:
                # this doesn't need to be handled separately,
                # it's just an optimization
                if left > 0:
                    for ass in count_assignments(at + 1, left - 1):
                        yield [1] + ass
            else:
                for cur in range(left+1):
                    for ass in count_assignments(at + 1, left - cur):
                        yield [cur] + ass

        for count_ass in count_assignments(0, n):
            for perm_ass in product(*[ s[1].generate_of_length(cnt, input) for cnt, s in zip(count_ass, rule) ]):

                arr = [ [ [] for j in range(w) ] for i in range(h) ]

                for i, perm in enumerate(perm_ass):
                    arr[rule[i][0][0]][rule[i][0][1]] = perm

                rowcnt = [ sum( len(arr[row][col]) for col in range(w) ) for row in range(h) ]
                colcnt = [ sum( len(arr[row][col]) for row in range(h) ) for col in range(w) ]

                for colpart in product(*[ ordered_set_partitions(range(colcnt[col]), [ len(arr[row][col]) for row in range(h) ]) for col in range(w) ]):
                    for rowpart in product(*[ ordered_set_partitions(range(rowcnt[row]), [ len(arr[row][col]) for col in range(w) ]) for row in range(h) ]):
                        res = [ [None]*colcnt[col] for col in range(w) ]

                        cumul = 1
                        for row in range(h-1,-1,-1):
                            for col in range(w):
                                for idx, val in zip(sorted(colpart[col][row]), permute(sorted(rowpart[row][col]), arr[row][col])):
                                    res[col][idx] = cumul + val

                            cumul += rowcnt[row]

                        yield tuple(flatten(res))


    def to_static(self, max_n, input, description=None):

        inp = deepcopy(input)

        for n in range(max_n+1):
            for perm in self.generate_of_length(n, inp):
                inp.setdefault(n, [])
                inp[n].append(perm)

        try:
            gf = self.generating_function()
        except NotImplementedError:
            gf = None

        perms = [ p for ps in inp.values() for p in ps ]
        return StaticPermutationSet(perms, gf, description if description is not None else self.description)

    def __str__(self):

        n = max( i for i,j in self.rule )+1 if self.rule else 1
        m = max( j for i,j in self.rule )+1 if self.rule else 1
        arr = [ [ ' ' for j in range(2*m+1) ] for i in range(2*n+1) ]
        labels = {}

        for i in range(2*n+1):
            for j in range(2*m+1):
                a = i % 2 == 0
                b = j % 2 == 0
                if a and b:
                    arr[i][j] = '+'
                elif a:
                    arr[i][j] = '-'
                elif b:
                    arr[i][j] = '|'

        for i,j in self.rule:
            if type(self.rule[(i,j)]) is InputPermutationSet:
                arr[2*i+1][2*j+1] = 'X'
            elif type(self.rule[(i,j)]) is PointPermutationSet:
                arr[2*i+1][2*j+1] = 'o'
            else:
                if self.rule[(i,j)] not in labels:
                    labels[self.rule[(i,j)]] = str(len(labels) + 1)

                arr[2*i+1][2*j+1] = labels[self.rule[(i,j)]]

        out = '\n'.join( ''.join(row) for row in arr )

        for k, v in sorted(labels.items(), key=lambda x: x[1]):
            out += '\n' + '%s: %s' % (v, k.description)

        return out

    def __eq__(self, other):
        return type(other) is GeneratingRule and self.rule == other.rule

    def __hash__(self):
        return sum( hash((k, v)) for k, v in self.rule.items() )

