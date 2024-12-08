import itertools
from collections import defaultdict

f = open('./input', 'r')

grid = [line.strip() for line in f.readlines() if line.strip()]
h, w = len(grid), len(grid[0])
mi, ma = complex(0,0), complex(w, h)
antennas = defaultdict(list)
al = set()
l = {}

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == ".":
            continue
        antennas[char].append(complex(x, y))
        al.add(complex(x,y))
        l[complex(x,y)] = char

anti = set()
for name, aas in antennas.items():
    for a, b in itertools.combinations(aas, 2):
        d = a - b

        aa = a - (b-a)
        while 0 <= aa.real < w and 0<=aa.imag<h:
            anti.add(aa)
            aa = aa - (b-a)

        bb = b - (a-b)
        while 0 <= bb.real < w and 0<=bb.imag<h:
            anti.add(bb)
            bb = bb - (a-b)

#
# print(
#     "\n".join(
#         "".join(l[complex(x,y)] if complex(x,y) in al else "#" if complex(x,y) in anti else "." for x in range(w+1))
#         for y in range(h+1)
#     )
# )

print(len(anti | al))





if __name__ == "__main__":
    pass
