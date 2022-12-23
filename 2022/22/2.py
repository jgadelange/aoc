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
    (R := 0): (0, 1),
    (D := 1): (1, 0),
    (L := 2): (0, -1),
    (U := 3): (-1, 0),
}


def perform(c, d):
    m = move[d]

    y, x = c
    dy, dx = m

    yy, xx = y+dy, x+dx

    if yy in grid and xx in grid[yy]:
        return yy, xx, d

    if d == U:
        if yy == 0:
            if 51 <= x <= 100:
                xx = 1
                yy = 150 + (x - 50)
                d = R
                return yy, xx, d
            if 101 <= x <= 150:
                yy = 200
                xx = x - 100
                d = U
                return yy, xx, d
        elif yy == 100:
            yy = 50+x
            xx = 51
            d = R
            return (yy, xx, d)
        else:
            print("PANINC")
            raise Exception()
    if d == D:
        if yy == 51:
            yy = 50 + x - 100
            xx = 100
            d = L
            return yy, xx, d
        if yy == 151:
            yy = 150 + x - 50
            xx = 50
            d = L
            return yy, xx, d
        if yy == 201:
            yy = 1
            xx = 100 + x
            d = D
            return yy, xx, d
        print("PANIC")
        raise Exception()

    if d == L:
        if 1 <= y <= 50:
            xx = 1
            yy = 150 - ((y-1) % 50) # Check 50
            d = R
            return yy, xx, d
        if 51 <= y <= 100:
            yy = 101
            xx = (y - 50)
            d = D
            return yy, xx, d
        if 101 <= y <= 150:
            xx = 51
            yy = 50 - ((y-1) % 50) # check 50
            d = R
            return yy, xx, d
        if 151 <= y <= 200:
            xx = 50 + (y - 150)
            yy = 1
            d = D
            return yy, xx, d

        print("PANIC")
        raise Exception()

    if d == R:
        if 1 <= y <= 50:
            xx = 100
            yy = 150 - ((y-1) % 50)
            d = L
            return yy, xx, d
        if 51 <= y <= 100:
            yy = 50
            xx = 100 + y - 50
            d = U
            return yy, xx, d
        if 101 <= y <= 150:
            xx = 150
            yy = 50 - ((y-1) % 50)
            d = L
            return yy, xx, d
        if 151 <= y <= 200:
            yy = 150
            xx = 50 + y - 150
            d = U
            return yy, xx, d
    print("PANIC", dx, x, y)
    raise Exception()

    return yy, xx, d



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
        newy, newx, newd = current
        for i in range(i):
            newy, newx, newd = perform((newy, newx), newd)
            # print(newy, newx)
            if (newy, newx) in walls:
                break
            if newy not in grid or newx not in grid[newy]:
                print(current)
                print(newy, newx)
                exit()
                print("WTF!")
            current = (newy, newx, newd)
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
