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


yy = 2000000
# yy = 10

skipx = set(x for x,y in sensors.keys() if y == yy)
skipx.update(set(x for x,y in beacons if y == yy))

xs = set()
for (sx, sy), d in sensors.items():
    dy = abs(sy - yy)
    if dy > d:
        continue
    dx = d - dy
    xs.update(range(sx - dx, sx + dx +1))

print(len(xs-skipx))

if __name__ == "__main__":
    pass
