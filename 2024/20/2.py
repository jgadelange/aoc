import sys
from collections import defaultdict

f = open('./input', 'r')

g = [
    l.strip()
    for l in f.readlines()
    if l.strip()
]

h, w = len(g), len(g[0])

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

ADJ_ORT = [N, E, S, W]


def in_bounds(x, y):
    return 0 <= x < w and 0 <= y < h


start = next((x,y) for x in range(w) for y in range(h) if g[y][x] == "S")
end = next((x,y) for x in range(w) for y in range(h) if g[y][x] == "E")

found = False
i = 0
q = [(*start, -2)]
possible_cheats = {}
dist = {}

no_cheat = {}
while q:
    if -2 in possible_cheats:
        break
    nq = []

    for x, y, cheated_at in q:
        dist[(x, y)] = min(dist.get((x, y), sys.maxsize), i)
        if cheated_at in possible_cheats:
            continue
        if (x,y) == end:
            possible_cheats[cheated_at] = i
            continue

        check_collisions = cheated_at != i-1

        for dx, dy in ADJ_ORT:
            xx, yy = x + dx, y + dy
            if not in_bounds(xx, yy):
                continue

            if (xx, yy) not in dist:
                if check_collisions:
                    if g[yy][xx] != "#":
                        nq.append((xx, yy, cheated_at))
                else:
                    nq.append((xx, yy, cheated_at))
            #
            # if cheated_at == -2 and g[yy][xx] == "#":
            #     nq.append((xx, yy, i))
    q = nq
    i += 1

possible_cheats = {}

for (cx,cy), d in dist.items():
    if (cx, cy) in possible_cheats:
        continue

    q = [(cx,cy)]
    visited = set()
    for i in range(21):
        nq = []
        for (x, y) in q:
            if (x,y) in dist:
                possible_cheats[(cx,cy, x, y)] = max(possible_cheats.get((cx,cy,x,y), 0), dist[(x,y)] - d - i)
                # continue
            for dx, dy in ADJ_ORT:
                xx, yy = x + dx, y + dy
                if in_bounds(xx, yy) and (xx,yy) not in visited:
                    visited.add((xx,yy))
                    nq.append((xx, yy))
        q = nq
#
# print(possible_cheats)
# saves = defaultdict(int)
# for cheat in possible_cheats.values():
#     saves[cheat] += 1
# print(saves)
print(len([v for v in possible_cheats.values() if v>=100]))

if __name__ == "__main__":
    pass
