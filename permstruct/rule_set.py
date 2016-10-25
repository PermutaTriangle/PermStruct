from __future__ import print_function
from permuta import Permutations, Permutation
from permuta.misc import exact_cover, exact_cover_smallest, binary_search
from permstruct.exact_cover import exact_cover_lb, exact_cover as ps_exact_cover
from permstruct.functions import verify_cover, RuleDeath
import sys

class RuleSet:

    def __init__(self, settings):
        self.settings = settings
        self.rules = {}
        self.death_by_overlap = 0
        self.death_by_perm_prop = 0
        self.ball = (1<<settings.sinput.validcnt)-1
        self.permset = [ sorted(settings.sinput.permutations[l]) for l in range(settings.perm_bound+1) ]
        self.total_rules = 0

        # self.seen = set()

    def print_stats(self):
        self.settings.logger.log('Death by overlap: %s' % self.death_by_overlap)
        self.settings.logger.log('Death by perm prop: %s' % self.death_by_perm_prop)

    def add_rule(self, rule):
        self.total_rules += 1
        bs = 0
        curcnt = 0
        empty = True
        for l in range(self.settings.perm_bound+1):
            curlevel = []
            for perm in rule.generate_of_length(l, self.settings.sinput.permutations):
                if not self.settings.sinput.contains(perm):
                    # the rule generated something that doesn't satisfy perm_prop
                    self.death_by_perm_prop += 1
                    return RuleDeath.PERM_PROP

                curlevel.append(perm)

            cur = sorted(curlevel)
            for a,b in zip(cur, cur[1:]):
                if a == b:
                    # the rule generated something more than once (i.e. there is overlap)
                    self.death_by_overlap += 1
                    return RuleDeath.OVERLAP

            i = 0
            j = 0
            while i < len(cur) and j < len(self.permset[l]):
                if self.permset[l][j] < Permutation(cur[i]):
                    j += 1
                    curcnt += 1
                elif Permutation(cur[i]) == self.permset[l][j]:
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
            assert False

        self.rules.setdefault(bs, [])
        self.rules[bs].append(rule)
        return RuleDeath.ALIVE

    def exact_cover(self,
                max_ec_cnt=None,
                allow_overlap_in_first=True,
                dag_elems_id=None,
            ):

        self.settings.logger.log('Finding exact cover...')

        bss = list(self.rules.keys())

        used_idx = set()
        self.settings.logger.log('Found:')
        if self.settings.lower_bound is None:
            covers = ps_exact_cover(self.settings, bss)
        else:
            covers = exact_cover_lb(self.settings, bss)

        covers = list(covers)
        for res in covers:
            print(repr(res))
            used_idx |= set(res)

        print('')
        self.settings.logger.log('Index:')
        for i, b in enumerate(bss):
            if i not in used_idx:
                continue

            if True or dag_elems_id is None:
                print('%3d: ' % i)
                print(''.join( '0' if (b & (1 << i)) == 0 else '1' for i in range(self.settings.sinput.validcnt - 1, -1, -1) ))

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
            else:
                print(i)

                for rule in self.rules[b]:
                    print(repr({ k:dag_elems_id[v] for k,v in rule.rule.items() }))

                print('')

        if self.settings.verify_bound is not None:
            # TODO: ask if we should verify a bit higher
            for res in covers:
                self.settings.logger.log('Verifying cover %s up to length %d' % (res, self.settings.verify_bound))
                cover = []
                warned = False
                for bi in res:
                    b = bss[bi]
                    if len(self.rules[b]) > 1 and not warned:
                        warned = True
                        self.settings.logger.warn('Multiple covers, but only using one for verification')
                    cover.append(self.rules[b][0])

                status = verify_cover(self.settings, cover)
                if status == RuleDeath.PERM_PROP:
                    self.settings.logger.error('Death by perm prop!!!!!!!!!!!!!')
                elif status == RuleDeath.OVERLAP:
                    self.settings.logger.error('Death by overlap!!!!!!!!!!!!!')
                elif status == RuleDeath.ALIVE:
                    self.settings.logger.log('Cover verified')

        # TODO: return the results on some nice form
        return []

