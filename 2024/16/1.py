import sys
from queue import PriorityQueue

f = open('./input', 'r')

g = [line.strip() for line in f.readlines() if line.strip()]
h,w = len(g), len(g[0])

start = next((x,y) for y in range(h) for x in range(w) if g[y][x] == "S")
end = next((x,y) for y in range(h) for x in range(w) if g[y][x] == "E")

N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)

rot = {
    N: [W, E],
    E: [N, S],
    S: [W, E],
    W: [N, S],
}

s = start, E
scores = {
    s: 0
}

queue = PriorityQueue()
queue.put((0, s))

print(s + s)
paths = {
    s: set((tuple(s),))
}

while not queue.empty():
    score, ((x, y), d) = queue.get()
    path = paths.get(((x, y), d))
    # print(path)
    if (x, y) == end:
        print(scores[(x, y), d])
        break

    dx, dy = d
    xx,yy = x+dx, y+dy
    if g[yy][xx] != "#":
        if score + 1 < scores.get(((xx, yy), d), sys.maxsize):
            scores[(xx, yy), d] = score + 1
            queue.put((score + 1, ((xx,yy), d)))
            paths[(xx, yy), d] = set(p + ((xx,yy),d) for p in path)
        if score + 1 == scores.get(((xx, yy), d), sys.maxsize):
            paths[(xx, yy), d] |= set(p + ((xx,yy),d) for p in path)

    for dd in rot[d]:
        dx, dy = dd
        xx,yy = x+dx, y+dy
        if g[yy][xx] != "#":
            if score + 1001 < scores.get(((xx, yy), dd), sys.maxsize):
                scores[(xx, yy), dd] = score + 1001
                queue.put((score + 1001, ((xx,yy), dd)))

                paths[(xx, yy), dd] = set(p + ((xx,yy),dd) for p in path)
            if score + 1001 == scores.get(((xx, yy), dd), sys.maxsize):
                paths[(xx, yy), dd]|= set(p + ((xx,yy),dd) for p in path)


visited = {
    (x,y)
    for p in paths[(x, y), d]
    for i, (x,y) in enumerate(p)
    if i%2 ==0
}
print(len(visited))

if __name__ == "__main__":
    pass
