import itertools

'''
Create all sum-type generating rules on an nxm grid
'''

def sumTs(n, m):
    
    b = min(n, m)
    
    pts = [((), [n], [m])]
    
    for s in range(1, b+1):
        
        pts = pts + list( itertools.product( Permutations(s),IntegerVectors(n-s,s+1),IntegerVectors(m-s,s+1) ) )
    
    unshadings = [((),[n+1],[m+1])]
    
    for s in range(1,b+2):
        
        unshadings = unshadings + list( itertools.product( Permutations(s),IntegerVectors(n+1-s,s+1),IntegerVectors(m+1-s,s+1) ) )
                        
    return CartesianProduct(pts,unshadings)