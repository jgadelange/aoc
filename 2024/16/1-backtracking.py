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
inv= {
    N: S,
    E: W,
    S: N,
    W: E,
}

s = start, E
scores = {
    s: 0
}

queue = PriorityQueue()
queue.put((0, s))

while not queue.empty():
    score, ((x, y), d) = queue.get()
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

    for dd in rot[d]:
        n = (x, y), dd
        if score + 1000 < scores.get(n, sys.maxsize):
            scores[n] = score + 1000
            queue.put((score + 1000, n))

stack = [((x,y), d)]
visited = {(x,y)}
while stack:
    (x, y), d = stack.pop()
    score = scores[(x, y), d]

    for dd in [N, E, S, W]:
        dx, dy = inv[dd]
        ds = 1 if dd == d else 1001
        xx, yy = x+dx, y+dy
        score2 = scores.get(((xx, yy), dd), sys.maxsize)
        if score2 + ds == score:
            stack.append(((xx, yy), dd))
            visited.add((xx, yy))

print(len(visited))





if __name__ == "__main__":
    pass
