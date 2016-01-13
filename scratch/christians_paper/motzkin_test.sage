def G(w):
    """
    The graph/diagram of the permutation w
    """
    return [ (x+1,y) for (x,y) in enumerate(w) ]
#
# Plotting mesh patterns
#

def plot_mesh_patt(p):

    s = list(p[0])
    R = Set(p[1])
    
    n = len(s)

    #L = text( '', (0,0) )
    L = Graphics()
    # added the text so the axes are centered at (0,0)
    
    # Drawing the shading
    for r in R:
        
        x = r[0]
        y = r[1]
        
        L += polygon2d([ r, (x+1,y), (x+1,y+1), (x,y+1)], alpha = 0.5, rgbcolor=(1,1/4,1/2))
    
    # Drawing the lines
    for i in [1..n]:
        
        L += line2d([(i,0),(i,n+1)], rgbcolor=(0,0,0), thickness = 2) + line2d([(0,i),(n+1,i)], rgbcolor=(0,0,0), thickness = 2)
        
    # Drawing the dots
    for i in [1..n]:
        
        L += point2d([(i,s[i-1])], color = 'black', size = 200)
       
    return L

# Plotting many mesh patterns (m in each row)
def visualize_patts(SG,m=4):

    if len(SG) <= m:
        g = graphics_array([ plot_mesh_patt(sg) for sg in SG])
        g.show(frame=True, axes=False, figsize=[14,2+8/m], aspect_ratio = 1)
    else:
        stop = int(len(SG)/m)
        if mod(len(SG),m) == 0:
            stop = stop -1

        for i in [0..stop]:
            g = graphics_array([ plot_mesh_patt(SG[j]) for j in [i*m..(i+1)*m-1] if j < len(SG)])
            g.show(frame=True, axes=False, figsize=[14,2+8/m], aspect_ratio = 1)

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

