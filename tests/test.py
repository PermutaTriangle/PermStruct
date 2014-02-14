
from struct import generate_rules, matches_rule, I, P, N


class Test(object):

    registered_tests = []

    def __init__(self, expected):
        self.expected = expected

    def run(self):
        raise NotImplementedError()

    @staticmethod
    def register(test):
        self.registered_tests.append(test)

    @staticmethod
    def run_all():

        for test in registered_tests:
            test.run()


class AvoidanceTest(Test):
    def __init__(self, avoid_patts, enum, expected):
        Test.__init__(self, expected)
        self.avoid_patts = avoid_patts
        self.enum = enum

