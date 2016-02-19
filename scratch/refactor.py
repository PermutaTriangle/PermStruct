from permuta import Permutation
from permstruct import *
from permstruct.dag import taylor_dag

# patts = [ Permutation([1,3,2]), Permutation([4,3,1,2]) ]
patts = [ Permutation([1,3,2]) ]

perm_bound = 7
settings = StructSettings(
        perm_bound=perm_bound,
        max_rule_size=(3,3),
        max_non_empty=3,
        verbosity=StructLogger.INFO)
settings.set_input(StructInput.from_avoidance(settings, patts))
settings.set_dag(taylor_dag(settings, max_len_patt=3, remove=True, upper_bound=3))
# settings.set_dag(taylor_dag(settings, max_len_patt=3, remove=False, upper_bound=3))

exhaustive(settings)

