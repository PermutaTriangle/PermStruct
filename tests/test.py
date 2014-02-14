


class Test(object):

    registered_tests = []

    def __init__(self, expected):
        self.expected = expected

    def run(self):
        raise NotImplementedError()

    @staticmethod
    def register(test):
        self.registered_tests.append(test)


class AvoidanceTest(Test):
    def __init__(self, avoid_patts, enum, expected):
        Test.__init__(self, expected)
        self.avoid_patts = avoid_patts
        self.enum = enum

