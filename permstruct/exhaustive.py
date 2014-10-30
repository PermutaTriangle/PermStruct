
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

    rules = list(generate_rules_with_overlay_upto(min_rule_size, max_rule_size, dag.elements, max_nonempty, overlay_dag.predicates, max_overlay_cnt, max_overlay_size))
    sol_iter = find_multiple_rules(rules, perm_bound, max_rules, perm_prop, ignore_first, allow_overlap_in_first)

    for sol in sol_iter:
        yield [ rule for rule, bs in sol ]

