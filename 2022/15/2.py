import re

f = open('./input', 'r')

r = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

beacons = set()
sensors = {}


def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


for line in f.readlines():
    m = r.match(line)
    if not m:
        continue
    sx, sy, bx, by=list(int(x) for x in m.groups())


    beacons.add((bx,by))
    sensors[(sx, sy)] = distance((sx, sy), (bx, by))

maxx = 4000000
maxy = 4000000
# maxx = 20
# maxy = 20

found = False
for yy in range(maxy+1):
    # xs = set()
    xs = set(range(maxx+1))
    xs -= set(x for x,y in sensors.keys() if y == yy)
    xs -= (set(x for x,y in beacons if y == yy))
    for (sx, sy), d in sensors.items():
        dy = abs(sy - yy)
        if dy > d:
            continue
        dx = d - dy
        xs -= set(range(max(0, sx - dx), min(sx + dx +1, maxx+1)))
        if len(xs) == 0:
            break
    print(yy, len(xs))
    if len(xs) == 1:
        x = xs.pop()
        print(x * 4000000 + yy)
        break



if __name__ == "__main__":
    pass
