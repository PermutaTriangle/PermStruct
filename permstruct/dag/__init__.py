from permstruct import E, N, P, X
from permstruct.permutation_sets import InputPermutationSet
from permuta import Permutations
from permstruct.permutation_sets.units import *

from .dag import DAG

def x_dag(perm_prop, n):
    dag = DAG()
    dag.add_element(InputPermutationSet(perm_prop))
    return dag

def decr_dag(perm_prop, n):
    dag = elementary(perm_prop, n)
    d = decr(n)
    dag.add_element(d)
    dag.put_below(N, d)
    dag.put_below(P, d)
    return dag

def elementary(perm_prop, n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)
    dag.add_element(InputPermutationSet(perm_prop))
    return dag

def elementary_X_minus_epsilon(perm_prop, n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)

    X_minus_epsilon = i = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and perm_prop(x)), n, description='X - epsilon')
    dag.add_element(X_minus_epsilon)
    return dag

def elementary_X_len2(perm_prop, n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)

    X_len2 = i = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and perm_prop(x)), n, description='X > 2')
    dag.add_element(X_minus_epsilon)
    return dag

def N_P(n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)
    return dag

def N_P_incr(n):
    dag = N_P(n)
    dag.add_element(incr(n))
    return dag

def N_P_incr1(n):
    dag = N_P(n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids([2,1])), n, description='incr > 0')
    dag.add_element(i)
    return dag

def N_P_incr2(n):
    dag = N_P(n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([2,1])), n, description='incr > 1')
    dag.add_element(i)
    return dag

def N_P_X(perm_prop, n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)
    dag.add_element(InputPermutationSet(perm_prop))
    return dag

def N_P_X1(perm_prop, n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)

    X1 = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and perm_prop(x)), n, description='X > 0')
    dag.add_element(X1)
    return dag

def N_P_X2(perm_prop, n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)

    X2 = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and perm_prop(x)), n, description='X > 1')
    dag.add_element(X2)
    return dag

def N_P_X3_mon2(perm_prop, n):
    dag = DAG()
    dag.add_element(N)
    dag.add_element(P)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([2,1])), n, description='incr > 1')
    dag.add_element(i)

    X3 = StaticPermutationSet.from_predicate((lambda x: len(x) > 2 and perm_prop(x)), n, description='X > 2')
    dag.add_element(X3)
    return dag

def incr_decr(perm_prop, n):
    dag = elementary(perm_prop, n)
    i = incr(n)
    d = decr(n)
    dag.add_element(i)
    dag.add_element(d)
    dag.put_below(N, i)
    dag.put_below(P, i)
    dag.put_below(N, d)
    dag.put_below(P, d)
    return dag

def incr_decr_nonempty(perm_prop, n):
    dag = elementary(perm_prop, n)
    i = incr_nonempty(n)
    d = decr_nonempty(n)
    dag.add_element(i)
    dag.add_element(d)
    dag.put_below(P, i)
    dag.put_below(P, d)
    return dag

def incr_decr_nonempty_X_minus_epsilon(perm_prop, n):
    dag = elementary_X_minus_epsilon(perm_prop, n)
    i = incr_nonempty(n)
    d = decr_nonempty(n)
    dag.add_element(i)
    dag.add_element(d)
    dag.put_below(P, i)
    dag.put_below(P, d)
    return dag

def N_P_X_mon(perm_prop, n):
    dag = N_P_X(perm_prop, n)

    i = incr(n)
    d = decr(n)

    dag.add_element(i)
    dag.add_element(d)
    return dag

def N_P_X_mon1(perm_prop, n):
    dag = N_P_X(perm_prop, n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids([2,1])), n, description='incr > 0')
    d = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids([1,2])), n, description='decr > 0')

    dag.add_element(i)
    dag.add_element(d)
    return dag

def N_P_X_mon2(perm_prop, n):
    dag = N_P_X(perm_prop, n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([2,1])), n, description='incr > 1')
    d = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([1,2])), n, description='decr > 1')

    dag.add_element(i)
    dag.add_element(d)
    return dag

