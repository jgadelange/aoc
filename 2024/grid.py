N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)


def add_points(*points):
    return tuple(map(sum, zip(*points)))


NE = add_points(N, E)
SE = add_points(S, E)
SW = add_points(S, W)
NW = add_points(N, W)

ADJ_ORT = [N, E, S, W]
ADJ_DIAG = [NE, SE, SW, NW]
ADJ = [N, NE, E, SE, S, SW, W, NW]

UP = (0, -1)
LEFT = (-1, 0)
DOWN = (0, 1)
RIGHT = (1, 0)

ADJ_ORT_3D = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def in_bounds(w, h, x, y):
    return 0 <= x < w and 0 <= y < h


def out_of_bounds(w, h, x, y):
    return x < 0 or x >= w or y < 0 or y >= h
    return not in_bounds(w, h, x, y)
