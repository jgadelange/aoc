import sys
from queue import PriorityQueue

f = open('./input', 'r')

grid = [
    [int(x) for x in line if x != "\n"]
    for line in f.readlines()
]

h = len(grid)
w = len(grid[0])

queue = PriorityQueue()
queue.put_nowait((0, (0, 0)))

risks = {}


def from_coordinate(xx, yy, risk):
    cxx = xx % w
    cyy = yy % h
    penalty = xx // w + yy // h

    nrisk = risk + ((grid[cyy][cxx] + penalty - 1) % 9) + 1
    if nrisk < risks.setdefault((yy,xx), sys.maxsize):
        risks[(yy, xx)] = nrisk
        queue.put_nowait((nrisk, (yy, xx)))


while not queue.empty():
    risk, (y, x) = queue.get_nowait()

    if x > 0:
        from_coordinate(x-1, y, risk)
    if x < (5*w)-1:
        from_coordinate(x+1, y, risk)
    if y > 0:
        from_coordinate(x, y-1, risk)
    if y < (5*h)-1:
        from_coordinate(x, y+1, risk)

print("part 1", risks[(h-1, w-1)])
print("part 2", risks[((5*h)-1,(5*w)-1)])

f.close()
