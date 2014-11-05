
from permstruct import RuleSet
from .functions import find_multiple_rules, generate_rules_with_overlay_upto, generate_rules_upto
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

    rules = RuleSet(perm_prop, perm_bound)

    assert ignore_first < rules.validcnt, "All permutations from the set are ignored"

    rule_cnt = 0
    for rule in generate_rules_upto(min_rule_size, max_rule_size, perm_prop, perm_bound, dag.elements, max_nonempty):
        rule_cnt += 1
        rules.add_rule(rule)

    print('Found %d rules, %d of which are valid, %d of which are distinct' % (
            rule_cnt,
            sum( len(v) for k, v in rules.rules.items() ),
            len(rules.rules),
        ))

    rules.print_stats()

    return rules.exact_cover(
            max_rules,
            ignore_first,
            allow_overlap_in_first,
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

    rule_cnt = 0
    for rule in generate_rules_with_overlay_upto(min_rule_size, max_rule_size, perm_prop, perm_bound, dag.elements, max_nonempty, overlay_dag.elements, max_overlay_cnt, max_overlay_size):

        # print(rule)
        # print ""

        rule_cnt += 1
        rules.add_rule(rule)

    print('Found %d rules, %d of which are valid, %d of which are distinct' % (
            rule_cnt,
            sum( len(v) for k, v in rules.rules.items() ),
            len(rules.rules),
        ))

    return rules.exact_cover(
            max_rules,
            ignore_first,
            allow_overlap_in_first,
        )

