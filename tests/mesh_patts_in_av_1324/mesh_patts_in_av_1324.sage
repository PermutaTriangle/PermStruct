def G(w):
    """
    The graph/diagram of the permutation w
    """
    return [ (x+1,y) for (x,y) in enumerate(w) ]

def avoids_mpat(perm, pat, R=[]):
    """
    Returns False if (pat, R) occurs in perm, otherwise returns True
    """

    k = len(pat)
    n = len(perm)

    if k>n: return True

    pat = G(pat)
    perm = G(perm)
    for H in Subwords(perm, k):

        X = dict(G(sorted(i for (i,_) in H)))
        Y = dict(G(sorted(j for (_,j) in H)))
        if H == [ (X[i], Y[j]) for (i,j) in pat ]:
            X[0], X[k+1] = 0, n+1
            Y[0], Y[k+1] = 0, n+1
            shady = ( X[i] < x < X[i+1] and Y[j] < y < Y[j+1]
                      for (i,j) in R
                      for (x,y) in perm
                      )
            if not any(shady):
                return False
    return True

def num_occs_mpat(perm, pat, R=[]):
    """
    Returns the number of copies/occurrences of (pat, R) in perm
    """
    occs = 0
    k = len(pat)
    n = len(perm)
    pat = G(pat)
    perm = G(perm)
    for H in Subsets(perm, k):
        H = sorted(H)
        X = dict(G(sorted(i for (i,_) in H)))
        Y = dict(G(sorted(j for (_,j) in H)))
        if H == [ (X[i], Y[j]) for (i,j) in pat ]:
            X[0], X[k+1] = 0, n+1
            Y[0], Y[k+1] = 0, n+1
            shady = ( X[i] < x < X[i+1] and Y[j] < y < Y[j+1]
                      for (i,j) in R
                      for (x,y) in perm
                      )
            if not any(shady):
                occs = occs + 1
    return occs

# N = 9
# for n in range(N+1):
#     print 'Looking at permutations of length %s' % (n)

#     # nom1 = 0
#     # nom2 = 0
#     f1 = 0
#     f2 = 0
#     for perm in Permutations(n, avoiding = [1,3,2,4]):
#         # nom1 = nom1 + num_occs_mpat(perm, [1], [(1,0)])
#         # nom2 = nom2 + num_occs_mpat(perm, [2,1], [(0,0),(1,1),(2,1),(2,0)])
#         nom1 = num_occs_mpat(perm, [1], [(1,0)])
#         nom2 = num_occs_mpat(perm, [2,1], [(0,0),(1,1),(2,1),(2,0)])
#         f1 = f1 + x^nom1
#         f2 = f2 + x^nom2
#     # print 'nom1 is %s' % (nom1)
#     # print 'nom2 is %s' % (nom2)
#     print 'f1 is %s' % (f1)
#     print 'f2 is %s' % (f2)
#     print ''

'''
Output

Looking at permutations of length 0
f1 is 1
f2 is 1

Looking at permutations of length 1
f1 is x
f2 is 1

Looking at permutations of length 2
f1 is x^2 + x
f2 is x + 1

Looking at permutations of length 3
f1 is x^3 + 3*x^2 + 2*x
f2 is x^2 + 3*x + 2

Looking at permutations of length 4
f1 is x^4 + 5*x^3 + 11*x^2 + 6*x
f2 is x^3 + 6*x^2 + 10*x + 6

Looking at permutations of length 5
f1 is x^5 + 7*x^4 + 24*x^3 + 48*x^2 + 23*x
f2 is x^4 + 9*x^3 + 30*x^2 + 41*x + 22

Looking at permutations of length 6
f1 is x^6 + 9*x^5 + 41*x^4 + 123*x^3 + 236*x^2 + 103*x
f2 is x^5 + 12*x^4 + 59*x^3 + 155*x^2 + 194*x + 92

Looking at permutations of length 7
f1 is x^7 + 11*x^6 + 62*x^5 + 239*x^4 + 674*x^3 + 1262*x^2 + 513*x
f2 is x^6 + 15*x^5 + 97*x^4 + 364*x^3 + 851*x^2 + 1007*x + 427

Looking at permutations of length 8
f1 is x^8 + 13*x^7 + 87*x^6 + 404*x^5 + 1435*x^4 + 3906*x^3 + 7185*x^2 + 2762*x
f2 is x^7 + 18*x^6 + 144*x^5 + 695*x^4 + 2260*x^3 + 4929*x^2 + 5586*x + 2160

Looking at permutations of length 9
f1 is x^9 + 15*x^8 + 116*x^7 + 626*x^6 + 2633*x^5 + 8920*x^4 + 23699*x^3 + 42973*x^2 + 15793*x
f2 is x^8 + 21*x^7 + 200*x^6 + 1175*x^5 + 4816*x^4 + 14358*x^3 + 29833*x^2 + 32642*x + 11730
'''

# Data from Anders's Haskell module
a = [1]
b = [1, 2]
c = [2, 9, 4]
d = [6, 42, 33, 8]
e = [23, 213, 225, 98, 16]

L = d
f = 0
for i in range(len(L)):
    f = f + L[i]*binomial(x,i)

print f
print expand(f)
print factor(f)