def N_P_X1_mon(perm_prop, n):
    dag = N_P_X1(perm_prop, n)

    i = incr(n)
    d = decr(n)

    dag.add_element(i)
    dag.add_element(d)
    return dag

def N_P_X1_mon1(perm_prop, n):
    dag = N_P_X1(perm_prop, n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids([2,1])), n, description='incr > 0')
    d = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids([1,2])), n, description='decr > 0')

    dag.add_element(i)
    dag.add_element(d)
    return dag

def N_P_X1_mon2(perm_prop, n):
    dag = N_P_X2(perm_prop, n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids([2,1])), n, description='incr > 0')
    d = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids([1,2])), n, description='decr > 0')

    dag.add_element(i)
    dag.add_element(d)
    return dag

def N_P_X2_mon2(perm_prop, n):
    dag = N_P_X2(perm_prop, n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([2,1])), n, description='incr > 1')
    d = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([1,2])), n, description='decr > 1')

    dag.add_element(i)
    dag.add_element(d)
    return dag

def classic_avoiders_length_3(perm_prop, n):
    dag = N_P_X2_mon2(perm_prop, n)

    for p in Permutations(3):

        has_incr = Permutation([1,2,3]).avoids(p)
        has_decr = Permutation([3,2,1]).avoids(p)

        if has_incr and has_decr:
            pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p)), n, description='Av(%s)-incr-decr' % (p))
        elif has_incr:
            pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([2,1]) and x.avoids(p)), n, description='Av(%s)-incr' % (p))
        elif has_decr:
            pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and x.avoids(p)), n, description='Av(%s)-decr' % (p))
        else:
            pset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p)), n, description='Av(%s)' % (p))

        # pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
        # pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
        if any( len(pset.perms[l]) > 0 for l in pset.perms ):
            dag.add_element(pset)

    # av123 = classical_avoiders(Permutation([1,2,3]), n)
    # av132 = classical_avoiders(Permutation([1,3,2]), n)
    # av213 = classical_avoiders(Permutation([2,1,3]), n)
    # av231 = classical_avoiders(Permutation([2,3,1]), n)
    # av312 = classical_avoiders(Permutation([3,1,2]), n)
    # av321 = classical_avoiders(Permutation([3,2,1]), n)

    # dag.add_element(av123)
    # dag.add_element(av132)
    # dag.add_element(av213)
    # dag.add_element(av231)
    # dag.add_element(av312)
    # dag.add_element(av321)

    # dag.put_below(d, av123)
    # dag.put_below(d, av132)
    # dag.put_below(d, av213)
    # dag.put_below(d, av231)
    # dag.put_below(d, av312)

    # dag.put_below(i, av132)
    # dag.put_below(i, av213)
    # dag.put_below(i, av231)
    # dag.put_below(i, av312)
    # dag.put_below(i, av321)

    return dag

