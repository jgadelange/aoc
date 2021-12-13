f = open('./input', 'r')


class Wall():
    def __int__(self):
        return self

    def __add__(self, other):
        return self

    def __gt__(self, other):
        return False

    def __str__(self):
        return "#"


energy = [
    [Wall()] + [int(c) for c in r if c != "\n"] + [Wall()]
    for r in f.readlines()
]
energy.insert(0, [Wall() for _ in range(len(energy[1]))])
energy += [[Wall() for _ in range(len(energy[1]))]]

adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), ]


def incr(y, x):
    energy[y][x] += 1
    return energy[y][x] > 9


def print_grid():
    print("\n".join(
        "".join(str(energy[y][x]) if not isinstance(energy[y][x], Wall) and energy[y][x] < 10 else "#" for x in
                range(len(energy[y])))
        for y in range(len(energy))
    ))


flashes = 0
i = 0

while True:
    i += 1
    stack = list()
    flashed = set()

    for y in range(1, 11):
        for x in range(1, 11):
            if incr(y, x):
                stack.append((y, x))
                flashed.add((y, x))

    while len(stack) > 0:
        y, x = stack.pop()

        for dy, dx in adj:
            if incr(y + dy, x + dx):
                if (y + dy, x + dx) not in flashed:
                    stack.append((y + dy, x + dx))
                    flashed.add((y + dy, x + dx))

    for y, x in flashed:
        energy[y][x] = 0
    flashes += len(flashed)
    if i == 100:
        print("Part 1", flashes)
    if len(flashed) == 100:
        print("Part 2", i)
        break

f.close()
