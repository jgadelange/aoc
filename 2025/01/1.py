# Advent of Code 2025 - Day 01 – https://adventofcode.com/2025/day/01
f = open('./example', 'r')

c = 50
n = 0
nn = 0
for line in f.readlines():
    if not line.strip():
        continue
    r = line[0] == "R"
    v = int(line[1:])

    if r:
        nv = c + v
        c = nv % 100
        nn += nv // 100
    else:
        nv = c - v
        if c == 0:
            nn -= 1
        nn += abs(nv // 100)
        c = nv % 100
        if c == 0:
            nn += 1

    n += c == 0


print(c, n, n + nn, nn)

if __name__ == '__main__':
    pass

