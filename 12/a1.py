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

    # def getmask(mat, row_reverse, col_reverse)->(int, int, int):
    #     mask = []
    #     for line in mat[::-1 if row_reverse else 1]:
    #         x = 0
    #         for ch in line[::-1 if col_reverse else 1]:
    #             x <<= 1
    #             x += ch == '#'
    #         mask.append(x)
    #     return tuple(mask)
    #
    lines = inp.splitlines()
    # presents = []
    areas = []
    ans = 0
    # def search(x, y, reqs) -> bool:
    #     for i, cnt in enumerate(reqs):
    #         # put `cnt` presents[i] to the X-Y region
    #         for _ in range(cnt):
    #             put()
    #             presents[i]
    for i in range(6):
    #     masks = set()
        mat = lines[5*i+1: 5*i+4]
        areas.append(sum([ch == '#' for ch in ''.join(mat)]))
    #     mat1 = [[mat[j][i] for j in range(3)] for i in range(3)]
    #     for row_reverse, col_reverse in itertools.permutation([True, False], 2):
    #         masks.add(getmask(mat, row_reverse, col_reverse))
    #         masks.add(getmask(mat1, row_reverse, col_reverse))
    #     presents.append(masks)
    for line in lines[30:]:
        dimension, reqs = map(ints, line.split(':'))
        x, y = dimension
        # ans += search(x, y, reqs)
        total_area = 0
        for i, req in enumerate(reqs):
            total_area += req * areas[i]
        if total_area > x * y:
            continue
        tot_cnt = sum(reqs)
        if x // 3 * y // 3 >= tot_cnt:
            ans += 1
            continue
        print("that's hard") # none of them are hard:)
    print('ans >= ', ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
