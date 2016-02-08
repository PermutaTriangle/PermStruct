from __future__ import print_function
from permstruct import RuleSet
from .functions import generate_rules_with_overlay_upto, generate_rules_upto, generate_small_input
from permstruct.dag import DAG
from permuta.misc import ProgressBar
import sys


def exhaustive(
        perm_prop,
        perm_bound,
        dag,
        max_rule_size,
        max_nonempty,

        max_rules=None,
        ignore_first=1,
        allow_overlap_in_first=True,
        min_rule_size=(1,1),
        lower_bound=None,
    ):

    rules = RuleSet(perm_prop, perm_bound)

    assert ignore_first < rules.validcnt, "All permutations from the set are ignored"

    small_input = generate_small_input(perm_prop)
    rule_cnt = 0

    sys.stderr.write('Generating rules\n')
    sets = sorted(dag.elements, key=lambda x: (repr(type(x)), x))
    gen = generate_rules_upto(min_rule_size, max_rule_size, small_input, sets, max_nonempty, mn_at_most=perm_bound)

    sys.stderr.write('Processing rules\n')
    ProgressBar.create(len(gen))
    for rule in gen:
        ProgressBar.progress()
        rule_cnt += 1
        rules.add_rule(rule)
    ProgressBar.finish()

    sys.stderr.write('Found %d rules, %d of which are valid, %d of which are distinct\n' % (
            rule_cnt,
            sum( len(v) for k, v in rules.rules.items() ),
            len(rules.rules),
        ))

    rules.print_stats()

    print(rules.lens)
    print('')

    dag_elems_id = { v:i for i,v in enumerate(sets) }
    res = rules.exact_cover(
            allow_overlap_in_first=allow_overlap_in_first,
            ignore_first=ignore_first,
            lower_bound=lower_bound,
            dag_elems_id=dag_elems_id,
            max_ec_cnt=max_rules,
        )

    for k,v in enumerate(sets):
        print(repr(tuple([k,v.description if v is not None else 'None'])))

    return res


def exhaustive_with_overlays(
        perm_prop,
        perm_bound,
        dag,
        max_rule_size,
        max_nonempty,

        overlay_dag,
        max_overlay_cnt,
        max_overlay_size,

        max_rules=None,
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
            allow_overlap_in_first=allow_overlap_in_first,
            ignore_first=ignore_first,
            dag_elems_id=dag_elems_id,
            max_ec_cnt=max_rules,
        )

