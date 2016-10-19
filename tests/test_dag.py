import unittest
import permstruct
from permstruct import *
import permstruct.dag
from permstruct.dag import *
import sys
from permstruct.dag import taylor_dag
from permuta import Permutation
import random

class TestDAG(unittest.TestCase):

    def check(self, expected, actual):
        found = []
        for el in actual.elements:
            if el is not None and el.description.startswith('Av('):
                here = eval(el.description[3:-1])
                here = sorted(here)
                found.append(here)
        found = sorted(found)
        expected = sorted(map(sorted, expected))
        self.assertEqual(expected, found)

    def test_taylor(self):

        settings = StructSettings(
                perm_bound=7,
                max_rule_size=(3,3),
                max_non_empty=3)

        patts = [Permutation([1,2,3]),
                 Permutation([3,2,1])]
        settings.set_input(StructInput.from_avoidance(settings, patts))
        res = taylor_dag(settings, remove=False)
        self.check([
        ], res)

        patts = [Permutation([1,2,3]),
                 Permutation([3,2,1])]
        settings.set_input(StructInput.from_avoidance(settings, patts))
        res = taylor_dag(settings, remove=False, remove_finite=False)
        self.check([
            [[1,2], [2,1]],
            [[1,2,3], [2,1]],
            [[1,2], [3,2,1]],
        ], res)

        patts = [
            Permutation([1,2,3]),
            Permutation([3,2,1]),
        ]
        settings.set_input(StructInput.from_avoidance(settings, patts))
        res = taylor_dag(settings, upper_bound=1, remove=False, remove_finite=False)
        self.check([
        ], res)

        patts = [
            Permutation([1,2,3]),
            Permutation([3,2,1]),
        ]
        settings.set_input(StructInput.from_avoidance(settings, patts))
        res = taylor_dag(settings, max_len_patt=2, remove=False, remove_finite=False)
        self.check([
            [[1,2], [2,1]],
        ], res)

    def test_reachable_above(self):
        dag = DAG()
        for i in range(5):
            dag.add_element(i)
            self.assertEqual([i], sorted(dag.get_reachable_above(i)))
        for i in range(5):
            self.assertEqual([i], sorted(dag.get_reachable_above(i)))

        dag.put_below(3, 4)
        self.assertEqual([3], sorted(dag.get_reachable_above(3)))
        self.assertEqual([3,4], sorted(dag.get_reachable_above(4)))
        self.assertEqual([1], sorted(dag.get_reachable_above(1)))

        dag.put_below(1, 0)
        dag.put_below(2, 1)
        self.assertEqual([2], sorted(dag.get_reachable_above(2)))
        self.assertEqual([1,2], sorted(dag.get_reachable_above(1)))
        self.assertEqual([0,1,2], sorted(dag.get_reachable_above(0)))

        dag.put_below(2, 0)
        self.assertEqual([2], sorted(dag.get_reachable_above(2)))
        self.assertEqual([1,2], sorted(dag.get_reachable_above(1)))
        self.assertEqual([0,1,2], sorted(dag.get_reachable_above(0)))

        dag.put_below(4, 1)
        self.assertEqual([2], sorted(dag.get_reachable_above(2)))
        self.assertEqual([1,2,3,4], sorted(dag.get_reachable_above(1)))
        self.assertEqual([0,1,2,3,4], sorted(dag.get_reachable_above(0)))

        dag.put_below(4, 2)
        self.assertEqual([0,1,2,3,4], sorted(dag.get_reachable_above(0)))
        self.assertEqual([1,2,3,4], sorted(dag.get_reachable_above(1)))
        self.assertEqual([2,3,4], sorted(dag.get_reachable_above(2)))
        self.assertEqual([3], sorted(dag.get_reachable_above(3)))
        self.assertEqual([3,4], sorted(dag.get_reachable_above(4)))

    def get_random_dag(self,n,p):
        dag = DAG()
        for i in range(n):
            dag.add_element(i)
        arr = [ i for i in range(n) ]
        random.shuffle(arr)
        for i in range(n):
            for j in range(i+1,n):
                if random.random() < p:
                    dag.put_below(arr[i], arr[j])
        return dag

    def test_topological_order(self):
        for n in range(100):
            p = random.random()
            dag = self.get_random_dag(n,p)
            arr = dag.get_topological_order()
            seen = set()
            for x in arr:
                seen.add(x)
                for y in dag.get_reachable_above(x):
                    self.assertTrue(y in seen)

    def test_transitive_reduction(self):
        def es(d):
            return sum( len(v) for (k,v) in d.above.items() )

        a = 0
        b = 0
        for n in range(100):
            p = random.random()
            dag = self.get_random_dag(n,p)
            dag2 = dag.get_transitive_reduction()
            for x in dag.elements:
                self.assertEqual(sorted(dag.get_reachable_above(x)),
                                 sorted(dag2.get_reachable_above(x)))

            a += es(dag)
            b += es(dag2)

        self.assertTrue(a*20/100 > b) # just a sanity check, but can fail with low probability

