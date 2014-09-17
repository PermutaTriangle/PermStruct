
from permstruct.lib import Permutation, Permutations, choose, exact_cover, binary_search
from permstruct.permutation_sets import GeneratingRule
import random
from itertools import product

def construct_rule(permProp,
                   B,
                   n_range,
                   m_range,
                   max_nonempty,
                   max_ec_cnt,
                   inputs,
                   ignore_first=0,
                   allow_overlap_in_first=False):

    """Tries to construct a set of generating rules that together generate the
    given permutation set.

    INPUT:

    - ``permProp`` - the permutation set expressed as a boolean predicate:
      permProp(p) should return True iff the permutation p is a part of the
      permutation set.

    - ``B`` - consider only permutations of length up to B, inclusive.

    - ``n_range`` - a tuple (a, b) specifying that we should consider
      generating rules with number of rows between a and b, inclusive.

    - ``m_range`` - a tuple (a, b) specifying that we should consider
      generating rules with number of rows between a and b, inclusive.

    - ``max_nonempty`` - the maximum number of non-empty boxes in the resulting
      generating rule.

    - ``max_ec_cnt`` - the maximum number of generating rules to match
      together.

    - ``inputs`` - a list of tuples (f, g), where g is a generating rule and f
      is a boolean predicate: f(p) should return True iff the permutation p can
      be produced by g. These generating rules are possible candidates for
      boxes in the resulting generating rules.

    - ``ignore_first`` - ignore the smallest ``ignore_first`` permutations when
      doing the generating rule matching. So even if a set of generating rules
      don't produce a certain small permutation, they will still be considered.

    - ``allow_overlap_in_first`` - whether to allow overlap (that is, the same
      permutation being produced multiple times) in the ``ignore_first``
      permutations.

    Note that if performance is an issue, the parameters ``B``, ``n_range``,
    ``m_range``, ``max_nonempty``, ``max_ec_cnt`` and ``inputs`` can be tweaked
    for better performance, at the cost of lower number of results.

    This function currently doesn't return anything meaningful, but it does
    display its results to stdout.

    """


    validcnt = 0
    ball = 0
    permset = [ [] for _ in range(B+1) ]
    ocreated = {}
    for l in range(B+1):
        ocreated.setdefault(l, [])
        for perm in Permutations(l):
            if permProp(perm):
                permset[l].append(tuple(perm))
                ocreated[l].append(perm)
                ball |= 1 << validcnt
                validcnt += 1

    # pick the main permutation to work with, currently just chooses one of the
    # largest ones randomly
    # TODO: be more smart about picking the permutations to learn from (or use all of them)
    main_perms = list(permset[B])
    random.shuffle(main_perms)
    main_perms = main_perms[:10]

    ok_rules = {}
    tried_rules = set()
    for n in range(n_range[0], n_range[1] + 1):
        for m in range(m_range[0], m_range[1] + 1):
            for xsep in choose(B - 1, n - 1):
                for ysep in choose(B - 1, m - 1):
                    for main_perm in main_perms:

                        arr = [ [ [] for j in range(m) ] for i in range(n) ]

                        nonempty_cnt = 0
                        ok = True
                        for i in range(n):
                            for j in range(m):
                                for k in range(0 if j == 0 else ysep[j-1] + 1, (B - 1 if j == m - 1 else ysep[j]) + 1):
                                    if (0 if i == 0 else xsep[i-1] + 1) <= B - main_perm[k] <= (B - 1 if i == n - 1 else xsep[i]):
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
                                    for inp_prop, inp in inputs:
                                        if inp_prop(arr[i][j]):
                                            cur.append((i, j, inp))

                                    nonempty.append(cur)

                        for poss in product(*nonempty):
                            rule = GeneratingRule({ (i,j): inp for i, j, inp in poss })
                            if rule in tried_rules:
                                continue

                            tried_rules.add(rule)

                            bs = 0
                            ok = True
                            curcnt = 0
                            for l in range(B+1):
                                curlevel = []
                                for perm in rule.generate_of_length(l, ocreated):
                                    # if not permProp(perm):
                                    if not binary_search(permset[l], perm):
                                        ok = False
                                        # print('Generated something not in the set (%s)' % str(perm))
                                        break

                                    curlevel.append(perm)

                                if not ok:
                                    break

                                cur = sorted(curlevel)
                                for a,b in zip(cur, cur[1:]):
                                    if a == b:
                                        ok = False
                                        # print('Generated something more than once (%s)' % str(a))
                                        break

                                if not ok:
                                    break

                                i = 0
                                j = 0
                                while i < len(cur) and j < len(permset[l]):
                                    if permset[l][j] < cur[i]:
                                        j += 1
                                        curcnt += 1
                                    elif cur[i] == permset[l][j]:
                                        bs |= 1 << curcnt
                                        i += 1
                                        j += 1
                                        curcnt += 1
                                    else:
                                        assert False

                                assert i == len(cur)
                                curcnt += len(permset[l]) - j

                            if ok:
                                print(rule)
                                print(''.join( '0' if (bs & (1 << i)) == 0 else '1' for i in range(validcnt - 1, -1, -1) ))
                                print('')

                                ok_rules.setdefault(bs, [])
                                ok_rules[bs].append(rule)

    print('Finding exact cover...')

    bss = list(ok_rules.keys())

    used_idx = set()
    print('Found:')
    for res in exact_cover(bss, validcnt, max_ec_cnt, ignore_first, allow_overlap_in_first):
        print(', '.join(map(str, res)))
        used_idx |= set(res)

    print('')
    print('Index:')
    for i, b in enumerate(bss):
        if i not in used_idx:
            continue

        print('%3d: ' % i)
        print(''.join( '0' if (b & (1 << i)) == 0 else '1' for i in range(validcnt - 1, -1, -1) ))


        for rule in ok_rules[b]:
            print('')
            print(rule)

        print('')

    # TODO: return the results on some nice form
    return []

