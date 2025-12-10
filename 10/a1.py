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
    INF = 0x7fff
    def sprint(*a, **k): sample and print(*a, **k)
    def solve(line: str) -> int:
        target, remain = line.split(']')
        target = functools.reduce(lambda x, y: (x << 1) + (1 if y == '#' else 0), list(target[-1:0:-1]), 0)
        masks = [functools.reduce(lambda x, y: x + (1 << y), ints(btn), 0) for btn in remain.split(')')[:-1]]

        @functools.lru_cache(maxsize=None)
        def search(target, i) -> int:
            if target == 0:
                return 0
            if i == len(masks):
                return INF
            return min(1 + search(target ^ masks[i], i + 1), search(target, i + 1))
        return search(target, 0)


    lines = inp.splitlines()
    ans = 0
    for line in lines:
        ans += solve(line)
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
