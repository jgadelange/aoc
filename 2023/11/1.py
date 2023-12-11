from itertools import combinations
from queue import PriorityQueue

f = open('./input', 'r')
N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)


data = [([c for c in line.strip()]) for line in f.readlines() if line.strip()]

ngrid = []
for y in range(len(data)):
    ngrid.append(data[y].copy())
    if all(c == "." for c in data[y]):
        ngrid.append(data[y].copy())

h = len(ngrid)
w = len(ngrid[0])
n = 0

grid = [line.copy() for line in ngrid]

for x in range(w):
    if all(ngrid[y][x] == "." for y in range(h)):
        for y in range(h):
            grid[y].insert(x+n, ".")
        n+=1


# exit()
h = len(grid)
w = len(grid[0])
# exit()

galaxies = [
    (x, y)
    for y, line in enumerate(grid)
    for x, c in enumerate(line)
    if c == "#"
]

print(galaxies)

# total_distance = 0
# paths = {}
# for cx, cy in galaxies:
#     dists = {
#         (tx, ty): tdists[(x,y)]
#         for (tx, ty), tdists in paths.items()
#         if (x,y) in tdists
#     }
#     q = PriorityQueue()
#     q.put((0, (cx,cy)))
#
#     while any(t not in dists for t in galaxies):
#         # print([t for t in galaxies if t not in dists])
#         # print(q.qsize())
#         d, (x,y) = q.get()
#         if (x, y) in dists:
#             continue
#         dists[(x,y)] = d
#
#         for dx, dy in [N, E, S, W]:
#             xx, yy = x + dx, y + dy
#             if xx < 0 or xx>=w or yy<0 or yy >= h:
#                 continue
#             if (xx, yy) in dists:
#                 continue
#             q.put((d+1, (xx, yy)))
#
#     print(cx,cy)
#     paths[(cx,cy)] = dists
#     # total_distance += sum(
#     #     dists[t]
#     #     for t in galaxies
#     # )
#
# print(paths[galaxies[0]][galaxies[6]])
# print(paths[galaxies[2]][galaxies[5]])
# print(paths[galaxies[7]][galaxies[8]])
#
# # print(total_distance)
#
# print(*("".join(line) for line in grid), sep="\n")
# print(sum(
#     paths[a][b]
#     for a, b in combinations(galaxies, 2)
# ))


print(
    sum(
        abs(xa - xb) + abs(ya - yb)
        for (xa, ya), (xb, yb) in combinations(galaxies, 2)
    )
)

if __name__ == "__main__":
    pass
