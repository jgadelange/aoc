from collections import defaultdict
from itertools import cycle

f = open('./input', 'r')
NROCKS = 1_000_000_000_000
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
    return zip(cycle(rox), range(n+1))


def print_state(rock=None):
    global positions, maxy
    if rock is None:
        rock = []

    for y in range(maxy+7, -1, -1):
        print("|"+"".join("#" if (x,y) in positions else "@" if (x,y) in rock else "." for x in range(maxx+1))+"|")


maxx = 6
maxy = -1

positions = defaultdict(set)
rocks = rock_generator(NROCKS)

check_every = len(jets) if len(jets)%len(rox) == 0 else len(jets)*len(rox)

def move_rock(r, to):
    dx, dy = to

    return [
        (x+dx, y+dy)
        for x, y in r
    ]


last_lines = {}
maxys = {}
nlines= 20
rock = None
for d, j in zip(cycle(jets), range(NROCKS)):
    if rock is None:
        try:
            rock, i = next(rocks)
            maxys[i] = maxy
            rock = move_rock(rock, (2, maxy+4))

            if maxy > nlines:
                lines = (i%len(rox), j%len(jets), tuple(x in positions[y] for y in range(maxy-nlines, maxy+1) for x in range(maxx+1)))
                if lines in last_lines:
                    print("I've seen this before!")
                    print(i,maxy, last_lines[lines])

                    previ= last_lines[lines]
                    prevy = maxys[previ]
                    di = i - previ
                    dy = maxy - prevy
                    for n in (2022, NROCKS):
                        trest = n-i
                        steps = trest // di
                        rest = trest % di

                        rest_y = maxys[previ + rest] - prevy

                        print(maxy+steps*dy+rest_y+1)

                    exit()

                last_lines[lines] = i

            # print_state(rock)
            # input()
        except StopIteration:
            break

    r2 = move_rock(rock, d)

    if any(x in positions[y] for x, y in r2) or any(x<0 or x>maxx for x, _ in r2):
        pass
    else:
        rock = r2

    r2 = move_rock(rock, (0, -1))

    if any(x in positions[y] for x, y in r2) or any(y < 0 for _, y in r2):
        maxy = max(maxy, rock[-1][1])
        for x, y in rock:
            positions[y].add(x)
        # print_state()
        # input()
        rock = None
    else:
        rock = r2


print(maxy+1)



if __name__ == "__main__":
    pass
