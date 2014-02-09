import itertools


'''
A permutation of length s+t for a rule with s points and t unshaded
boxes. We "mark" the s points on the permutation to remember which correspond to points.
'''

def sumTs(n):
    
    return CartesianProduct(Permutations(n), Subsets(range(n)))

def createFromSumType( sumT, atoms, B, b = 1, permProp = (lambda perm : True), permCount = (lambda n : 0), overl = (lambda n : 1), compl = (lambda n: 1), report = False ):
    
    created = {}
    
    # Putting the atoms in the dictionary by length
    for atom in atoms:
        created.setdefault(len(atom),[])
        created[len(atom)].append(atom)
    
    rulePerm  = sumT[0]
    nrulePerm = len(rulePerm)
    pts       = sumT[1]
    npts      = pts.cardinality()
    
    if npts == 0:
        if report:
            print "We do not currently support rules without points"
        return created
    
    rulePermInv = rulePerm.inverse()
    
    nfree = nrulePerm-npts
    
    for n in range(b, B+1):
        
        # Need to be careful if there are atoms of length n        
        created.setdefault(n,[])
        
        if nfree == 0 and nrulePerm == n:
            created[n].append(rulePerm)
        
        for oPart in IntegerVectors(n - npts, nfree):
            
            for elt in itertools.product(*map( lambda x : created[x], oPart )):
                
                #print elt
                outPerm = [None]*nrulePerm
                
                cumul = 0
                used  = 0
                for ind in rulePermInv:
                    #print "ind", ind
                    
                    # if ind is marked
                    if ind-1 in pts:
                        cumul += 1
                        outPerm[ind-1] = cumul
                    else:
                        new = elt[used]
                        used += 1
                        outPerm[ind-1] = map( lambda x : x + cumul, new)
                        cumul += len(new)
                        
                outPerm = Permutation(flatten(outPerm))
                
                if not permProp(outPerm):
                    if report:
                        print "Generated the permutation ", outPerm, " which does not satisfy the property"
                    return {}
                        
                created[n].append(outPerm)
        
        if len(created[n]) < compl(n)*permCount(n):
            if report:
                print "The rule creates too few permutations of length ", n
            return {}
        
        if Set(created[n]).cardinality() < overl(n) * len(created[n]):
            if report:
                print "The rule is too overlapping"
            return {}
                
    return created

'''
Testing

B         : Look for generating rules of sizes 1 through B-1
permProp  : The defining property of the set of permutations you are looking at
permCount : How many permutations of length n have this property
over      : How much overlap to allow. 1 = no overlap, 1/2 = on average each permutation in
            the set may be generated twice
compl     : What kind of coverage you want. 1 = complete coverage, 1/2 = at least half of
            the permutations in the set are generated
atoms     : The list of permutations to start with

------------------- Nice examples that work -------------------

Unless otherwise stated assume

permCount = (lambda n : len(filter(lambda x : permProp(x), Permutations(n))) )
overl     = (lambda n : 1)
compl     = (lambda n : 1)
atoms     = [Permutation([])]

1) Decreasing permutations
permProp  = (lambda perm : perm.avoids([1,2]))

[[2, 1], {0}]
[[2, 1], {1}]

2) Increasing permutations
permProp  = (lambda perm : perm.avoids([1,2]))

[[1, 2], {0}]
[[1, 2], {1}]

Avoiders of a single non-monotone pattern of length 3, e.g.,
3) Avoiders of 213
permProp  = (lambda perm : perm.avoids([2,1,3]))

[[2, 3, 1], {0}]
[[3, 1, 2], {1}]

------------------- Examples that might work with more general rules -------------------

Unless otherwise stated assume

permCount = (lambda n : len(filter(lambda x : permProp(x), Permutations(n))) )
overl     = (lambda n : 1)
compl     = (lambda n : 1)
atoms     = [Permutation([])]

1) Avoiders of a single monotone pattern of length 3, e.g.,
permProp  = (lambda perm : perm.avoids([1,2,3]))

Tested up to B = 6.
It is well known that there is a rule of size two (two boxes free) where
we put in decreasing permutations.

Avoiders of two patterns of length 3. Below we have all combinations up to symmetry.
-----------------------------------------------------------------------
2) Avoiders of 123 and 321. This class dies out, so probably no "nice" rule to
describe it
permProp  = (lambda perm : perm.avoids([1,2,3]) and perm.avoids([3,2,1]))

Tested up to B = 6.
Found nothing as expected.

3) Avoiders of 123 and 231. I think you need to rules to describe this class and
one of the rules requires putting monotone permutations in a box so we shouldn't
expect to find any rules yet.
permProp  = (lambda perm : perm.avoids([1,2,3]) and perm.avoids([2,3,1]))

Tested up to B = 6.
Found nothing as expected.

4) Avoiders of 123 and 132. Don't have a feeling for this set.
permProp  = (lambda perm : perm.avoids([1,2,3]) and perm.avoids([1,3,2]))

Tested up to B = 6.

-----------------------------------------------------------------------

Avoiders of one pattern of length 3 and one of length 4
-----------------------------------------------------------------------
5) Avoiders of 321 and 1234. This class dies out, so probably no "nice" rule
to describe it
permProp  = (lambda perm : perm.avoids([3,2,1]) and perm.avoids([1,2,3,4]))

Tested up to B = 7.

6) Avoiders of 321 and 2134.
permProp  = (lambda perm : perm.avoids([3,2,1]) and perm.avoids([2,1,3,4]))

Tested up to B = 7.

7) Avoiders of 132 and 4321.
permProp  = (lambda perm : perm.avoids([1,3,2]) and perm.avoids([4,3,2,1]))

Tested up to B = 7.

8) Avoiders of 321 and 1324.
permProp  = (lambda perm : perm.avoids([3,2,1]) and perm.avoids([1,3,2,4]))

Tested up to B = 7.

9) Avoiders of 321 and 1343.
permProp  = (lambda perm : perm.avoids([3,2,1]) and perm.avoids([1,3,4,2]))

Tested up to B = 7.

9) Avoiders of 321 and 2143.
permProp  = (lambda perm : perm.avoids([3,2,1]) and perm.avoids([2,1,4,3]))

Tested up to B = 7.

To be continued ...
-----------------------------------------------------------------------
'''

B = 7

permProp  = (lambda perm : perm.avoids([4,3,2,1]) and perm.avoids([4,3,1,2]))
permCount = (lambda n : len(filter(lambda x : permProp(x), Permutations(n))) )
overl     = (lambda n : 1)
compl     = (lambda n : 1)
atoms     = [Permutation([])]

for N in range(1,6):
    for sumT in sumTs(N):
        #print sumT
        cr = createFromSumType( sumT, atoms, B, 1, permProp, permCount, overl, compl, report = False )
        if len(cr) > len(atoms):
            print sumT
            print cr
            print len(cr)
            print ""