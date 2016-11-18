# Defining the generating functions for the decreasing and increasing perms
# D, I = var('D, I')
D = 1/(1-x)
I = 1/(1-x)

# print "Patterns: 123, 132"
B31 = var('B31')
eq = 1 + x*D*B31 - B31
sols = solve(eq == 0, B31, solution_dict = True)
# print sols
# print sols[0][B31].series(x, 15)
B31 = sols[0][B31] # Needed later

print "Skew-merge"
print ""

print "Patterns: 2143_2413_3142_3412"
F  = var('F')
eq = 1 + x*F + x*(F-1)*(B31-1) + x^2*(F-1)*(B31-1)*D + x*(F-1)*D- F
sols = solve(eq == 0, F, solution_dict = True)
print sols
print sols[0][F].series(x, 15)
print ""

print "--------------------------------------"
