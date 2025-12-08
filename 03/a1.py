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
    def calc(s) -> int:
        a, b = s[0], s[1]
        c = b if a < b else ''
        for d in s[2:]:
            if c != '' and c > a:
                a = c
                b = d
                c = ''
            if d > b:
                b = d
            if d > a:
                c = d
        return int(a+b)
    def calc1(s) -> int:
        mx = max(s)
        idx = s.find(mx)
        if idx == len(s) - 1:
            return int(max(s[:-1])+mx)
        return int(mx + max(s[idx+1:]))
    for s in lines:
        if calc(s) != calc1(s):
            print('----------', s, calc1(s))
    print(sum(map(calc1, lines)))

    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD



run_samples_and_actual([
# Part 1
r"""
987654321111111
811111111111119
234234234234278
818181911112111
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
