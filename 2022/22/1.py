from itertools import takewhile

f = open('./input', 'r')

map_data, ins = f.read().split("\n\n")

walls = set()
grid = {}


def instructions():
    it = iter(ins.strip())

    while True:
        d = ""
        try:
            while (n := next(it)).isdigit():
                d+=n
        except StopIteration:
            yield int(d)
            break
        yield int(d)
        yield n



for y, line in enumerate(map_data.split("\n"), start=1):
    grid[y] = {}
    for x, c in enumerate(line, start=1):
        if c == " ":
            continue
        if c == "#":
            walls.add((y, x))
        grid[y][x] = c

start = (1, min(x for x, v in grid[1].items() if v == "."), 0)


move = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


def perform(c, m):
    y, x = c
    dy, dx = m

    yy, xx = y+dy, x+dx

    if yy in grid and xx in grid[yy]:
        return yy, xx

    if dy != 0:
        f = max if dy == -1 else min
        return (f(yyy for yyy, line in grid.items() if x in line), x)

    if dx != 0:
        f = max if dx == -1 else min
        return (y, f(xxx for xxx in grid[yy].keys()))
    print("Ahoh")
    exit()


current = start
# print(current)
for i in instructions():
    y, x, d = current
    if isinstance(i, int):
        m = move[d]
        newy, newx = y, x
        for i in range(i):
            newy, newx = perform((newy, newx), m)
            # print(newy, newx)
            if (newy, newx) in walls:
                break
            if newy not in grid or newx not in grid[newy]:
                print(newy, newx)
                exit()
                print("WTF!")
            current = (newy, newx, d)
        continue
    if i == "L":
        d = (d - 1) % 4
    elif i == "R":
        d = (d + 1) % 4
    else:
        print("???", i)
        print(repr(i))
    current = (y, x, d)

print("Pt1")
print(current)
print(current[0] * 1000 + 4 * current[1] + current[2])


if __name__ == "__main__":
    pass
