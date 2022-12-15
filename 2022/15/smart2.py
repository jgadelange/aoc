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

points = set((x,y) for x in range(maxx) for y in range(maxy))

print("initialized")

for (sx, sy), d in sensors.items():
    for dy in range(-d, d+1):
        yy = sy + dy
        dx = d - dy
        points -= set((xx, yy) for xx in range(max(0, sx - dx), min(sx + dx +1, maxx+1)))
    print("Processed sensor")

x, y = points.pop()
print(x* 4000000 + y)


if __name__ == "__main__":
    pass
