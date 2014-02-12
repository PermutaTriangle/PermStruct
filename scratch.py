

# def generate_all_of_length(max_n, S, inp):
def generate_all_of_length(max_n, S):

    # inp = dict(inp)
    inp = dict()

    for n in range(max_n+1):
        for perm in S.generate_of_length(n, inp):
            inp.setdefault(n, [])
            inp[n].append(perm)

    return inp


# Increasing permutations
# incr = SimpleGeneratingRule(Permutation([1,2]), [InputPermutationSet(), Point()])
incr = SimpleGeneratingRule(Permutation([1,2]), [None, Point()])
incr.sets[0] = incr  # TODO: Having to type this is boring, make construction easier

# Decreasing permutations
decr = SimpleGeneratingRule(Permutation([2,1]), [None, Point()])
decr.sets[0] = decr

# Avoiders of 231 and 312
avoid_231_312 = SimpleGeneratingRule(Permutation([1,3,2]), [None, Point(), decr])
avoid_231_312.sets[0] = avoid_231_312

print(generate_all_of_length(6, incr))
print(generate_all_of_length(6, decr))
print(generate_all_of_length(5, avoid_231_312))

res = generate_all_of_length(10, avoid_231_312)
for i in range(1, 11):
    assert len(res[i]) == 2**(i-1)

