class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(
            self.x+other.x,
            self.y+other.y,
            self.z+other.z
        )

    def __sub__(self, other):
        return Point(
            self.x-other.x,
            self.y-other.y,
            self.z-other.z,
        )

    def __mul__(self, other):
        return Point(
            self.x*other.x,
            self.y*other.y,
            self.z*other.z,
            )

    def __str__(self):
        return str(self.as_tuple())

    def __repr__(self):
        return str(self.as_tuple())

    def __hash__(self):
        return hash(self.as_tuple())

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()

    def __int__(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def as_tuple(self):
        return self.x, self.y, self.z
