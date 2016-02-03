from permuta import Permutation, Permutations
from permuta.misc import choose, subsets
from permstruct import E, N, P, X
from permstruct.permutation_sets import InputPermutationSet, StaticPermutationSet
from permstruct.dag import DAG

# TODO: support outputting tuples of patterns of different length
def taylor_dag(patterns, perm_bound, max_len_patt=None, upper_bound=None, remove=True):
    if max_len_patt is None:
        max_len_patt = max( len(p) for p in patterns )

    n = max( len(p) for p in patterns )
    # sub = [ [ set([]) for i in range(n+1) ] for _ in range(len(patterns)) ]
    sub = [ set([]) for _ in range(len(patterns)) ]
    for i,p in enumerate(patterns):
        last = set([ p ])
        sub[i] |= last
        for l in range(len(p)-1, 1, -1):
            nxt = set([])
            for q in last:
                for j in range(len(q)):
                    qp = Permutation.to_standard(q[:j] + q[j+1:]) # TODO: could do this in linear time
                    nxt.add(qp)
            sub[i] |= nxt
            last = nxt

        # sub[i][len(p)].add(p)

    # for l in range(n,2,-1):
    #     for i,p in enumerate(patterns):
    #         for q in sub[i][l]:
    #             for j in range(len(q)):
    #                 qp = Permutation.to_standard(q[:j] + q[j+1:]) # TODO: could do this in linear time
    #                 sub[i][l-1].add(qp)

    def valid(picked):
        picked = sorted(picked, key=lambda x: len(x))

        for i in range(len(picked)):
            for j in range(i+1,len(picked)):
                if picked[j].contains(picked[i]):
                    return False

                # if p != q and p.contains(q):
                #     return False

        # ps = {}
        # for p in picked:
        #     ps.setdefault(len(p), [])
        #     ps[len(p)].append(p)
        #
        # its = sorted(ps.items())
        # for (l1,ps1),(l2,ps2) in zip(its, its[1:]):
        #     for q in ps2:
        #         for p in ps1:
        #             if q.contains(p):
        #                 return False
        return True

    def bt(at,picked,seen):
        if upper_bound is not None and len(picked) > upper_bound:
            pass
        elif not valid(picked):
            pass
        elif at == len(patterns):
            yield picked
        else:
            for s in subsets(list(sub[at] - picked - seen)):
                npicked = picked | set(s)
                if not (npicked & sub[at]):
                    continue
                for res in bt(at+1,npicked,seen | sub[at]):
                    yield res

    elems = []
    for ps in bt(0,set(),set()):

        here = set()
        for m in range(perm_bound+1):
            for perm in Permutations(m):
                if all( perm.avoids(p) for p in ps ):
                    here.add(perm)

        descr = 'Av(%s)' % ', '.join(map(str, sorted(ps)))
        elems.append((ps, here, descr))

    perm_prop = lambda p: all( p.avoids(q) for q in patterns )
    input = set( p for l in range(perm_bound+1) for p in Permutations(l) if perm_prop(p) )
    elems.append((InputPermutationSet(perm_prop), input, None))
    elems.append((N, set([ Permutation([]) ]), None))
    elems.append((P, set([ Permutation([1]) ]), None))

    res = DAG()
    if remove:
        for ps,here,descr in elems:
            rem = set()
            remdescr = ''
            for qs,other,odescr in elems:
                # if other and qs is not None and other < here:
                if other and other < here:
                    rem |= other
                    remdescr += ' - ' + (odescr if odescr is not None else 'empty permutation' if qs is None else qs.description)

            if not here-rem:
                continue

            if descr is not None:
                ps = StaticPermutationSet(here-rem, description=descr + remdescr)
            if type(ps) is InputPermutationSet:
                ps = StaticPermutationSet(here-rem, description=ps.description + remdescr, alone_ok=False)
            # if ps is not None:

            res.add_element(ps)
    else:
        for ps,here,descr in elems:
            if descr is not None:
                ps = StaticPermutationSet(here, description=descr)
            res.add_element(ps)

    return res

if __name__ == '__main__':
    res = taylor_dag([
        Permutation([3,2,1]),
        Permutation([1,3,2,4]),
        Permutation([3,4,1,2]),
    ], 7, upper_bound=3)

    for el in res.elements:
        print(el.description if el is not None else None)

