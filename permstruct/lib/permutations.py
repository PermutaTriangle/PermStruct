
from .dancing_links import DancingLinks

class Permutation(object):
    def __init__(self, perm, check=False):

        if check:
            assert type(perm) is list
            n = len(perm)
            used = [False]*n

            for x in perm:
                assert type(x) is int
                assert 1 <= x <= n
                assert not used[x-1]
                used[x-1] = True

        self.perm = list(perm)

    def contains(self, pattern):
        def con(i, now):
            if len(now) == len(pattern):
                return True

            if i == len(self):
                return False

            nxt = now + [self[i]]
            # TODO: make this faster by incrementally building the flattened list
            if Permutation.to_standard(nxt) == Permutation.to_standard(pattern[:len(nxt)]):
                if con(i+1, nxt):
                    return True

            return con(i+1, now)

        return con(0, [])

    def avoids(self, pattern):
        return not self.contains(pattern)

    def inverse(self):
        n = len(self)
        res = [None]*n
        for i in range(n):
            res[self.perm[i]-1] = i+1
        return Permutation(res)

    @staticmethod
    def to_standard(lst):
        n = len(lst)
        res = [None]*n
        for j, (x, i) in enumerate(sorted( (lst[i], i) for i in range(n) )):
            res[i] = j+1

        return Permutation(res)

    def __call__(self, lst):
        assert len(lst) == len(self)

        n = len(self)
        res = [None]*n
        for i in range(n):
            res[i] = lst[self.perm[i] - 1]

        return res

    def __getitem__(self, i):
        return self.perm[i]

    def __len__(self):
        return len(self.perm)

    def __iter__(self):
        return iter(self.perm)

    def __str__(self):
        return str(self.perm)

    def __repr__(self):
        return 'Permutation(%s)' % repr(self.perm)

    def __eq__(self, other):
        return type(other) is Permutation and self.perm == other.perm

    def __lt__(self, other):
        return len(self) < len(other) and self.perm < other.perm

    def __hash__(self):
        res = 27
        for x in self.perm:
            res = res * 31 + x
        return res

class Permutations(object):
    def __init__(self, n):
        assert 0 <= n
        self.n = n

    def __iter__(self):

        left = DancingLinks(range(1, self.n+1))
        res = []
        def gen():
            if len(left) == 0:
                yield Permutation(list(res))
            else:
                cur = left.front
                while cur is not None:
                    left.erase(cur)
                    res.append(cur.value)
                    for p in gen():
                        yield p
                    res.pop()
                    left.restore(cur)
                    cur = cur.next

        return gen()

    def __str__(self):
        return 'The set of Permutations of length %d' % self.n

    def __repr__(self):
        return 'Permutations(%d)' % self.n

