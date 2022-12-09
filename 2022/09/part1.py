from copy import copy

f = open('./input', 'r')

h = [0, 0]
t = [0, 0]

visited_by_tail = {
    tuple(t): True
}

def distance(a, b):
    x1, y1 = a
    x2, y2 = b

    return abs(y1 - y2) > 1 or abs(x1 - x2) > 1


for line in f.readlines():
    d, n = line.strip().split()

    for _ in range(int(n)):
        old_h = copy(h)
        if d == "U":
            h[1] -= 1
        if d == "D":
            h[1] += 1
        if d == "L":
            h[0] -= 1
        if d == "R":
            h[0] += 1


        if distance(h, t):
            t = old_h
            visited_by_tail[tuple(t)] = True

print(len(visited_by_tail))

if __name__ == "__main__":
    pass
