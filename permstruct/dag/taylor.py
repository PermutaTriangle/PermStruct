from permuta import Permutation, Permutations
from permuta.misc import choose, subsets
from permstruct import E, N, P, X
from permstruct.permutation_sets import InputPermutationSet, StaticPermutationSet
from permstruct.dag import DAG

# TODO: support outputting tuples of patterns of different length
def taylor_dag(patterns, perm_bound, max_len_patt=None, upper_bound=None, remove=True):
    if max_len_patt is None:
        max_len_patt = max( len(p) for p in patterns ) - 1

    n = max( len(p) for p in patterns )
    sub = [ [ set([]) for i in range(n+1) ] for _ in range(len(patterns)) ]
    for i,p in enumerate(patterns):
        sub[i][len(p)].add(p)

    for l in range(n,2,-1):
        for i,p in enumerate(patterns):
            for q in sub[i][l]:
                for j in range(len(q)):
                    qp = Permutation.to_standard(q[:j] + q[j+1:]) # TODO: could do this in linear time
                    sub[i][l-1].add(qp)

    def bt(l,at,picked,seen):
        if upper_bound is not None and len(picked) > upper_bound:
            pass
        elif at == len(patterns):
            yield picked
        else:
            for s in subsets(list(sub[at][l] - picked - seen)):
                npicked = picked | set(s)
                if not (npicked & sub[at][l]):
                    continue
                for res in bt(l,at+1,npicked,seen | sub[at][l]):
                    yield res

    elems = []
    for l in range(2,max_len_patt+1):
        for ps in bt(l,0,set(),set()):

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
                if other and qs is not None and other < here:
                    rem |= other
                    remdescr += ' - ' + (odescr if odescr is not None else qs.description)

            if descr is not None:
                ps = StaticPermutationSet(here-rem, description=descr)
            if ps is not None:
                ps.description += remdescr

            res.add_element(ps)
    else:
        for ps,here,descr in elems:
            if descr is not None:
                ps = StaticPermutationSet(here, description=descr)
            res.add_element(ps)

    return res

# res = taylor_dag([
#     Permutation([1,3,2]),
#     Permutation([4,3,2,1]),
# ], 5, remove=False)
#
# for el in res.elements:
#     print(el.description if el is not None else None)
