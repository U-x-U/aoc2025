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

def transpose(lines: list(str)) -> list(str):
    nrows, ncols = len(lines), len(lines[0])
    ret = [''] * ncols
    for j in range(ncols):
        for i in range(nrows):
            ret[j] += lines[i][j]
    return ret
allwhite = lambda s: s.strip() == ''
def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    ops = lines[-1].split()
    trspsd = transpose(lines[:-1])

    tot = 0
    idx = 0
    v = 1 if ops[idx] == '*' else 0
    for line in trspsd:
        if allwhite(line):
            tot += v
            if idx + 1 < len(ops):
                idx += 1
                v = 1 if ops[idx] == '*' else 0
            continue
        if ops[idx] == '*':
            v *= int(line)
        else:
            v += int(line)
    if not allwhite(trspsd[-1]):
        tot += v
    print(tot)
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


###
# 1  
# 24 
# 356
#   
# 369
# 248
# 8
#    
#  32
# 581
# 175
#
# 623
# 431
#   4
###
run_samples_and_actual([
# Part 1
r"""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)
