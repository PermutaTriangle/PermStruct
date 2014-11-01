
from permstruct import RuleSet
from .functions import find_multiple_rules, generate_rules_with_overlay_upto
from permstruct.dag import DAG


def exhaustive(
        perm_prop,
        perm_bound,
        dag,
        max_rule_size,
        max_nonempty,
        max_rules,

        ignore_first=1,
        allow_overlap_in_first=True,
        min_rule_size=(1,1),
    ):

    return exhaustive_with_overlays(
            perm_prop,
            perm_bound,
            dag,
            max_rule_size,
            max_nonempty,
            max_rules,

            DAG(),
            0,
            (0,0),

            ignore_first,
            allow_overlap_in_first,
            min_rule_size,
        )


def exhaustive_with_overlays(
        perm_prop,
        perm_bound,
        dag,
        max_rule_size,
        max_nonempty,
        max_rules,

        overlay_dag,
        max_overlay_cnt,
        max_overlay_size,

        ignore_first=1,
        allow_overlap_in_first=True,
        min_rule_size=(1,1),
    ):

    rules = RuleSet(perm_prop, perm_bound)

    assert ignore_first < rules.validcnt, "All permutations from the set are ignored"

    for rule in generate_rules_with_overlay_upto(min_rule_size, max_rule_size, dag.elements, max_nonempty, overlay_dag.elements, max_overlay_cnt, max_overlay_size):
        rules.add_rule(rule)

    print('Found %d rules, %d of which are distinct' % (
            sum( len(v) for k, v in rules.rules.items() ),
            len(rules.rules)
        ))

    return rules.exact_cover(
            max_rules,
            ignore_first,
            allow_overlap_in_first,
        )

