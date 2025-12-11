from itertools import permutations


def solve(joltages_left, pushes_done, buttons):
    global fewest_pushes

    if min(joltages_left) < 0:
        return

    if max(joltages_left) >= fewest_pushes - pushes_done:
        return

    if max(joltages_left) == 0:
        fewest_pushes = min(fewest_pushes, pushes_done)
        return

    push = lambda b: [j-(i in b) for i,j in enumerate(joltages_left)]
    push_n = lambda b, n: [j-n*(i in b) for i,j in enumerate(joltages_left)]

    for i, j in impossible_list[len(buttons)]:
        if joltages_left[i] > joltages_left[j]:
            return
    for k, v in useful_dict[len(buttons)].items():
        i, j = k
        if joltages_left[i] > joltages_left[j]:
            cnt = joltages_left[i] - joltages_left[j]
            return solve(push_n(v, cnt), pushes_done+cnt, buttons)
    for i, button in enumerate(buttons):
        solve(push(button), pushes_done+1, buttons[i:])

total_pushes = 0

for _, *buttons, joltage in map(str.split, open('input.txt')):
    buttons = sorted([eval(b[:-1]+',)') for b in buttons], key=lambda b: len(b), reverse=True)
    joltage = eval(joltage[1:-1])

    impossible_list = [[] for _ in range(len(buttons) + 1)]
    useful_dict = [dict() for _ in range(len(buttons) + 1)]
    for idx in range(len(buttons)):
        for i, j in permutations(range(len(joltage)), 2):
            useful = [b for b in buttons[idx:] if i in b and j not in b]
            if len(useful) == 0:
                impossible_list[len(buttons[idx:])].append((i, j))
            if len(useful) == 1:
                useful_dict[len(buttons[idx:])][(i, j)] = useful[0]

    fewest_pushes = sum(joltage) // min([len(b) for b in buttons])
    solve(joltage, 0, buttons)
    total_pushes += fewest_pushes

print(total_pushes)
