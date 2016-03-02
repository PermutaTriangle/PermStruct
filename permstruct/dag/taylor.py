from permuta import Permutation, Permutations, AvoidanceClass
from permuta.misc import choose, subsets
from permstruct import E, N, P, X
from permstruct.permutation_sets import InputPermutationSet, StaticPermutationSet
from permstruct.dag import DAG
import datetime

# def taylor_dag(patterns, perm_bound, max_len_patt=None, upper_bound=None, remove=True):
def taylor_dag(settings, max_len_patt=None, upper_bound=None, remove=True):
    assert settings.sinput.avoidance is not None, "Tayloring is only supported for avoidance"
    patterns = settings.sinput.avoidance

    if max_len_patt is None:
        max_len_patt = max( len(p) for p in patterns )

    started = datetime.datetime.now()
    settings.logger.log('Tayloring DAG')

    n = max( len(p) for p in patterns )
    # sub = [ [ set([]) for i in range(n+1) ] for _ in range(len(patterns)) ]
    sub = [ set([]) for _ in range(len(patterns)) ]
    for i,p in enumerate(patterns):
        last = set([ p ])
        if len(p) <= max_len_patt:
            sub[i] |= last
        for l in range(len(p)-1, 1, -1):
            nxt = set([])
            for q in last:
                for j in range(len(q)):
                    qp = Permutation([ x-1 if x>q[j] else x for x in q[:j] + q[j+1:] ])

                    nxt.add(qp)
            if l <= max_len_patt:
                sub[i] |= nxt
            last = nxt

    def can_add(add, picked):
        for p in picked:
            if len(p) > len(add) and p.contains(add):
                return False
            if len(add) > len(p) and add.contains(p):
                return False
        return True

    def bt(at,picked,seen):
        if upper_bound is not None and len(picked) > upper_bound:
            pass
        elif picked == set(patterns):
            pass
        elif at == len(patterns):
            yield picked
        else:
            for s in subsets(list(sub[at] - picked - seen)):
                npicked = set(picked)
                ok = True
                for add in set(s):
                    if not can_add(add, npicked):
                        ok = False
                        break
                    npicked.add(add)
                if not ok or not (npicked & sub[at]):
                    continue

                for res in bt(at+1,npicked,seen | sub[at]):
                    yield res

    elems = []
    for ps in bt(0,set(),set()):

        here = set()
        for perm in AvoidanceClass(settings.verify_bound, avoiding=ps, upto=True):
            here.add(perm)

        descr = 'Av(%s)' % ', '.join(map(str, sorted(ps)))
        elems.append((ps, here, descr))

    input = settings.sinput.get_permutation_set()
    elems.append((InputPermutationSet(settings), input, None))
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

    ended = datetime.datetime.now()
    settings.logger.log('Finished in %.3fs' % (ended - started).total_seconds())
    return res

