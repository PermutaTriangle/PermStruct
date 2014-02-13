
from permutation_sets import Point, Input, SimpleGeneratingRule, GeneratingRule

def generate_all_of_length(max_n, S, inp):

    inp = dict(inp)

    for n in range(max_n+1):
        for perm in S.generate_of_length(n, inp):
            inp.setdefault(n, [])
            inp[n].append(perm)

    return inp


# Shorthands, maybe include this in the library?
I = Input()
P = Point()
empty = {0:[Permutation([])]}

# Increasing permutations
incr = SimpleGeneratingRule(Permutation([1,2]), [I, P])

# Decreasing permutations
decr = SimpleGeneratingRule(Permutation([2,1]), [I, P])

# Avoiders of 231 and 312
avoid_231_312 = SimpleGeneratingRule(Permutation([1,3,2]), [I, P, decr.to_static(10, empty)])

avoid_231_312_G = GeneratingRule([
    [None, P, None],
    [None, None, decr.to_static(10, empty)],
    [I, None, None],
])

avoid_vinc_3_12_ = GeneratingRule([
    [None, P, None],
    [I, None, decr.to_static(10,empty)]
])


print(generate_all_of_length(6, incr, empty))
print(generate_all_of_length(6, decr, empty))
print(generate_all_of_length(5, avoid_231_312, empty))

res = generate_all_of_length(10, avoid_231_312, empty)
for i in range(1, 11):
    assert len(res[i]) == 2**(i-1)

