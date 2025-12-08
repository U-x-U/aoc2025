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

    lines = [list(line) for line in inp.splitlines()]
    nrows, ncols = len(lines), len(lines[0])
    ans = 0
    toremove = set()
    npapers = [[0] * ncols for _ in range(nrows)]

    for i in range(nrows):
        for j in range(ncols):
            if lines[i][j] != '@':
                continue
            for d in OCT_DELTA:
                ni, nj = i + d[0], j + d[1]
                if nrows <= ni or ni < 0 or ncols <= nj or nj < 0 or lines[ni][nj] != '@':
                    continue
                npapers[i][j] += 1
            if npapers[i][j] < 4:
                toremove.add((i, j))
    while len(toremove):
        i, j = toremove.pop()
        lines[i][j] = 'X'
        ans += 1
        for d in OCT_DELTA:
            ni, nj = i + d[0], j + d[1]
            if nrows <= ni or ni < 0 or ncols <= nj or nj < 0 or lines[ni][nj] != '@':
                continue
            npapers[ni][nj] -= 1
            if npapers[ni][nj] < 4:
                toremove.add((ni, nj))
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
