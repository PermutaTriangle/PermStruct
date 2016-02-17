import unittest
import permstruct
from permstruct import *
import permstruct.dag
from permstruct.dag import *
import sys

class TestTravis(unittest.TestCase):
    def test_travis(self):
        # perm_prop = lambda p: p.avoids([2,3,1])
        # perm_bound = 6
        # inp_dag = permstruct.dag.incr_decr(perm_prop, perm_bound)
        # sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (3, 3), 4)
        # for sol in sol_iter:
        #     pass
        #
        #     # sys.stdout.write('====================================\n')
        #     # sys.stdout.write('\n')
        #     # for rule in sol:
        #     #     sys.stdout.write('%s\n\n' % rule)
        #
        patts = [ Permutation([2,3,1]) ]
        settings = StructSettings(
                perm_bound=6,
                max_rule_size=(3,3),
                max_non_empty=4)
        settings.set_input(StructInput.from_avoidance(settings, patts))
        settings.set_dag(taylor_dag(settings))

        exhaustive(settings)

