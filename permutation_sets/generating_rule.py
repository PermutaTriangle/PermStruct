
from sage.combinat.permutation import Permutation
from sage.misc.flatten import flatten
from sage.combinat.set_partition_ordered import OrderedSetPartitions
from permutation_set import PermutationSet
from static_permutation_set import StaticPermutationSet
from point import Point
from itertools import product

class GeneratingRule(PermutationSet):
    """A permutation set containing all permutations generated by a generating
    rule."""

    def __init__(self, rule):

        if type(rule) is list:
            self.rule = { (i,j): rule[i][j] for i in range(len(rule)) for j in range(len(rule[i])) if rule[i][j] is not None }
        else:
            self.rule = rule


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
        h = max( k[0] for k,v in rule ) + 1
        w = max( k[1] for k,v in rule ) + 1

        def count_assignments(at, left):

            if at == len(rule):
                if left == 0:
                    yield []
            elif type(rule[at][1]) is Point:
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

                arr = [ [ Permutation([]) for j in range(w) ] for i in range(h) ]

                for i, perm in enumerate(perm_ass):
                    arr[rule[i][0][0]][rule[i][0][1]] = perm

                # TODO: The following conversion to a permutation doesn't work
                # when there are many permutations in a column

                def permute(arr, perm):
                    res = [None] * len(arr)
                    for i in range(len(arr)):
                        res[i] = arr[perm[i] - 1]
                    return res

                def gen(i):
                    if i == h:
                        yield [ [] for _ in range(w) ]
                    else:
                        cnt = sum( len(arr[i][j]) for j in range(w) )

                        for part in OrderedSetPartitions(list(range(1,cnt+1)), [ len(arr[i][j]) for j in range(w) ]):
                            for tres in gen(i+1):
                                res = list(tres)
                                cumul = sum( len(r) for r in res )
                                for j in range(w):
                                    if arr[i][j]:
                                        res[j] = permute([ x + cumul for x in sorted(part[j]) ], arr[i][j])

                                yield res


                for perm in gen(0):
                    yield Permutation(flatten(perm))


                # perm = [None]*w
                # cumul = 0
                # for i in range(h-1, -1, -1):
                #     for j in range(w):
                #         if arr[i][j] is not None:
                #             perm[j] = [ x + cumul for x in arr[i][j] ]
                #             cumul += len(arr[i][j])
                # yield Permutation(flatten(perm))


    def to_static(self, max_n, input):

        inp = dict(input)

        for n in range(max_n+1):
            for perm in self.generate_of_length(n, inp):
                inp.setdefault(n, [])
                inp[n].append(perm)

        try:
            gf = self.generating_function()
        except NotImplementedError:
            gf = None

        perms = [ p for ps in inp.values() for p in ps ]
        return StaticPermutationSet(perms, gf)

