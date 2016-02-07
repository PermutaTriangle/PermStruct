import unittest
import permstruct
import permstruct.dag
import sys
from permstruct.dag import taylor_dag
from permuta import Permutation

class TestDAG(unittest.TestCase):

    def check(self, expected, actual):
        found = []
        for el in actual.elements:
            if el is not None and el.description.startswith('Av('):
                here = eval('[%s]' % el.description[3:-1])
                here = sorted(here)
                found.append(here)
        found = sorted(found)
        expected = sorted(map(sorted, expected))
        self.assertEqual(expected, found)

    def test_taylor(self):

        res = taylor_dag([
            Permutation([1,2,3]),
            Permutation([3,2,1]),
        ], 7, remove=False)
        self.check([
            [[1,2], [2,1]],
            [[1,2,3], [2,1]],
            [[1,2], [3,2,1]],
        ], res)

        res = taylor_dag([
            Permutation([1,2,3]),
            Permutation([3,2,1]),
        ], 7, upper_bound=1, remove=False)
        self.check([
        ], res)

        res = taylor_dag([
            Permutation([1,2,3]),
            Permutation([3,2,1]),
        ], 7, max_len_patt=2, remove=False)
        self.check([
            [[1,2], [2,1]],
        ], res)

