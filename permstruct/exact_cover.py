from subprocess import Popen, PIPE

def exact_cover(settings, bss):
    assert settings.allow_overlap_in_first or settings.ignore_first == 0, "Not supported"
    bss = [ bs >> settings.ignore_first for bs in bss ]

    width = settings.sinput.validcnt
    n = len(bss)
    clauses = []
    for i in range(width):
        need = []
        for j in range(len(bss)):
            if (bss[j] & (1<<i)) != 0:
                need.append(j+1)
        clauses.append(need)

    for i in range(len(bss)):
        for j in range(i+1, len(bss)):
            if (bss[i]&bss[j]) != 0:
                clauses.append([ -(i+1), -(j+1) ])

    lines = []
    lines.append('p cnf %d %d' % (len(bss), len(clauses)))
    for cl in clauses:
        lines.append(' '.join(map(str, cl + [0])))

    inp = '\n'.join(lines)

    p = Popen(['lingeling'], stdin=PIPE, stderr=PIPE, stdout=PIPE)
    p.stdin.write(inp)
    p.stdin.flush()
    p.stdin.close()
    p.wait()
    res = p.stdout.read()
    found = False
    used = set()
    for line in res.split('\n'):
        if line.startswith('s '):
            found = line.strip().split()[1] == 'SATISFIABLE'
        elif line.startswith('v '):
            for num in map(int, line.strip().split()[1:]):
                if num > 0:
                    used.add(num-1)

    yield sorted(used)

def exact_cover_lb(settings, bss):

    lens = [ len(settings.sinput.permutations[l]) for l in range(settings.sinput.perm_bound+1) ]

    curcover = []
    ball = (1 << settings.sinput.validcnt) - 1
    care = ball & ~((1 << settings.ignore_first) - 1)
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
            if buck[i] < lens[i]*settings.lower_bound:
                ok = False
                break

        if ok or (done & care) == (ball & care):
            yield list(curcover)
        elif not (left == 0 or at == len(bss)):
            if (bss[at] & done & (care if settings.allow_overlap_in_first else ball)) == 0:
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

