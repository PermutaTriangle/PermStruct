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
'''

B = 5

permProp  = (lambda perm : perm.avoids([2,3,1]))
permCount = (lambda n : len(filter(lambda x : permProp(x), Permutations(n))) )
overl     = (lambda n : 1)
compl     = (lambda n : 1)
atoms = [Permutation([])]

for N in range(1,6):
    for sumT in sumTs(N):
        #print sumT
        cr = createFromSumType( sumT, atoms, B, 1, permProp, permCount, overl, compl, report = False )
        if len(cr) > len(atoms):
            print sumT
            print cr
            print len(cr)
            print ""