import functools
import sys
from itertools import permutations, combinations_with_replacement, product, pairwise

f = open('./input', 'r')

UP, DOWN, LEFT, RIGHT = "^v<>"

numpad = [
    [7,8,9],
    [4,5,6],
    [1,2,3],
    [None, 0, "A"]
]
num = {
    str(numpad[y][x]): (x,y)
    for y in range(len(numpad))
    for x in range(len(numpad[0]))
}
print(num)
keypad = [
    [None, UP, "A"],
    [LEFT, DOWN, RIGHT]
]
key = {
    str(keypad[y][x]): (x,y)
    for y in range(len(keypad))
    for x in range(len(keypad[0]))
}


def get_paths(keyboard):
    all_paths = {}
    for start, end in product(keyboard.keys(), repeat=2):
        if start == "None" or end == "None":
            continue

        tx, ty = keyboard[end]

        stack = [(keyboard[start], "")]
        paths = []

        while stack:
            (x, y), p = stack.pop()
            if keyboard["None"] == (x, y):
                continue
            if x == tx and y == ty:
                paths.append(p+"A")
                continue

            if x < tx:
                stack.append(((x+1, y), p+RIGHT))
            if x > tx:
                stack.append(((x-1, y), p+LEFT))
            if y < ty:
                stack.append(((x, y+1), p+DOWN))
            if y > ty:
                stack.append(((x, y-1), p+UP))

        all_paths[start, end] = paths
    return all_paths
#
#
# def get_paths(keyboard):
#     all_paths = {}
#     for start, end in product(keyboard.keys(), repeat=2):
#         if start == "None" or end == "None":
#             continue
#
#         x, y = keyboard[start]
#         xx,yy = keyboard[end]
#         dx, dy = xx-x, yy-y
#
#         hor = LEFT if dx < 0 else RIGHT
#         ver = UP if dy < 0 else DOWN
#
#         if dx == 0 and dy == 0:
#             paths = ["A"]
#         elif dx == 0:
#             paths = [ver*abs(dy) + "A"]
#         elif dy == 0:
#             paths = [hor*abs(dx) + "A"]
#         else:
#             first_hor = hor*abs(dx) + ver*abs(dy) + "A"
#             first_ver = ver*abs(dy) + hor*abs(dx) + "A"
#             nx, ny = keyboard["None"]
#
#             if x == nx and yy == ny:
#                 paths = [first_hor]
#             elif xx == nx and y == ny:
#                 paths = [first_ver]
#             else:
#                 paths = [first_ver, first_hor]
#
#         all_paths[start, end] = paths
#     return all_paths


num_paths = get_paths(num)
key_paths = get_paths(key)


@functools.cache
def shortest(code, depth, max_depth):
    if depth == max_depth:
        return len(code)

    paths = num_paths if depth == 0 else key_paths

    b = 0
    for start, end in pairwise("A" + code):
        b += min(
            shortest(p, depth+1, max_depth)
            for p in paths[start,end]
        )

    return b

a1 = 0
a2 = 0
for line in f.readlines():
    line = line.strip()
    if not line:
        continue

    b1 = shortest(line, 0, 3)
    a1 += int(line[:-1]) * b1
    b2 = shortest(line, 0, 26)
    a2 += int(line[:-1]) * b2
    print(int(line[:-1]), b1, b2)

print(a1, a2)




if __name__ == "__main__":
    pass
