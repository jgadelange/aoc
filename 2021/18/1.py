from functools import reduce
from itertools import permutations
from math import floor, ceil

f = open('./input', 'r')


class IntNode:
    def __init__(self, val, parent=None):
        self.parent = parent
        self.value = val

    def split(self):
        if self.value >= 10:
            div = self.value // 2
            return True, Pair(div, self.value - div, parent=self.parent)
        return False, self

    def explode(self, _d, _wl, _wr):
        return False

    def magnitude(self):
        return self.value

    def move_value_right(self, value, _=False):
        assert _ is False
        self.value += value
        return True

    def move_value_left(self, value, _=False):
        assert _ is False
        self.value += value
        return True

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Pair:
    def __init__(self, left, right, loc=None, parent=None):
        self.loc = loc
        self.parent = parent
        if isinstance(left, list):
            self.left = Pair(left[0], left[1], "left", self)
        elif isinstance(left, int):
            self.left = IntNode(left, self)
        else:
            left.parent = self
            left.loc = "left"
            self.left = left

        if isinstance(right, list):
            self.right = Pair(right[0], right[1], "right", self)
        elif isinstance(right, int):
            self.right = IntNode(right, self)
        else:
            right.parent = self
            right.loc = "right"
            self.right = right

    def __str__(self):
        return f"[{self.left},{self.right}]"

    def __repr__(self):
        return f"<Pair [{repr(self.left)}, {repr(self.right)}] d={self.get_depth()} loc={self.loc}>"

    def __add__(self, other):
        return Pair(self, other)

    def get_depth(self):
        if self.parent == None:
            return 1
        return self.parent.get_depth() + 1

    def split(self):
        split, self.left = self.left.split()
        self.left.loc = "left"
        if not split:
            split, self.right = self.right.split()
            self.right.loc = "right"
        return split, self

    def explode(self, d=1, went_left=False, went_right=False):
        # print(d, went_left, went_right, str(self))
        if d == 5:
            assert isinstance(self.left, IntNode)
            assert isinstance(self.right, IntNode)
            # print("BOOM!", went_left, went_right)
            return True

        explode = self.left.explode(d+1, True, went_right)

        if explode and d == 4:
            # print("left_explode", self)
            left_value = self.left.left.value
            right_value = self.left.right.value
            # print(self)

            self.left.move_value_right(right_value, True)
            if went_right:
                self.left.move_value_left(left_value, True)
            self.left = IntNode(0, self)

            return True

        if not explode:
            explode = self.right.explode(d+1, went_left, True)
            if explode and d == 4:
                # print("right_explode", self)
                left_value = self.right.left.value
                right_value = self.right.right.value
                # print(self)
                self.right.move_value_left(left_value, True)
                # print(self)
                if went_left:
                    self.right.move_value_right(right_value, True)
                # print(self)
                self.right = IntNode(0, self)

                return True

        return explode

    def move_value_right(self, value, direction_up=False):
        if direction_up and self.loc == "left":
            return self.parent.right.move_value_right(value)
        if direction_up and self.loc == "right":
            if self.parent is None:
                return False
            return self.parent.move_value_right(value, True)

        self.left.move_value_right(value)

    def move_value_left(self, value, direction_up=False):
        if direction_up and self.loc == "right":
            return self.parent.left.move_value_left(value)
        if direction_up and self.loc == "left":
            if self.parent is None:
                return False
            return self.parent.move_value_left(value, True)

        return self.right.move_value_left(value)

    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    def reduce(self):
        while True:
            # print(p)
            # print(p.magnitude())
            explode = self.explode()
            if explode:
                # print(p)
                # input()
                continue

            split, _ = self.split()
            if not split:
                break
        return self


def get_gen(inp):
    for c in inp:
        yield c


def parse(g):
    c = next(g)
    if c == "[":
        return parse_list(g)

    return parse_number(c)


def parse_number(c):
    return int(c)


def parse_list(g):
    left = parse(g)

    c = next(g)
    assert c == ","

    right = parse(g)

    c = next(g)
    assert c == "]"

    return [left, right]


x = "[[1,2],[[3,4],5]]"

lines = list(f.readlines())

def get_pairs():
    return [
        Pair(*parse(get_gen(line)))
        for line in lines
    ]
pairs = [
    Pair(*parse(get_gen(line)))
    for line in f.readlines()
]
#
# p = pairs.pop(0)
# # print(repr(p))
# while True:
#     while True:
#         # print(p)
#         # print(p.magnitude())
#         explode = p.explode()
#         if explode:
#             # print(p)
#             # input()
#             continue
#
#         split, p = p.split()
#         if not split:
#             break
#     if len(pairs) == 0:
#         break
#     add = pairs.pop(0)
#     p = p + add
#     # input()
# print(p)
# print(p.magnitude())
# print("----")

# print("\n".join(repr(p) for p in pairs))

final_pair = reduce(lambda acc, a: (acc + Pair(*parse(get_gen(a)))).reduce(), lines[1:], Pair(*parse(get_gen(lines[0]))))
print(final_pair.magnitude())

print(max(
    (Pair(*parse(get_gen(a))) + Pair(*parse(get_gen(b)))).reduce().magnitude()
    for a, b in permutations(lines, 2)
))

f.close()
