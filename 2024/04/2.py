from itertools import pairwise

f = open('./input', 'r')

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

adj = [N, W, S, E]
adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), ]

grid = [line.strip() for line in f.readlines()]

h, w = len(grid), len(grid[0])

s = "XMAS"

a = [
    [(-1, -1), (1, 1)],
    ((1, -1), (-1, 1)),
]

n = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'A':
            if y-1 < 0 or y+1 >= h or x-1 < 0 or x+1 >= w:
                continue
            if all(
                grid[y+dy1][x+dx1] == "M" and grid[y+dy2][x+dx2] == "S"
                or
                grid[y+dy1][x+dx1] == "S" and grid[y+dy2][x+dx2] == "M"
                for (dx1, dy1), (dx2, dy2) in a
            ):
                n+=1



print(n)

if __name__ == "__main__":
    pass