def classic_avoiders_length_3_with_input_without_incrdecr(perm_prop, n):
    dag = elementary(perm_prop, n)
    i = incr_nonempty(n)
    d = decr_nonempty(n)
    dag.add_element(i)
    dag.add_element(d)
    dag.put_below(N, i)
    dag.put_below(P, i)
    dag.put_below(N, d)
    dag.put_below(P, d)

    av123 = classical_avoiders(Permutation([1,2,3]), n)
    av132 = classical_avoiders(Permutation([1,3,2]), n)
    av213 = classical_avoiders(Permutation([2,1,3]), n)
    av231 = classical_avoiders(Permutation([2,3,1]), n)
    av312 = classical_avoiders(Permutation([3,1,2]), n)
    av321 = classical_avoiders(Permutation([3,2,1]), n)

    dag.add_element(av123)
    dag.add_element(av132)
    dag.add_element(av213)
    dag.add_element(av231)
    dag.add_element(av312)
    dag.add_element(av321)

    dag.put_below(d, av123)
    dag.put_below(d, av132)
    dag.put_below(d, av213)
    dag.put_below(d, av231)
    dag.put_below(d, av312)

    dag.put_below(i, av132)
    dag.put_below(i, av213)
    dag.put_below(i, av231)
    dag.put_below(i, av312)
    dag.put_below(i, av321)

    # inp_wo_incr = input_without_incr(perm_prop, n)
    # inp_wo_decr = input_without_decr(perm_prop, n)
    # dag.add_element(inp_wo_incr)
    # dag.add_element(inp_wo_decr)
    # TODO: put X below inp_wo_{incr,decr}

    # av321_132 = classical_avoiders_2(Permutation([3,2,1]), Permutation([1,3,2]), n)
    # av321_132 = classical_avoiders_2_nonempty(Permutation([3,2,1]), Permutation([1,3,2]), n)
    # dag.add_element(av321_132)

    av321_132_minus_incr = from_predicate((lambda p: p.avoids([1,3,2]) and p.avoids([3,2,1]) and not p.avoids([2,1])), 'Av([1,3,2], [3,2,1]) - incr', n)
    dag.add_element(av321_132_minus_incr)

    # TODO: dag stuff

    return dag

def N_P_X_mon1_taylored_for_av_132_4321(perm_prop, n):
    dag = N_P_X_mon1(perm_prop, n)

    p = Permutation([1,3,2])
    q = Permutation([3,2,1])
    pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)-incr' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X_mon1_taylored_for_av_321_1324(perm_prop, n):
    dag = N_P_X_mon1(perm_prop, n)

    p = Permutation([2,1,3])
    q = Permutation([3,2,1])
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))

    p = Permutation([1,3,2])
    q = Permutation([3,2,1])
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X2_mon2_taylored_for_av_321_1342(perm_prop, n):
    dag = N_P_X2_mon2(perm_prop, n)

    p = Permutation([2,3,1])
    q = Permutation([3,2,1])
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))

    return dag

def N_P_X_mon2_taylored_for_av_132_4312(perm_prop, n):
    dag = N_P_X_mon2(perm_prop, n)

    p = Permutation([1,3,2])
    q = Permutation([3,1,2])
    pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)-incr-decr' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X_taylored_for_av_132_4231(perm_prop, n):
    dag = N_P_X(perm_prop, n)

    p = Permutation([1,3,2])
    q = Permutation([3,1,2])
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    p = Permutation([1,3,2])
    q = Permutation([2,3,1])
    pqset = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s) > 0' % (p, q))
    dag.add_element(pqset)

    return dag

# def N_P_X_taylored_for_av_321_3412(perm_prop, n):
#     dag = N_P_X2_mon2(perm_prop, n)

#     p = Permutation([1,3,2])
#     q = Permutation([3,1,2])
#     pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
#         description='Av(%s,%s)' % (p, q))
#     dag.add_element(pqset)

#     p = Permutation([1,3,2])
#     q = Permutation([2,3,1])
#     pqset = StaticPermutationSet.from_predicate((lambda x: len(x) > 0 and x.avoids(p) and x.avoids(q)), n,
#         description='Av(%s,%s) > 0' % (p, q))
#     dag.add_element(pqset)

#     return dag

