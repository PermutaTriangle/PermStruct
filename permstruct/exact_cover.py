
def exact_cover_lb(bss, validcnt, max_cnt, ignore_first, allow_overlap_in_first, lens, lower_bound):
    curcover = []
    ball = (1 << validcnt) - 1
    care = ball & ~((1 << ignore_first) - 1)
    buck = [0]*len(lens)
    buckadd = []
    for i in range(len(bss)):
        cur = [0]*len(lens)
        at = 0
        for k in range(len(lens)):
            for j in range(lens[k]):
                if ((bss[i]>>at)&1) != 0:
                    cur[k] += 1
                at += 1
        buckadd.append(cur)

    def bt(at, left, done):
        ok = True
        for i in range(len(lens)):
            if buck[i] < lens[i]*lower_bound:
                ok = False
                break

        if ok or (done & care) == (ball & care):
            yield list(curcover)
        elif not (left == 0 or at == len(bss)):
            if (bss[at] & done & (care if allow_overlap_in_first else ball)) == 0:
                curcover.append(at)

                for i in range(len(lens)):
                    buck[i] += buckadd[at][i]

                for res in bt(at + 1, left - 1, done | bss[at]):
                    yield res

                for i in range(len(lens)):
                    buck[i] -= buckadd[at][i]

                curcover.pop()

            for res in bt(at + 1, left, done):
                yield res

    return bt(0, max_cnt, 0)

