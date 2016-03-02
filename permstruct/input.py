from permuta import AvoidanceClass, Permutation
import datetime

class StructInput(object):

    def __init__(self, settings, perm_prop, generator, is_classical=False, avoidance=None):
        self.settings = settings
        self.perm_prop = perm_prop
        self.generator = generator
        self.is_classical = is_classical
        self.avoidance = avoidance
        self._compile()

    @staticmethod
    def from_perm_prop(settings, perm_prop, generator=None, is_classical=False, avoidance=None):
        if generator is None:
            # TODO: make a faster version for is_classical=True
            def gen(n):
                for p in Permutations(n):
                    if perm_prop(p):
                        yield p
            generator = gen
        return StructInput(settings, perm_prop, generator, is_classical=is_classical, avoidance=avoidance)

    @staticmethod
    def from_avoidance(settings, patterns):
        assert all( type(p) is Permutation for p in patterns )

        def gen(n):
            for p in AvoidanceClass(n, avoiding=patterns):
                yield p

        return StructInput.from_perm_prop(settings, lambda p: p.avoids(patterns), generator=gen, is_classical=True, avoidance=patterns)

    def _compile(self):
        self.settings.logger.log('Generating permutations from input')
        started = datetime.datetime.now()

        self.validcnt = 0
        self.permutations = {}
        upto = self.settings.verify_bound
        for l in range(upto+1):
            self.permutations[l] = set([])
            for perm in self.generator(l):
                self.permutations[l].add(perm)
                if l <= self.settings.perm_bound:
                    self.validcnt += 1

        ended = datetime.datetime.now()
        self.settings.logger.log('Finished in %.3fs' % (ended - started).total_seconds())
        self.settings.logger.log('Enumeration is %s' % [ len(self.permutations[l]) for l in range(upto+1) ])
        assert self.settings.ignore_first < self.validcnt, "All permutations from the set are ignored"

    def contains(self, perm):
        if type(perm) is not Permutation:
            perm = Permutation(list(perm))
        return perm in self.permutations[len(perm)]

    def count_of_length(self, l):
        return len(self.permutations[l])

    def get_permutations(self):
        # XXX: should we return a deep copy?
        return self.permutations

    def get_permutation_set(self):
        return set([ p for ps in self.permutations.values() for p in ps ])