def avoids_mpat_many_shadings(perm, pat, Rs):
    """
    Returns False if (pat, R) occurs in perm for any R in Rs, otherwise returns True
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
            for R in Rs:
                shady = ( X[i] < x < X[i+1] and Y[j] < y < Y[j+1]
                          for (i,j) in R
                          for (x,y) in perm
                          )
                if not any(shady):
                    return False
    return True

def avoids_mpats(perm,pats):
    """
    Returns False if any pattern from pats occurs in perm, otherwise returns True
    """
    
    for pat in pats:
        
        if avoids_mpat(perm,pat[0],pat[1]) == False:
            return False
            
    return True

def avoids_mpats_many_shadings(perm,pats_w_shadings):
    """
    Returns False if any pattern from pats occurs in perm, otherwise returns True
    """
    for n in pats_w_shadings.keys():
        for pat in pats_w_shadings[n].keys():
        
            if avoids_mpat_many_shadings(perm,pat,pats_w_shadings[n][pat]) == False:
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

def occs_mpat(perm, pat, R=[]):
    """
    Returns the copies/occurrences of (pat, R) in perm
    """
    occs = []
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
                occs.append((H[0][0]-1,H[1][0]-1))
    return occs

def perms_avoiding(M,n):
            
    return filter(lambda perm: avoids_mpat(perm,M[0],M[1]), Permutations(n))

def perms_containing(M,n):
            
    return filter(lambda perm: not avoids_mpat(perm,M[0],M[1]), Permutations(n))

# Parallel version of perms_avoiding_many
@parallel
def para_subs_perms_avoiding_many(v,cps,n,Ms):
    """
    Helper function for the function below
    """
    
    return filter( lambda x: avoids_mpats(x,Ms), map( lambda y: Permutations(n)[y], xrange(v,factorial(n),cps) ) )

@parallel
def para_subs_perms_avoiding_many_many_shadings(v,cps,n,Ms):
    """
    Helper function for the function below
    """
    
    return filter( lambda x: avoids_mpats_many_shadings(x,Ms), map( lambda y: Permutations(n)[y], xrange(v,factorial(n),cps) ) )
    
def para_perms_avoiding_many(N,Ms):
    """
    Returns a dictionary where the key n points to the permutations in S_n that avoid the mesh patterns in Ms
    """
    D = dict()
    
    cps = sage.parallel.ncpus.ncpus()
    
    for n in [1..N]:
        
        D[n] = sum( map( lambda x: x[1], para_subs_perms_avoiding_many( map( lambda y: (y,cps,n,Ms) , range(cps) ) ) ), [] )
        
    return D

def para_perms_in_avoiding_many_one_layer(n,Ms):
    """
    Returns the permutations in S_n that avoid the mesh patterns in Ms
    """
    
    cps = sage.parallel.ncpus.ncpus()
        
    return sum( map( lambda x: x[1], para_subs_perms_avoiding_many( map( lambda y: (y,cps,n,Ms) , range(cps) ) ) ), [] )

def para_perms_in_avoiding_many_one_layer_many_shadings(n,Ms):
    """
    Returns the permutations in S_n that avoid the mesh patterns in Ms
    """
    
    cps = sage.parallel.ncpus.ncpus()
        
    return sum( map( lambda x: x[1], para_subs_perms_avoiding_many_many_shadings( map( lambda y: (y,cps,n,Ms) , range(cps) ) ) ), [] )

# Parallel version of perms_sat_prop
@parallel
def para_subs_perms_sat_prop(v,cpus,n,prop):
    
    return filter( lambda x: prop(x), map( lambda y: Permutations(n)[y], xrange(v,factorial(n),cpus) ) )
    
def para_perms_sat_prop( N, prop, cpus=0 ):
    
    D = dict()
    
    if not cpus:
        cpus = sage.parallel.ncpus.ncpus()
    
    for n in [1..N]:
        
        D[n] = sum( map( lambda x: x[1], para_subs_perms_sat_prop( map( lambda y: (y,cpus,n,prop) , range(cpus) ) ) ), [] )
        
    return D

@parallel
def para_subs_perms_sat_prop_w_complement( v, cpus, n, prop ):

    return reduce(lambda x,y : temp_func_f_para_subs(x,Permutations(n)[y],prop), xrange(v,factorial(n),cpus), ([],[]) )
    

def temp_func_f_para_subs(x,y,prop):
    if prop(y):
        return (x[0]+[y],x[1])
    else:
        return (x[0],x[1]+[y])

    
def para_perms_sat_prop_w_complement( N, prop, cpus=0 ):
    
    D = dict()
    E = dict()
    
    if not cpus:

        cpus = sage.parallel.ncpus.ncpus()
    
    for n in [1..N]:

        (D[n],E[n]) = reduce( lambda x,y : (x[0]+y[0],x[1]+y[1]), map( lambda x: x[1], para_subs_perms_sat_prop_w_complement( map( lambda y: (y,cpus,n,prop) , range(cpus) ) ) ), ([],[]) )
        
    return D,E

def para_perms_sat_prop_w_complement_different_sizes( Ng, Nb, prop, cpus=0 ):
    
    D = dict()
    E = dict()
    
    if not cpus:
        cpus = sage.parallel.ncpus.ncpus()
    
    for n in [1..min(Ng,Nb)]:

        (D[n],E[n]) = reduce( lambda x,y : (x[0]+y[0],x[1]+y[1]), map( lambda x: x[1], para_subs_perms_sat_prop_w_complement( map( lambda y: (y,cpus,n,prop) , range(cpus) ) ) ), ([],[]) )

        print "Done with length " + str(n)
    
    for n in [Nb+1..Ng]:

        D[n] = sum( map( lambda x: x[1], para_subs_perms_sat_prop( map( lambda y: (y,cpus,n,prop) , range(cpus) ) ) ), [] )

        print "Done with length " + str(n)

    for n in [Ng+1..Nb]:

        E[n] = sum( map( lambda x: x[1], para_subs_perms_sat_prop( map( lambda y: (y,cpus,n,lambda x : not prop(x)) , range(cpus) ) ) ), [] )

        print "Done with length " + str(n)
        
    return D,E

'''
-----------------------------------------------------
'''

def rev(gpatt):
        
    patt = gpatt[0]
    G = gpatt[1]
    
    m = len(patt)
    
    npatt = Permutation(patt).reverse()

    nG = Set(sorted([(m-x,y) for (x,y) in G]))
    
    return (npatt,nG)

def inve(gpatt):
        
    patt = gpatt[0]
    G = gpatt[1]
    
    m = len(patt)
    
    npatt = Permutation(patt).inverse()
    
    nG = Set(sorted([(y,x) for (x,y) in G]))
    
    return (npatt,nG)

def compl(gpatt):
   
    patt = gpatt[0]
    G = gpatt[1]
   
    m = len(patt)
   
    npatt = Permutation(patt).complement()
   
    nG = Set(sorted([(x,m-y) for (x,y) in G]))
   
    return (npatt,nG)

# Taking the closure with respect to all symmetries

def closure_under_all_symmetries(S):
    
    newS = Set(S)
    
    for s in S:
        
        rs = rev(s)
        cs = compl(s)
        ins = inve(s)
        
        crs = compl(rev(s))
        inrs = inve(rev(s))
        incs = inve(compl(s))
        
        incrs = inve(compl(rev(s)))
        
        for symm_s in [rs,cs,ins,crs,inrs,incs,incrs]:
            
            if symm_s not in newS:
                newS = newS.union(Set([symm_s]))
                
    return newS