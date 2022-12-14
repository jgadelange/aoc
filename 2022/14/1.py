from itertools import pairwise

f = open('./input', 'r')

SAND = "o"
ROCK = "#"
positions = {}
lines = [
    [
        tuple([int(x) for x in c.split(",")])
        for c in line.split(" -> ")
    ]
    for line in f.read().split("\n")
    if line
]


for line in lines:
    for (x, y), (xx, yy) in pairwise(line):
        if x == xx:
            miny = min(y, yy)
            maxy = max(y, yy)
            for yyy in range(miny, maxy+1):
                positions[(x, yyy)] = ROCK
        elif y == yy:
            minx = min(x, xx)
            maxx = max(x, xx)
            for xxx in range(minx, maxx+1):
                positions[(xxx, y)] = ROCK
        else:
            print(":( diagonals")

minx = min(x for (x, y) in positions.keys())
maxx = max(x for (x, y) in positions.keys())
miny = 0
maxy = max(y for (x, y) in positions.keys())


start = (500, 0)
oob = False
while True:
    if start in positions or oob:
        break
    x, y = start
    while True:
        if maxx <= x or x <= minx or y >= maxy:
            oob = True
            break
        if (x, y+1) in positions:
            if (x-1, y+1) not in positions:
                x-=1
                y+=1
                continue
            if (x+1, y+1) not in positions:
                x+=1
                y+=1
                continue
            positions[(x,y)] = SAND
            break
        y += 1

print(len([x for x in positions.values() if x == SAND]))
if __name__ == "__main__":
    pass
