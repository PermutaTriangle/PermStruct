'''
Find all different (up to symmetry) classes of the form Av(321, p, q) where p,q
are classical patterns of lenght 4
'''

# Symmetries fixing 321
# perm = Permutation([3,2,1])

# S =  Set([perm,
# 	 perm.inverse(),
# 	 perm.reverse().complement(),
# 	 perm.reverse().complement().inverse()])
# print S.cardinality()

symms_fixing_321 = [lambda p : p,
                    lambda p : p.inverse(),
                    lambda p : p.reverse().complement(),
                    lambda p : p.reverse().complement().inverse()]

L = []
for p in Permutations(4):
	if p != Permutation([1,2,3,4]) and p.avoids([3,2,1]):
		for q in Permutations(4):
			if q != p and q != Permutation([1,2,3,4]) and q.avoids([3,2,1]):
				L.append([p,q])

ell = [0]*len(L)

print "Created L and ell"

c = 1
for i in range(len(L)):
	if ell[i] == 0:
		print '#-- Symmetry-class %s --#' % (c)
		print '# perm_prop = lambda p: p.avoids(%s) and p.avoids(%s) and p.avoids(%s)' % ([3,2,1],L[i][0],L[i][1])
		print ''
		c = c+1
		for j in range(i+1,len(L)):
			if any(Set(L[j]) == Set(map(symm,L[i]))
				   for symm in symms_fixing_321):
				ell[j] = 1

unique = [L[g] for g in range(len(L)) if ell[g] == 0]

# for u in unique:
# 	print 'perm_prop = lambda p: p.avoids(%s) and p.avoids(%s) and p.avoids(%s)' % ([3,2,1],u[0],u[1])

# All symmetries
# perm = Permutations(100).random_element()

# S =  Set([perm,
# 	 perm.reverse(), perm.complement(), perm.inverse(),
# 	 perm.reverse().complement(), perm.reverse().inverse(), perm.complement().inverse(),
# 	 perm.reverse().complement().inverse()])
# print S.cardinality()