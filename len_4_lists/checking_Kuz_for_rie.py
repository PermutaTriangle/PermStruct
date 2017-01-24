
L = []

patts = [Permutation([2,1,4,3]), Permutation([3,1,4,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([1,3,2,4])]
L.append(patts)
patts = [Permutation([2,4,3,1]), Permutation([2,1,4,3]), Permutation([3,1,4,2]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([1,3,2,4]), Permutation([1,4,2,3]), Permutation([1,2,4,3])]
L.append(patts)
patts = [Permutation([2,3,4,1]), Permutation([2,3,1,4]), Permutation([2,4,1,3]), Permutation([2,1,4,3]), Permutation([4,3,1,2]), Permutation([1,4,3,2]), Permutation([1,3,2,4]), Permutation([1,2,4,3])]
L.append(patts)
patts = [Permutation([2,4,3,1]), Permutation([2,3,4,1]), Permutation([4,2,1,3]), Permutation([2,1,4,3]), Permutation([3,1,4,2]), Permutation([3,1,2,4]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([4,1,2,3])]
L.append(patts)
patts = [Permutation([3,2,1,4]), Permutation([2,4,3,1]), Permutation([2,4,1,3]), Permutation([2,1,4,3]), Permutation([2,1,3,4]), Permutation([3,1,4,2]), Permutation([3,1,2,4]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([1,2,3,4])]
L.append(patts)
patts = [Permutation([3,2,1,4]), Permutation([2,4,3,1]), Permutation([2,3,4,1]), Permutation([2,4,1,3]), Permutation([2,1,3,4]), Permutation([3,1,2,4]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([4,1,2,3]), Permutation([1,2,4,3])]
L.append(patts)
patts = [Permutation([2,4,1,3]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([1,3,2,4])]
L.append(patts)
patts = [Permutation([3,2,1,4]), Permutation([2,4,3,1]), Permutation([4,2,1,3]), Permutation([2,1,4,3]), Permutation([2,1,3,4]), Permutation([3,1,2,4]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([4,1,2,3])]
L.append(patts)
patts = [Permutation([2,3,1,4]), Permutation([4,2,1,3]), Permutation([2,4,1,3]), Permutation([3,1,2,4]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([4,1,2,3])]
L.append(patts)
patts = [Permutation([2,4,3,1]), Permutation([4,2,1,3]), Permutation([2,4,1,3]), Permutation([2,1,4,3]), Permutation([2,1,3,4]), Permutation([3,1,4,2]), Permutation([1,4,3,2]), Permutation([1,3,4,2]), Permutation([1,3,2,4]), Permutation([4,1,2,3]), Permutation([1,2,3,4])]
L.append(patts)
patts = [Permutation([2,4,3,1]), Permutation([2,3,4,1]), Permutation([2,3,1,4]), Permutation([4,2,1,3]), Permutation([2,4,1,3]), Permutation([2,1,4,3]), Permutation([2,1,3,4]), Permutation([3,1,2,4]), Permutation([1,4,3,2]), Permutation([4,1,2,3])]
L.append(patts)
patts = [Permutation([2,4,3,1]), Permutation([2,1,4,3]), Permutation([2,1,3,4]), Permutation([3,4,1,2]), Permutation([4,1,3,2]), Permutation([1,4,3,2]), Permutation([1,3,2,4])]
L.append(patts)
patts = [Permutation([2,3,1,4]), Permutation([4,2,1,3]), Permutation([2,4,1,3]), Permutation([2,1,4,3]), Permutation([3,4,1,2]), Permutation([3,1,4,2]), Permutation([1,4,3,2])]
L.append(patts)

cntr = 1
for B in L:
    print 'Kuzmaul example ', cntr
    cntr += 1
    print B
    print is_insertion_encodable(B)
    print ""
