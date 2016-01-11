
from permstruct import RuleSet
from permuta import Permutation, Permutations
from permuta.misc import choose
from permstruct.permutation_sets import GeneratingRule
import random
from itertools import product

def construct_rule(perm_prop,
                   perm_bound,
                   dag,
                   max_rule_size,
                   max_nonempty,
                   max_rules,

                   ignore_first=1,
                   allow_overlap_in_first=True):

    """Tries to construct a set of generating rules that together generate the
    given permutation set.

    INPUT:

    - ``perm_prop`` - the permutation set expressed as a boolean predicate:
      perm_prop(p) should return True iff the permutation p is a part of the
      permutation set.

    - ``perm_bound`` - consider only permutations of length up to perm_bound, inclusive.

    - ``max_rule_size`` - a tuple (n, m) specifying that we should consider
      generating rules with at most n rows and at most m columns.

    - ``max_nonempty`` - the maximum number of non-empty boxes in the resulting
      generating rule.

    - ``max_rules`` - the maximum number of generating rules to match
      together.

    - ``dag`` - a list of tuples (f, g), where g is a generating rule and f
      is a boolean predicate: f(p) should return True iff the permutation p can
      be produced by g. These generating rules are possible candidates for
      boxes in the resulting generating rules.

    - ``ignore_first`` - ignore the smallest ``ignore_first`` permutations when
      doing the generating rule matching. So even if a set of generating rules
      don't produce a certain small permutation, they will still be considered.

    - ``allow_overlap_in_first`` - whether to allow overlap (that is, the same
      permutation being produced multiple times) in the ``ignore_first``
      permutations.

    Note that if performance is an issue, the parameters ``perm_bound``, ``max_rule_size``,
    ``max_nonempty``, ``max_rules`` and ``dag`` can be tweaked
    for better performance, at the cost of lower number of results.

    This function currently doesn't return anything meaningful, but it does
    display its results to stdout.

    """


    main_perms = []
    for perm in Permutations(perm_bound):
        if perm_prop(perm):
            main_perms.append(tuple(perm))

    # pick the main permutation to work with, currently just chooses one of the
    # largest ones randomly
    # TODO: be more smart about picking the permutations to learn from (or use all of them)
    random.shuffle(main_perms)
    main_perms = main_perms[:50]
    # main_perm = [ Permutation([1,2,3,4,5,6]) ]

    rules = RuleSet(perm_prop, perm_bound)
    tried_rules = set()
    for n in range(1, max_rule_size[0] + 1):
        for m in range(1, max_rule_size[1] + 1):
            for xsep in choose(perm_bound - 1, n - 1):
                for ysep in choose(perm_bound - 1, m - 1):
                    for main_perm in main_perms:

                        arr = [ [ [] for j in range(m) ] for i in range(n) ]

                        nonempty_cnt = 0
                        ok = True
                        for i in range(n):
                            for j in range(m):
                                for k in range(0 if j == 0 else ysep[j-1] + 1, (perm_bound - 1 if j == m - 1 else ysep[j]) + 1):
                                    if (0 if i == 0 else xsep[i-1] + 1) <= perm_bound - main_perm[k] <= (perm_bound - 1 if i == n - 1 else xsep[i]):
                                        arr[i][j].append(main_perm[k])

                                if arr[i][j]:
                                    nonempty_cnt += 1
                                    if nonempty_cnt > max_nonempty:
                                        ok = False
                                        break

                            if not ok:
                                break

                        if not ok:
                            continue


                        nonempty = []
                        for i in range(n):
                            for j in range(m):
                                if arr[i][j]:
                                    arr[i][j] = Permutation.to_standard(arr[i][j])
                                    cur = []
                                    # for inp_prop, inp in dag.elements:
                                    for inp in dag.elements:
                                        if inp is None:
                                            continue

                                        if inp.contains(arr[i][j]):
                                            cur.append((i, j, inp))

                                    nonempty.append(cur)



                        for poss in product(*nonempty):
                            rule = GeneratingRule({ (i,j): inp for i, j, inp in poss })
                            if rule in tried_rules:
                                continue

                            # print(rule)

                            tried_rules.add(rule)
                            rules.add_rule(rule)

    print('Found %d rules, %d of which are valid, %d of which are distinct' % (
            len(tried_rules),
            sum( len(v) for k, v in rules.rules.items() ),
            len(rules.rules),
        ))

    return rules.exact_cover(
            max_rules,
            ignore_first,
            allow_overlap_in_first,
        )

