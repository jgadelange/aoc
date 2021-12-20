f = open('./input', 'r')

adj = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get(grid, loc, oob):
    y, x = loc

    if y < 0 or x < 0:
        return oob

    try:
        return grid[y][x]
    except:
        return oob


def convert_to_int(grid, loc):
    y, x = loc
    return int("".join(str(get(grid, (y + dy, x + dx), grid[0][0])) for dy, dx in adj), base=2)


def enhance(g, conv):
    h = len(g)
    w = len(g[0])

    return [
        [
            conv[convert_to_int(g, (y-1,x-1))]
            for x in range(w+2)
        ]
        for y in range(h+2)
    ]


def print_grid(g):
    h = len(g)
    w = len(g[0])
    print(
        "\n".join(
            "".join(
                "#" if grid[y][x] else "."
                for x in range(w)
            )
            for y in range(h)
        )
    )


conversion = [1 if c == "#" else 0 for c in f.readline() if c != "\n"]

extra = 1

assert f.readline() == "\n"

grid = [
    [0 for _ in range(extra)]+[
        1 if c == "#" else 0 for c in line if c != "\n"
    ]+[0 for _ in range(extra)]
    for line in f.readlines()
]

zeros = [0 for _ in range(len(grid[0]))]
grid = [zeros for _ in range(extra)] + grid + [zeros for _ in range(extra)]


for i in range(50):
    grid = enhance(grid, conversion)

    if i == 1:
        # print_grid(grid)
        print(sum(c for line in grid[extra:-extra] for c in line[extra:-extra]))
        # exit()

# print_grid(grid)
print(sum(c for line in grid[extra:-extra] for c in line[extra:-extra]))


f.close()
