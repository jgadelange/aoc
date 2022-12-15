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

print("initialized")
ry = {}
rx = {}


def add(ranges, new_range):
    ranges.append(new_range)
    ranges = sorted(ranges)
    new = ranges[:1]
    for f, t in ranges[1:]:
        ff, tt = new.pop(-1)
        if ff <= f <= tt:
            new.append((ff, max(t,tt)))
        elif f <= ff <= t:
            new.append((f, max(tt,t)))
        elif f == tt + 1:
            new.append((min(f,ff), max(tt, t)))
        elif ff == t + 1:
            new.append((min(f, ff), max(tt, t)))
        else:
            new.append((ff,tt))
            new.append((f,t))
    return new

for (sx, sy), d in sensors.items():
    for dd in range(0, d+1):
        yy = sy+dd
        xx = sx+dd
        r = d - dd

        if 0 <= yy <= maxy:
            ry[yy] = add(ry.get(yy, []), (max(0, sx-r), min(sx+r, maxx)))
        if 0 <= xx <= maxx:
            rx[xx] = add(rx.get(xx, []), (max(0, sy-r), min(sy+r, maxx)))
        yy = sy-dd
        xx = sx-dd
        r = d - dd

        if 0 <= yy <= maxy:
            ry[yy] = add(ry.get(yy, []), (max(0, sx-r), min(sx+r, maxx)))
        if 0 <= xx <= maxx:
            rx[xx] = add(rx.get(xx, []), (max(0, sy-r), min(sy+r, maxx)))


    print("Processed sensor")

print("done processing, searching answer")
# print(x* 4000000 + y)

print("\n".join(str(x) for x, rs in rx.items() if len(rs) != 1))
print()
print("\n".join(str(y) for y, rs in ry.items() if len(rs) != 1))
if __name__ == "__main__":
    pass
