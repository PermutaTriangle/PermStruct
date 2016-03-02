from permuta import Permutation
from permstruct import *
from permstruct.dag import taylor_dag

# patts = [ Permutation([1,3,2]), Permutation([4,3,1,2]) ]
patts = [ Permutation([1,3,2]) ]
# patts = [Permutation([3,2,1]), Permutation([2,1,4,3])]
# patts = [ Permutation([1,2,3]) ]
# patts = [ Permutation([1,3,2,4]) ]

perm_bound = 7
settings = StructSettings(
        perm_bound=perm_bound,
        verify_bound=9,
        max_rule_size=(3,3),
        max_non_empty=3,
        verbosity=StructLogger.INFO)
settings.set_input(StructInput.from_avoidance(settings, patts))
# settings.set_dag(taylor_dag(settings, max_len_patt=3, remove=True, upper_bound=3))
# settings.set_dag(taylor_dag(settings, remove=False))
# el = taylor_dag(settings, remove=True, max_len_patt=2, upper_bound=1).elements
# print(el)
# print(len(el))
settings.set_dag(taylor_dag(settings, remove=False))
# settings.set_dag(taylor_dag(settings, max_len_patt=3, remove=False, upper_bound=3))

exhaustive(settings)

# [2016-02-26 10:24:22.539623] Found 210 rules, 210 of which are valid, 180 of which are distinct
# [2016-02-26 10:24:44.030354] Found 204 rules, 204 of which are valid, 174 of which are distinct


