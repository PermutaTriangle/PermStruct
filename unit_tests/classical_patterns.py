
from test import Test, AvoidanceTest


'''
Classical pattern avoidance
Data from http://en.wikipedia.org/wiki/Enumerations_of_specific_permutation_classes
'''


'''
One pattern of length 3
'''

Test.register(AvoidanceTest(
    [[1,2,3]],
    [1, 2, 5, 14, 42, 132, 429, 1430],
    None
))

Test.register(AvoidanceTest(
    [[2,3,1]],
    [1, 2, 5, 14, 42, 132, 429, 1430],
    {
        (2, 2): set(),
        (3, 3): {
            GeneratingRule([
                [None, P, None],
                [None, None, I],
                [I, None, None]
            ]),
            GeneratingRule([
                [None, None, I],
                [P, None, None],
                [None, I, None]
            ])
        }
    }
))


'''
One pattern of length 4
'''

Test.register(AvoidanceTest(
    [[1,3,4,2]],
    [1, 2, 6, 23, 103, 512, 2740, 15485],
    None
))

Test.register(AvoidanceTest(
    [[2,4,1,3]],
    [1, 2, 6, 23, 103, 512, 2740, 15485],
    None
))

#-

Test.register(AvoidanceTest(
    [[1,2,3,4]],
    [1, 2, 6, 23, 103, 513, 2761, 15767],
    None
))

Test.register(AvoidanceTest(
    [[1,4,3,2]],
    [1, 2, 6, 23, 103, 513, 2761, 15767],
    None
))

Test.register(AvoidanceTest(
    [[2,1,4,3]],
    [1, 2, 6, 23, 103, 513, 2761, 15767],
    None
))

#-

Test.register(AvoidanceTest(
    [[1,3,2,4]],
    [1, 2, 6, 23, 103, 513, 2762, 15793],
    None
))

'''
One pattern of length 3 and one of length 4
'''
