import sys; sys.dont_write_bytecode = True; from utils import *
"""
To do: ensure Code Runner works (in WSL), have preloaded the day and input in Chrome,
saved input into the folder, have utils on the side, collapse regions
Strings, lists, dicts:
lmap, ints, positive_ints, floats, positive_floats, words, keyvalues

Algorithms:
bisect, binary_search, hamming_distance, edit_distance

Data structures:
Linked, UnionFind
use deque for queue: q[0], q.append and q.popleft

List/Vector operations:
GRID_DELTA, OCT_DELTA
lget, lset, fst, snd
padd, pneg, psub, pmul, pdot, pdist1, pdist2sq, pdist2

Matrices:
matmat, matvec, matexp

Previous problems:
knot

Dict things:
dict.keys()
dict.values()
dict.items()
"""

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)

    lines = inp.splitlines()
    G = defaultdict()

    for line in lines:
        a, b = line.split(':')
        G[a] = b.strip().split(' ')

    def solve(g) -> int:
        dp = defaultdict()
        indeg = defaultdict()
        nxt = deque(['svr'])
        seen = set()
        while len(nxt):
            cur = nxt.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            if g.get(cur) == None:
                continue
            for x in g[cur]:
                indeg.setdefault(x, 0)
                indeg[x] += 1
                nxt.append(x)
        dp['svr'] = 1
        dp['out'] = 0
        nxt = ['svr']
        while len(nxt):
            nnxt = []
            for cur in nxt:
                if cur == 'out':
                    continue
                for x in g[cur]:
                    dp.setdefault(x, 0)
                    dp[x] += dp[cur]
                    indeg[x] -= 1
                    if indeg[x] == 0:
                        nnxt.append(x)
            nxt = nnxt
        return dp['out']
    def remove(g, s):
        ret = defaultdict()
        for k, v in g.items():
            ret[k] = [x for x in v]
        del ret[s]
        for k, v in ret.items():
            if v != None and s in v:
                v.remove(s)
                ret[k] = v
        return ret
    g_no_dac = remove(G, 'dac')
    g_no_fft = remove(G, 'fft')
    g_none = remove(g_no_dac, 'fft')
    print(solve(G) - solve(g_no_dac) - solve(g_no_fft) + solve(g_none))
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
