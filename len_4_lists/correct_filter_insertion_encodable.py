# import sys
# from permuta import Permutation

# The following code is based on "The Insertion Encoding of Permutations".
#

def is_incr_next_incr(perm):
    for i in range(len(perm) - 1):
        if perm[i+1] < perm[i]:
            for j in range(i+1,len(perm) - 1):
                if perm[j+1] < perm[j]:
                    return False
            break
    return True

def is_incr_next_decr(perm):
    for i in range(len(perm) - 1):
        if perm[i+1] < perm[i]:
            for j in range(i+1,len(perm) - 1):
                if perm[j+1] > perm[j]:
                    return False
            break
    return True

def is_decr_next_incr(perm):
    for i in range(len(perm) - 1):
        if perm[i+1] > perm[i]:
            for j in range(i+1,len(perm) - 1):
                if perm[j+1] < perm[j]:
                    return False
            break
    return True

def is_decr_next_decr(perm):
    for i in range(len(perm) - 1):
        if perm[i+1] > perm[i]:
            for j in range(i+1,len(perm) - 1):
                if perm[j+1] > perm[j]:
                    return False
            break
    return True

# For the over bases I rotate 90 degrees then use above code
def rotate(perm):
    n = len(perm)
    return Permutation([ perm.index(n-i) + 1 for i in range(n)])


mem = dict()
def insertion_encodable_properties(perm):
    if tuple(perm) in mem:
        return mem[tuple(perm)]

    properties = []
    if is_incr_next_decr(perm):
        properties.append(0)
    if is_incr_next_incr(perm):
        properties.append(1)
    if is_decr_next_decr(perm):
        properties.append(2)
    if is_decr_next_incr(perm):
        properties.append(3)

    res = sum( 1 << x for x in properties )
    mem[tuple(perm)] = res

    return res

def is_insertion_encodable(C):
    goal = (1 << 4) - 1
    curr = 0
    # Check for insertion_encodable by rightmost
    for perm in C:
        curr = curr | insertion_encodable_properties(perm)
        if curr == goal:
            return True
    curr = 0
    # Check for insertion_encodable by maximum
    for perm in C:
        curr = curr | insertion_encodable_properties(rotate(perm))
        if curr == goal:
            return True
    return False
