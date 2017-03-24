from subprocess import Popen, PIPE
import sys
import tempfile
import shutil
import resource
import platform
import os

def exact_cover(settings, bss):
    try:
        print('Trying to start Gurobi')
        for res in exact_cover_gurobi(settings, bss):
            yield res
        print('Gurobi was found')
    except Exception as e:
        print('No Gurobi found or Gurobi failed, with the error')
        print(e)
        try:
            print('Trying Lingeling:')
            for res in exact_cover_lingeling(settings, bss):
                yield res
        except Exception as f:
            print('Lingeling failed as well, with the error')
            print(f)

    # TODO: call Permuta's Algorithm X implementation if everything else fails

def exact_cover_gurobi(settings, bss):
    assert settings.allow_overlap_in_first or settings.ignore_first == 0, "Not supported"
    bss = [ bs >> settings.ignore_first for bs in bss ]
    width = settings.sinput.validcnt

    tdir = None
    used = set()
    anything = False
    try:
        tdir = tempfile.mkdtemp(prefix='struct_tmp')
        inp = os.path.join(tdir, 'inp.lp')
        outp = os.path.join(tdir, 'out.sol')
        #templog = os.path.join(tdir, 'templog.txt')

        with open(inp, 'w') as lp:
            lp.write('Minimize %s\n' % ' + '.join( 'x%d' % i for i in range(len(bss)) ))
            lp.write('Subject To\n')

            for i in range(width):
                here = []
                for j in range(len(bss)):
                    if (bss[j] & (1<<i)) != 0:
                        here.append(j)
                lp.write('    %s = 1\n' % ' + '.join( 'x%d' % x for x in here ))

            lp.write('Binary\n')
            lp.write('    %s\n' % ' '.join( 'x%d' % i for i in range(len(bss)) ))
            lp.write('End\n')
        
        print('The inp.lp file has been created')
        print('The size of the inp.file is %s Mb' %(os.path.getsize(inp)//2**20))
        if platform.system() == 'Darwin':
            print('The peak memory used so far is %s Mb' %(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//2**20)) # getrusage returns in bytes on OS X
        else:
            print('The peak memory used so far is %s Mb' %(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//2**10)) # but kilobytes on Linux
        print('Starting Gurobi')
        #p = Popen('gurobi_cl ResultFile=%s %s' % (outp, inp), shell=True, stdout=PIPE, stderr=PIPE)
        #p = Popen('gurobi_cl LogFile=%s ResultFile=%s %s' % (templog, outp, inp), shell=True)
        #p = Popen('gurobi_cl LogFile=%s ResultFile=%s %s' % (templog, outp, inp), shell=True, stdout=PIPE, stderr=PIPE)
        p = Popen('gurobi_cl Method=1 ResultFile=%s %s' % (outp, inp), shell=True, stdout=PIPE, stderr=PIPE)
        print('Made it past Popen')
        output, error = p.communicate()
        if p.returncode != 0:
            print(p.returncode, output, error)
        else:
            print('returncode = %s' %p.returncode)
            print(output)
        assert p.wait() == 0
        print('Made it through Gurobi')

        #with open(templog, 'r') as fin:
        #    print(fin.read())

        with open(outp, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.startswith('#') or not line.strip():
                    continue
                anything = True
                k,v = line.strip().split()
                if abs(float(v) - 1) < 0.1:
                    used.add(int(k[1:]))
    finally:
        if tdir is not None:
            shutil.rmtree(tdir)

    if anything:
        yield sorted(used)

def exact_cover_lingeling(settings, bss):
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
    p.stdin.write(inp.encode('utf-8'))
    p.stdin.flush()
    p.stdin.close()
    p.wait()
    res = str(p.stdout.read().decode('utf-8'))
    found = False

    used = set()
    for line in res.split('\n'):
        if line.startswith('s '):
            found = line.strip().split()[1] == 'SATISFIABLE'
        elif line.startswith('v '):
            for num in map(int, line.strip().split()[1:]):
                if num > 0:
                    used.add(num-1)

    if found:
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

