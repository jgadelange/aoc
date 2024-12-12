f = open('./input', 'r')

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)
ADJ_ORT = [N, E, S, W]


g = [
    line.strip()
    for line in f.readlines()
    if line.strip()
]
h, w = len(g), len(g[0])
# print(g)

def in_bounds(x, y):
    return 0 <= x < w and 0 <= y < h

visited = set()
plots = []
ans = 0
for s in range(h):
    for r in range(w):

        if (r, s) in visited:
            continue
        stack = [(r, s)]
        v = set()
        c = g[s][r]
        p = set()

        while stack:
            x, y = stack.pop()
            v.add((x, y))
            visited.add((x, y))
            for dx, dy in ADJ_ORT:
                xx, yy = x + dx, y + dy
                if (xx,yy) in v:
                    continue
                if not in_bounds(xx, yy) or g[yy][xx] != c:
                    p.add((xx, yy, (dx, dy)))
                    continue
                stack.append((xx, yy))
        # print(c, len(v), len(p))
        ans += len(p) * len(v)

print(ans)



if __name__ == "__main__":
    pass
