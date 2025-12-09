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
    points = [ints(line) for line in lines]
    segments = list(zip(points, points[1:] + [points[0]]))

    ### visualization
    # import matplotlib.pyplot as plt
    #
    # fig, ax = plt.subplots()
    # for (x1, y1), (x2, y2) in segments:
    #     ax.plot([x1, x2], [y1, y2], linewidth=2)
    #
    # ax.set_aspect('equal', adjustable='box')
    # ax.grid(True)
    # plt.savefig("sample.jpg" if sample else "vis.jpg")

    ans = 0
    for i in range(1, len(points)):
        x1, y1 = points[i][0], points[i][1]
        for j in range(i):
            x2, y2 = points[j][0], points[j][1]
            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)

            def segment_no_pass(segment, x_min, x_max, y_min, y_max):
                x1, x2, y1, y2 = segment[0][0], segment[1][0], segment[0][1], segment[1][1]
                if x1 == x2:
                    return x1 <= x_min or x_max <= x1 \
                            or y1 <= y_min and y2 <= y_min \
                            or y_max <= y1 and y_max <= y2
                assert(y1 == y2)
                return y1 <= y_min or y_max <= y1 \
                        or x1 <= x_min and x2 <= x_min \
                        or x_max <= x1 and x_max <= x2

            if not any(map(lambda p: x_min < p[0] and p[0] < x_max and y_min < p[1] and p[1] < y_max, points)) \
                    and all(map(lambda segment: segment_no_pass(segment, x_min, x_max, y_min, y_max), segments)):
                ans = max(ans, (x_max - x_min + 1) * (y_max - y_min + 1))
    print(ans)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
