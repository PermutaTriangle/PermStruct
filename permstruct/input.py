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

    def get_permutations(self, upto=None):
        if upto is not None:
            raise NotImplemented()
        # XXX: should we return a deep copy?
        return self.permutations

    def get_permutation_set(self):
        return set([ p for ps in self.permutations.values() for p in ps ])


class AvoiderInput(StructInput):

    def __init__(self, settings, patterns):
        assert all( type(p) is Permutation for p in patterns )
        self.settings = settings
        self.is_classical = True
        self.avoidance = patterns

        self._compile()

    def _compile(self):
        self.settings.logger.log('Generating permutations from input')
        started = datetime.datetime.now()

        self.permutations = {}
        self._assure_length(self.settings.perm_bound)
        self.validcnt = sum( len(self.permutations[l]) for l in range(self.settings.perm_bound+1) )

        ended = datetime.datetime.now()
        self.settings.logger.log('Finished in %.3fs' % (ended - started).total_seconds())
        self.settings.logger.log('Enumeration is %s' % [ len(self.permutations[l]) for l in range(self.settings.perm_bound+1) ])
        assert self.settings.ignore_first < self.validcnt, "All permutations from the set are ignored"

    def _assure_length(self, l):
        if l in self.permutations:
            return
        if l == 0:
            self.permutations[0] = [ Permutation([]) ]
        else:
            self._assure_length(l-1)
            here = set()
            for p in self.permutations[l-1]:
                for i in range(l):
                    q = Permutation(p[:i] + [l] + p[i:])
                    if q.avoids(self.avoidance):
                        here.add(q)
            self.permutations[l] = list(here)

    def contains(self, perm):
        if type(perm) is not Permutation:
            perm = Permutation(list(perm))
        self._assure_length(len(perm))
        return perm in self.permutations[len(perm)]

    def count_of_length(self, l):
        self._assure_length(l)
        return len(self.permutations[l])

    def get_permutations(self, upto=None):
        # XXX: should we return a deep copy?
        if upto is not None:
            self._assure_length(upto)
            return { k:self.permutations[k] for k in range(upto+1) }
        else:
            return self.permutations

    def get_permutation_set(self):
        # XXX: should there be an upto paramater?
        return set([ p for ps in self.permutations.values() for p in ps ])