def N_P_X_taylored_for_av_132_1234(perm_prop, n):
    dag = N_P_X(perm_prop, n)

    p = Permutation([1,3,2])
    q = Permutation([1,2,3])
    # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-decr' % (p, q))
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X_taylored_for_av_132_4312(perm_prop, n):
    dag = N_P_X(perm_prop, n)

    p = Permutation([1,3,2])
    q = Permutation([3,1,2])
    # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X_taylored_for_av_132_4213(perm_prop, n):
    dag = N_P_X(perm_prop, n)

    p = Permutation([1,3,2])
    q = Permutation([2,1,3])
    # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X1_taylored_for_av_231_15432(perm_prop, n):
    dag = N_P_X1(perm_prop, n)

    p = Permutation([2,3,1])
    q = Permutation([3,2,1])
    # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X1_taylored_for_av_231_15423(perm_prop, n):
    dag = N_P_X1(perm_prop, n)

    p = Permutation([2,3,1])
    q = Permutation([3,1,2])
    # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X1_taylored_for_av_231_15324(perm_prop, n):
    dag = N_P_X1(perm_prop, n)

    p = Permutation([2,3,1])
    q = Permutation([2,1,3])
    # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X1_taylored_for_av_231_15234(perm_prop, n):
    dag = N_P_X1(perm_prop, n)

    p = Permutation([2,3,1])
    q = Permutation([1,2,3])
    # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_X_taylored_for_av_231_12534(perm_prop, n):
    dag = N_P_X_mon1(perm_prop, n)

    X_non_decr = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and perm_prop(x)), n, description='X non decr')
    dag.add_element(X_non_decr)

    p = Permutation([2,3,1])
    q = Permutation([1,4,2,3])
    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n,
        description='Av(%s,%s)' % (p, q))
    dag.add_element(pqset)

    return dag

def N_P_taylored_for_av_321_1324_3412(n):
    dag = N_P_incr1(n)

    p = Permutation([3,2,1])
    q = Permutation([1,3,2])
    r = Permutation([3,4,1,2])
    pqrset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q) and x.avoids(r)), n,
        description='Av(%s,%s,%s)' % (p, q, r))
    dag.add_element(pqrset)

    return dag

def len_3_pairs(perm_prop, n):
    dag = N_P_X2_mon2(perm_prop, n)

    for p in Permutations(3):
        for q in Permutations(3):
            if p < q:

                has_incr = Permutation([1,2,3]).avoids(p) and Permutation([1,2,3]).avoids(q)
                has_decr = Permutation([3,2,1]).avoids(p) and Permutation([3,2,1]).avoids(q)

                if has_incr and has_decr:
                    pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
                elif has_incr:
                    pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr' % (p, q))
                elif has_decr:
                    pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-decr' % (p, q))
                else:
                    pqset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)' % (p, q))

                # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
                # pqset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
                if any( len(pqset.perms[l]) > 0 for l in pqset.perms ):
                    dag.add_element(pqset)

    return dag

def len_3_pairs_X_minus_epsilon(perm_prop, n):
    dag = elementary_X_minus_epsilon(perm_prop, n)

    i = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([2,1])), n, description='incr, len>1')
    d = StaticPermutationSet.from_predicate((lambda x: len(x) > 1 and x.avoids([1,2])), n, description='decr, len>1')
    dag.add_element(i)
    dag.add_element(d)

    for p in Permutations(3):
        for q in Permutations(3):
            if p < q:

                has_incr = Permutation([1,2,3]).avoids(p) and Permutation([1,2,3]).avoids(q)
                has_decr = Permutation([3,2,1]).avoids(p) and Permutation([3,2,1]).avoids(q)

                if has_incr and has_decr:
                    pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
                elif has_incr:
                    pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr' % (p, q))
                elif has_decr:
                    pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-decr' % (p, q))
                else:
                    pset = StaticPermutationSet.from_predicate((lambda x: x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)' % (p, q))

                # pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([1,2]) and not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
                # pset = StaticPermutationSet.from_predicate((lambda x: not x.avoids([2,1]) and x.avoids(p) and x.avoids(q)), n, description='Av(%s,%s)-incr-decr' % (p, q))
                if any( len(pset.perms[l]) > 0 for l in pset.perms ):
                    dag.add_element(pset)

    return dag


# A "How To Add a DAG thing" tutorial by Bjarki
# - Step 1:
# def meowz(perm_prop, n):
#     dag = elementary(perm_prop, n)
#     m = meow(n)
#     dag.add_element(m)
#     dag.put_below(N, i)
#     return dag
# - Step 2: You're done.

