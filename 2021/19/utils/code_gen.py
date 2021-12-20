import operator
import os
from functools import reduce
from itertools import permutations
from math import pi, cos, sin
from pathlib import Path

from utils.point import Point


pi2 = pi/2
icos = lambda x: int(round(cos(x)))
isin = lambda x: int(round(sin(x)))


def rotateX(p, i):
    return Point(
        p.x,
        p.y * icos(i*pi2) - p.z * isin(i*pi2),
        p.y * isin(i*pi2) + p.z * icos(i*pi2)
    )


def rotateY(p, i):
    return Point(
        p.z * isin(i*pi2) + p.x * icos(i*pi2),
        p.y,
        p.z * icos(i*pi2) - p.x * isin(i*pi2)
    )


def rotateZ(p, i):
    return Point(
        p.x * icos(i*pi2) - p.y * isin(i*pi2),
        p.x * isin(i*pi2) + p.y * icos(i*pi2),
        p.z
    )


def rotateAll(p):
    rotateMethods = [
        rotateX,
        rotateY,
        rotateZ,
    ]
    rotations = list(
        m
        for m in permutations(rotateMethods, 3)
    )
    return reduce(
        operator.or_,
        [
            reduce(lambda ps, f: {
                f(px, i)
                for px in ps
                for i in range(4)
            }, rot, {p})
            for rot in rotations
        ]
    )


def print_imports(f):
    f.write("from utils.point import Point\n")


def print_spacing(f):
    f.write("\n\n")


def print_get_all_rotations_for(f):
    mapping = {
        2: "p.x",
        -2: "-p.x",
        4: "p.y",
        -4: "-p.y",
        6: "p.z",
        -6: "-p.z"
    }
    f.write("def get_all_rotations_for(p):\n")
    indent = "    "
    f.write("{0}return [\n".format(indent))
    for p in rotateAll(Point(2,4,6)):
        f.write("{0}{0}Point({x}, {y}, {z}),\n".format(
            indent,
            x=mapping[p.x],
            y=mapping[p.y],
            z=mapping[p.z],
        ))
    f.write("{0}]\n".format(indent))


def print_get_all_rotation_methods(f):
    mapping = {
        2: "p.x",
        -2: "-p.x",
        4: "p.y",
        -4: "-p.y",
        6: "p.z",
        -6: "-p.z"
    }
    f.write("def get_all_rotations_methods():\n")
    indent = "    "
    f.write("{0}return [\n".format(indent))
    for p in rotateAll(Point(2,4,6)):
        f.write("{0}{0}lambda p: Point({x}, {y}, {z}),\n".format(
            indent,
            x=mapping[p.x],
            y=mapping[p.y],
            z=mapping[p.z],
        ))
    f.write("{0}]\n".format(indent))


if __name__ == "__main__":
    # f = sys.stdout
    f = open(Path(os.path.dirname(__file__)) / "generated_code.py", "w")
    print_imports(f)
    print_spacing(f)
    print_get_all_rotations_for(f)
    print_spacing(f)
    print_get_all_rotation_methods(f)
    f.close()
