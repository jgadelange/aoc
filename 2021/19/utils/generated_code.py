from utils.point import Point


def get_all_rotations_for(p):
    return [
        Point(-p.x, p.y, -p.z),
        Point(p.x, p.z, -p.y),
        Point(p.z, -p.y, p.x),
        Point(p.y, -p.x, p.z),
        Point(p.z, -p.x, -p.y),
        Point(p.y, p.x, -p.z),
        Point(-p.z, p.x, -p.y),
        Point(p.x, -p.y, -p.z),
        Point(-p.z, -p.y, -p.x),
        Point(-p.y, -p.x, -p.z),
        Point(-p.y, p.z, -p.x),
        Point(-p.z, -p.x, p.y),
        Point(-p.z, p.y, p.x),
        Point(p.y, -p.z, -p.x),
        Point(-p.y, -p.z, p.x),
        Point(-p.x, -p.y, p.z),
        Point(-p.x, p.z, p.y),
        Point(-p.x, -p.z, -p.y),
        Point(-p.y, p.x, p.z),
        Point(p.y, p.z, p.x),
        Point(p.z, p.x, p.y),
        Point(p.z, p.y, -p.x),
        Point(p.x, -p.z, p.y),
        Point(p.x, p.y, p.z),
    ]


def get_all_rotations_methods():
    return [
        lambda p: Point(-p.x, p.y, -p.z),
        lambda p: Point(p.x, p.z, -p.y),
        lambda p: Point(p.z, -p.y, p.x),
        lambda p: Point(p.y, -p.x, p.z),
        lambda p: Point(p.z, -p.x, -p.y),
        lambda p: Point(p.y, p.x, -p.z),
        lambda p: Point(-p.z, p.x, -p.y),
        lambda p: Point(p.x, -p.y, -p.z),
        lambda p: Point(-p.z, -p.y, -p.x),
        lambda p: Point(-p.y, -p.x, -p.z),
        lambda p: Point(-p.y, p.z, -p.x),
        lambda p: Point(-p.z, -p.x, p.y),
        lambda p: Point(-p.z, p.y, p.x),
        lambda p: Point(p.y, -p.z, -p.x),
        lambda p: Point(-p.y, -p.z, p.x),
        lambda p: Point(-p.x, -p.y, p.z),
        lambda p: Point(-p.x, p.z, p.y),
        lambda p: Point(-p.x, -p.z, -p.y),
        lambda p: Point(-p.y, p.x, p.z),
        lambda p: Point(p.y, p.z, p.x),
        lambda p: Point(p.z, p.x, p.y),
        lambda p: Point(p.z, p.y, -p.x),
        lambda p: Point(p.x, -p.z, p.y),
        lambda p: Point(p.x, p.y, p.z),
    ]