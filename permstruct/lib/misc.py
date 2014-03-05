
import bisect

def binary_search(a, x):
    i = bisect.bisect_left(a, x)
    return i != len(a) and a[i] == x


def flatten(lst):
    res = []
    def dfs(l):
        for i in l:
            if type(i) in {list,tuple}:
                dfs(i)
            else:
                res.append(i)
    dfs(lst)
    return res

