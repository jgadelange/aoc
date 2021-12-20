from utils.point import Point
from utils.generated_code import get_all_rotations_methods

f = open('./example', 'r')

rotation_methods = get_all_rotations_methods()
print(rotation_methods)

scanners = [
    [
        Point(*map(int, beacon.split(",")))
        for beacon in block.strip().split("\n")[1:]
    ]
    for block in f.read().split("\n\n")
]

print(scanners)

beacons = scanners.pop(0)


f.close()
