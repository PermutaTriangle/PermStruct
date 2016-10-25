from __future__ import print_function
from permstruct import RuleSet
from .functions import populate_rule_set
from permstruct.dag import DAG
from permuta.misc import ProgressBar
import sys


def exhaustive(settings):

    for k,v in enumerate(settings.sets):
        settings.logger.log(repr(tuple([k,v.description if v is not None else 'None'])))

    rules = RuleSet(settings)

    rule_cnt = 0

    settings.logger.log('Generating rules')

    populate_rule_set(settings, rules)

    settings.logger.log('Found %d rules, %d of which are valid, %d of which are distinct' % (
            rules.total_rules,
            sum( len(v) for k, v in rules.rules.items() ),
            len(rules.rules),
        ))

    rules.print_stats()

    settings.logger.log('')

    dag_elems_id = dict()
    for i,v in enumerate(settings.sets):
        dag_elems_id[v] = i
    res = rules.exact_cover(settings)

    for k,v in enumerate(settings.sets):
        settings.logger.log(repr(tuple([k,v.description if v is not None else 'None'])))

    return res


