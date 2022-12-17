from itertools import cycle

f = open('./input', 'r')

rox = [
    # ####
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    # .#.
    # ###
    # .#.
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    # ..#
    # ..#
    # ###
    [(0, 0),  (1, 0), (2, 0), (2, 1), (2, 2)],
    # #
    # #
    # #
    # #
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    # ##
    # ##
    [(0, 0),  (1, 0), (0, 1),  (1, 1)],
]

jets = [(-1, 0) if x == "<" else (1, 0) for x in f.read().strip()]


def rock_generator(n):
    for r, _ in zip(cycle(rox), range(n)):
        yield r


def print_state(rock=None):
    global positions, maxy
    if rock is None:
        rock = []

    for y in range(maxy+7, -1, -1):
        print("|"+"".join("#" if (x,y) in positions else "@" if (x,y) in rock else "." for x in range(maxx+1))+"|")


maxx = 6
maxy = -1

positions = set()
rocks = rock_generator(2022)


def move_rock(r, to):
    dx, dy = to

    return [
        (x+dx, y+dy)
        for x, y in r
    ]


rock = None
for d in cycle(jets):
    if rock is None:
        try:
            rock = next(rocks)
            rock = move_rock(rock, (2, maxy+4))
            # print_state(rock)
            # input()
        except StopIteration:
            break

    r2 = move_rock(rock, d)

    if any(r in positions for r in r2) or any(x<0 or x>maxx for x, _ in r2):
        pass
    else:
        rock = r2

    r2 = move_rock(rock, (0, -1))

    if any(r in positions for r in r2) or any(y < 0 for _, y in r2):
        maxy = max(maxy, rock[-1][1])
        positions.update(rock)
        # print_state()
        # input()
        rock = None
    else:
        rock = r2


print(maxy+1)



if __name__ == "__main__":
    pass
