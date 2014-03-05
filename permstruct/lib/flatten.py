
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

