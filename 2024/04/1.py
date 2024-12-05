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

n = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'X':
            for dx, dy in adj:
                i = 1
                yy, xx = y + (dy*i), x + (dx*i)
                if yy < 0 or xx < 0 or yy >= h or xx >= w:
                    continue
                while grid[yy][xx] == s[i]:
                    if s[i] == "S":
                        n += 1
                        break
                    i += 1
                    yy, xx = y + (dy*i), x + (dx*i)
                    if yy < 0 or xx < 0 or yy >= h or xx >= w:
                        break



print(n)

if __name__ == "__main__":
    pass
