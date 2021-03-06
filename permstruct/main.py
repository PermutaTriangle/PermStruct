from __future__ import print_function
from permuta import Permutation
from permstruct import StructSettings, StructLogger, AvoiderInput, exhaustive
from permstruct.dag import taylor_dag, SubPatternType

def struct(patts, size=None, perm_bound=None, verify_bound=None, subpatts_len=None, subpatts_num=None, subpatts_type=SubPatternType.EVERY, ask_verify_higher=True):
    """
    INPUT:

    - ``patts'' - the patterns in the basis.

    - ``size'' - the maximum size of the rules to try.

    - ``perm_bound'' - the longest permutations to use from Av(patts).

    - ``verify_bound'' - the longest permutations from Av(patts) to use to verify the cover found.

    - ``subpatts_len'' - the longest subpattern to use from the basis.

    - ``subpatts_num'' - the maximum number of subpatterns to use from the basis.

    - ``subpatts_type'' - the type of subpattern to use from the basis.

    - ``ask_verify_higher'' - whether to ask about verifying with longer permutations.
    """

    k = 1 if len(patts) == 0 else max( len(p) for p in patts )

    # Grids
    if size is not None:
        max_rule_size = (size,size)
        max_non_empty = size
    else:
        max_rule_size = (k+1, k+1)
        max_non_empty = k+1
    max_rules     = None

    # Perms
    if size is None:
        perm_bound = k+2 if perm_bound is None else perm_bound
    else:
        perm_bound = max(size+1, k+2 if perm_bound is None else perm_bound)
    # perm_bound    = k+2 if perm_bound is None else perm_bound
    verify_bound  = perm_bound+2 if verify_bound is None else verify_bound

    # The dag
    max_len_patt = subpatts_len
    upper_bound  = subpatts_num
    remove       = False

    settings = StructSettings(
            perm_bound=perm_bound,
            verify_bound=verify_bound,
            max_rule_size=max_rule_size,
            max_non_empty=max_non_empty,
            max_rules=max_rules,
            verbosity=StructLogger.INFO,
            ask_verify_higher=ask_verify_higher)
    settings.set_input(AvoiderInput(settings, patts))
    settings.set_dag(taylor_dag(settings,
                        max_len_patt=max_len_patt,
                        remove=remove,
                        upper_bound=upper_bound,
                        subpattern_type=subpatts_type))

    exhaustive(settings)
