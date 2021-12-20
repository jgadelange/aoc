from itertools import combinations

from utils.generated_code import get_all_rotations_methods_tuple

f = open('./input', 'r')

rotation_methods = get_all_rotations_methods_tuple()


def rotated_points_gen(bs):
    for f in rotation_methods:
        yield {
            f(*b)
            for b in bs
        }


scanners = [
    {
        tuple(map(int, beacon.split(",")))
        for beacon in block.strip().split("\n")[1:]
    }
    for block in f.read().split("\n\n")
]


scanner_locations = [(0, 0, 0)]
beacons = scanners.pop(0)


def find_suitable_rotation(known_beacons, try_scanner):
    for (x, y, z) in known_beacons:
        relative_set = {(x - xx, y - yy, z - zz) for (xx,yy,zz) in known_beacons}
        for rotated_beacons in rotated_points_gen(try_scanner):
            for (rx, ry, rz) in rotated_beacons:
                try_relative_set = {(rx - rxx, ry-ryy, rz-rzz) for (rxx,ryy,rzz) in rotated_beacons}
                overlap = try_relative_set.intersection(relative_set)
                if len(overlap) >= 12:
                    return rotated_beacons, (x-rx, y-ry, z-rz)
    return None, (0,0,0)


while scanners:
    current = scanners.pop(0)
    rotated_beacons, (x, y, z) = find_suitable_rotation(beacons, current)
    if rotated_beacons is not None:
        beacons.update({(x+xx, y+yy, z+zz) for xx, yy, zz in rotated_beacons})
        scanner_locations.append((x,y,z))
    else:
        scanners.append(current)
        print(":(", len(scanners))


print(len(beacons))
print(max(abs(x-xx)+abs(y-yy)+abs(z-zz) for (x,y,z), (xx,yy,zz) in combinations(scanner_locations, 2)))


f.close()
