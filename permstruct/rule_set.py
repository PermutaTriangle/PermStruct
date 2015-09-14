from permuta import Permutations
from permuta.misc import exact_cover, binary_search

class RuleSet:

    def __init__(self, perm_prop, perm_bound):
        self.perm_prop = perm_prop
        self.perm_bound = perm_bound
        self.rules = {}

        self.death_by_overlap = 0
        self.death_by_perm_prop = 0

        # some preprocessing: cache all permutations of length at most
        # perm_bound that satisfy perm_prop
        self.validcnt = 0
        self.ball = 0
        self.permset = [ [] for _ in range(self.perm_bound+1) ]
        self.ocreated = {}
        for l in range(self.perm_bound+1):
            self.ocreated.setdefault(l, [])
            for perm in Permutations(l):
                if self.perm_prop(perm):
                    self.permset[l].append(tuple(perm))
                    self.ocreated[l].append(perm)
                    self.ball |= 1 << self.validcnt
                    self.validcnt += 1

    def print_stats(self):
        print('Death by overlap: ', self.death_by_overlap)
        print('Death by perm prop: ', self.death_by_perm_prop)


    def add_rule(self, rule):

        bs = 0
        curcnt = 0
        empty = True
        for l in range(self.perm_bound+1):
            curlevel = []
            for perm in rule.generate_of_length(l, self.ocreated):
                # if not self.perm_prop(perm):
                if not binary_search(self.permset[l], perm):
                    # the rule generated something that doesn't satisfy perm_prop
                    self.death_by_perm_prop += 1
                    return False

                curlevel.append(perm)

            cur = sorted(curlevel)
            for a,b in zip(cur, cur[1:]):
                if a == b:
                    # the rule generated something more than once (i.e. there is overlap)
                    self.death_by_overlap += 1
                    return False

            i = 0
            j = 0
            while i < len(cur) and j < len(self.permset[l]):
                if self.permset[l][j] < cur[i]:
                    j += 1
                    curcnt += 1
                elif cur[i] == self.permset[l][j]:
                    bs |= 1 << curcnt
                    i += 1
                    j += 1
                    curcnt += 1
                    empty = False
                else:
                    assert False

            assert i == len(cur)
            curcnt += len(self.permset[l]) - j

        if empty:
            return

        print(rule)
        print(''.join( '0' if (bs & (1 << i)) == 0 else '1' for i in range(self.validcnt - 1, -1, -1) ))
        print('')

        self.rules.setdefault(bs, [])
        self.rules[bs].append(rule)

    def exact_cover(self,
                max_ec_cnt,
                ignore_first=1,
                allow_overlap_in_first=True,
            ):

        print('Finding exact cover...')

        bss = list(self.rules.keys())

        used_idx = set()
        print('Found:')
        for res in exact_cover(bss, self.validcnt, max_ec_cnt, ignore_first, allow_overlap_in_first):
            print(', '.join(map(str, res)))
            used_idx |= set(res)

        print('')
        print('Index:')
        for i, b in enumerate(bss):
            if i not in used_idx:
                continue

            print('%3d: ' % i)
            print(''.join( '0' if (b & (1 << i)) == 0 else '1' for i in range(self.validcnt - 1, -1, -1) ))

            cnt = 0
            mx_cnt = 15
            for rule in self.rules[b]:
                if cnt == mx_cnt:
                    print('')
                    print('(and %d more)' % (len(self.rules[b]) - mx_cnt))
                    break

                print('')
                print(rule)
                cnt += 1

            print('')

        # TODO: return the results on some nice form
        return []

