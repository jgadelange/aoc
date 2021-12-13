import sys

f = open('./input', 'r')

def print_grid():
    for y in range(h):
        for x in range(w):
            sys.stdout.write("#" if (y,x) in dots else ".")
        sys.stdout.write("\n")


read_dots = True
dots = set()
folds = []
w = 0
h = 0
for line in f.readlines():
    if line == "\n":
        read_dots = False
        continue

    if read_dots:
        x, y = [int(i) for i in line.strip().split(",")]
        w = max(w, x)
        h = max(h, y)
        dots.add((y, x))
    else:
        fold, loc = line.rsplit(" ", 1)
        axis, i = loc.split("=")
        folds.append((axis, int(i)))

first = True
for axis, fold in folds:
    if axis == "x":
        new_dots = set()
        for y, x in dots:
            if x < fold:
                new_dots.add((y, x))
                continue
            new_dots.add((y, fold - (x - fold)))
        dots = new_dots
        w = fold
    else:
        new_dots = set()
        for y, x in dots:
            if y < fold:
                new_dots.add((y, x))
                continue
            new_dots.add((fold - (y - fold), x))
        dots = new_dots
        h = fold
    if first:
        print(len(dots))
        first = False

print_grid()

f.close()
