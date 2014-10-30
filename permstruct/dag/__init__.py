from permstruct import E, N, P, X
from permstruct.permutation_sets.units import *

from .dag import DAG

def x_dag(perm_prop, n):
    dag = DAG()
    dag.add_element(X, perm_prop)
    return dag

def decr_dag(perm_prop, n):
    dag = elementary(perm_prop, n)
    d = decr(n)
    dag.add_element(d, lambda p: all( x > y for x,y in zip(p, p[1:]) ))
    dag.put_below(N, d)
    dag.put_below(P, d)
    return dag

def elementary(perm_prop, n):
    dag = DAG()
    # dag.add_element(E, lambda p: False)
    dag.add_element(N, lambda p: len(p) == 0)
    dag.add_element(P, lambda p: len(p) == 1)
    dag.add_element(X, perm_prop)
    # dag.put_below(E, N)
    # dag.put_below(E, P)
    # dag.put_below(E, X)
    return dag

def incr_decr(perm_prop, n):
    dag = elementary(perm_prop, n)
    i = incr(n)
    d = decr(n)
    dag.add_element(i, lambda p: all( x < y for x,y in zip(p, p[1:]) ))
    dag.add_element(d, lambda p: all( x > y for x,y in zip(p, p[1:]) ))
    dag.put_below(N, i)
    dag.put_below(P, i)
    dag.put_below(N, d)
    dag.put_below(P, d)
    return dag

def incr_decr_nonempty(perm_prop, n):
    dag = elementary(perm_prop, n)
    i = incr_nonempty(n)
    d = decr_nonempty(n)
    dag.add_element(i, lambda p: all( x < y for x,y in zip(p, p[1:]) ))
    dag.add_element(d, lambda p: all( x > y for x,y in zip(p, p[1:]) ))
    dag.put_below(P, i)
    dag.put_below(P, d)
    return dag

def classic_avoiders_length_3(perm_prop, n):
    dag = elementary(perm_prop, n)
    i = incr(n)
    d = decr(n)
    dag.add_element(i, lambda p: all( x < y for x,y in zip(p, p[1:]) ))
    dag.add_element(d, lambda p: all( x > y for x,y in zip(p, p[1:]) ))
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

    dag.add_element(av123, lambda p: p.avoids([1,2,3]))
    dag.add_element(av132, lambda p: p.avoids([1,3,2]))
    dag.add_element(av213, lambda p: p.avoids([2,1,3]))
    dag.add_element(av231, lambda p: p.avoids([2,3,1]))
    dag.add_element(av312, lambda p: p.avoids([3,1,2]))
    dag.add_element(av321, lambda p: p.avoids([3,2,1]))

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

    return dag

