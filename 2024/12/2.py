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
ans2 = 0
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

        sides = 0
        vs = set()
        for x,y, d in p:
            stack = [(x, y, d)]
            if (x,y,d) not in vs:
                sides += 1
            else:
                continue
            while stack:
                xx, yy, dd = stack.pop()
                vs.add((xx, yy, dd))
                for dx, dy in ADJ_ORT:
                    xxx, yyy = xx + dx, yy + dy
                    if (xxx,yyy, dd) in vs:
                        continue
                    if (xxx, yyy, dd) in p:
                        stack.append((xxx,yyy, dd))


        # print(c, len(v), sides)
        ans += len(p) * len(v)
        ans2 += sides * len(v)

print(ans)
print(ans2)



if __name__ == "__main__":
    pass
