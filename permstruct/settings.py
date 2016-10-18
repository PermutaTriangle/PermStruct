from .logger import StructLogger

class StructSettings(object):
    def __init__(self,
            # General
            perm_bound=None, # The upper bound on the length of the permutations to consider from the input
            verbosity=StructLogger.WARNING, # Verbosity of output

            # Rule generation
            max_rule_size=None,  # The maximum rule size, a tuple
            min_rule_size=(1,1), # The minimum rule size, a tuple
            max_non_empty=None, # The maximum number of non-empty cells in a rule
            mn_at_most=None, # The maximum minimum length permutation that a rule can generate
            filter_rule_incrementally=False, # Whether the rules should be filtered at every step of the generation (a tradeoff)

            # Exact cover
            max_rules=None, # Maximum number of rules to use in the exact cover, or None if unlimited
            ignore_first=0, # The number of permutations to ignore in the exact cover, counted from the smallest up
            allow_overlap_in_first=True, # Whether to allow overlap in the `ignore_first` permutations

            # Verification
            verify_bound=None, # The upper bound on the length of the permutations used to verify an output rule
            ask_verify_higher=True, # If everything verifies up to length verify_bound, whether to ask if verification should be continued

            # Bounds
            lower_bound=None, # The ratio of permutations that need to be found, at least

            # Cache
            ignore_cache=False,
    ):
        assert perm_bound is not None, 'perm_bound is required'
        assert max_rule_size is not None, 'max_rule_size is required'
        assert max_non_empty is not None, 'max_non_empty is required'

        # General
        self.perm_bound = perm_bound
        self.logger = StructLogger(verbosity=verbosity)

        # Rule generation
        self.max_rule_size = max_rule_size
        self.min_rule_size = min_rule_size
        self.max_non_empty = max_non_empty
        self.mn_at_most = mn_at_most if mn_at_most is not None else perm_bound
        self.filter_rule_incrementally = filter_rule_incrementally

        # Exact cover
        self.max_rules = max_rules
        self.ignore_first = ignore_first
        self.allow_overlap_in_first = allow_overlap_in_first

        # Verification
        self.verify_bound = max(perm_bound, verify_bound if verify_bound is not None else 0)
        self.ask_verify_higher = ask_verify_higher

        # Bounds
        self.lower_bound = lower_bound

        # Cache
        self.ignore_cache = ignore_cache

    def set_input(self, sinput):
        self.sinput = sinput

    def set_dag(self, dag):
        self.dag = dag
        self.sets = sorted(dag.elements, key=lambda x: (repr(type(x)), x))
