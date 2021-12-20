from itertools import combinations

from utils.point import Point
from utils.generated_code import get_all_rotations_methods

f = open('./input', 'r')

rotation_methods = get_all_rotations_methods()


def rotated_points_gen(bs):
    for f in rotation_methods:
        yield {
            f(b)
            for b in bs
        }


scanners = [
    {
        Point(*map(int, beacon.split(",")))
        for beacon in block.strip().split("\n")[1:]
    }
    for block in f.read().split("\n\n")
]


scanner_locations = [Point(0, 0, 0)]
beacons = scanners.pop(0)


def find_suitable_rotation(known_beacons, try_scanner):
    for known_beacon in known_beacons:
        relative_set = {known_beacon - other_known for other_known in known_beacons}
        for rotated_beacons in rotated_points_gen(try_scanner):
            for try_beacon in rotated_beacons:
                try_relative_set = {try_beacon - other_try for other_try in rotated_beacons}
                overlap = try_relative_set.intersection(relative_set)
                if len(overlap) >= 12:
                    return rotated_beacons, known_beacon - try_beacon
    return None, None


while scanners:
    current = scanners.pop(0)
    rotated_beacons, offset = find_suitable_rotation(beacons, current)
    if offset is not None:
        beacons.update({(b + offset) for b in rotated_beacons})
        scanner_locations.append(offset)
    else:
        scanners.append(current)
        print(":(", len(scanners))


print(len(beacons))
print(max(int(a - b) for a, b in combinations(scanner_locations, 2)))


f.close()
