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

q = [(*start, -2, (None, None))]
a = 0
i=0
dist2 = defaultdict(dict)
possible_cheats = dict()
while q:
    nq = []
    for x, y, cheated_at, (cx, cy) in q:
        dist2[(cx,cy)][(x, y)] = min(dist2[cx,cy].get((x, y), sys.maxsize), i)
        is_cheating = cheated_at != -2 and i < cheated_at+20
        has_cheated = cheated_at != -2 and cheated_at <= i

        if has_cheated and (x,y) in dist:
            possible_cheats[(cx,cy,x,y)] = max(dist[(x,y)] -i, possible_cheats.get((cx,cy,x,y), 0))
            continue

        check_collisions = cheated_at != i-1

        for dx, dy in ADJ_ORT:
            xx, yy = x + dx, y + dy
            if not in_bounds(xx, yy):
                continue

            if (xx, yy) not in dist2[cx,cy]:
                if is_cheating:
                    nq.append((xx, yy, cheated_at, (cx, cy)))
                else:
                    if g[yy][xx] != "#":
                        nq.append((xx, yy, cheated_at, (cx, cy)))

            if not has_cheated:
                nq.append((xx, yy, i, (xx, yy)))
    q = nq
    i += 1

saves = defaultdict(int)
for cheat in possible_cheats.values():
    saves[cheat] += 1
print(saves)

print(len([v for v in possible_cheats.values() if v>=100]))

# print(dist)




if __name__ == "__main__":
    pass
