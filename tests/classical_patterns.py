'''
Classical pattern avoidance
Data from http://en.wikipedia.org/wiki/Enumerations_of_specific_permutation_classes
'''

'''
One pattern of length 3
'''

patts = [[1,2,3]]
enum  = [1, 2, 5, 14, 42, 132, 429, 1430]

patts = [[2,3,1]]
enum  = [1, 2, 5, 14, 42, 132, 429, 1430]

'''
One pattern of length 4
'''

patts = [[1,3,4,2]]
enum  = [1, 2, 6, 23, 103, 512, 2740, 15485]

patts = [[2,4,1,3]]
enum  = [1, 2, 6, 23, 103, 512, 2740, 15485]

#-

patts = [[1,2,3,4]]
enum  = [1, 2, 6, 23, 103, 513, 2761, 15767]

patts = [[1,2,4,3]]
enum  = [1, 2, 6, 23, 103, 513, 2761, 15767]

patts = [[1,4,3,2]]
enum  = [1, 2, 6, 23, 103, 513, 2761, 15767]

patts = [[2,1,4,3]]
enum  = [1, 2, 6, 23, 103, 513, 2761, 15767]

#-

patts = [[1,3,2,4]]
enum  = [1, 2, 6, 23, 103, 513, 2762, 15793]

'''
One pattern of length 3 and one of length 4
'''