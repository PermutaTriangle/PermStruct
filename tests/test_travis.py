import unittest
import permstruct
import permstruct.dag
import sys

class TestTravis(unittest.TestCase):
    def test_travis(self):
        perm_prop = lambda p: p.avoids([2,3,1])
        perm_bound = 6
        inp_dag = permstruct.dag.incr_decr(perm_prop, perm_bound)
        sol_iter = permstruct.exhaustive(perm_prop, perm_bound, inp_dag, (3, 3), 4)
        for sol in sol_iter:
            pass

            # sys.stdout.write('====================================\n')
            # sys.stdout.write('\n')
            # for rule in sol:
            #     sys.stdout.write('%s\n\n' % rule)

