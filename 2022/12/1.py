from queue import PriorityQueue

f = open('./input', 'r')

grid = [[x for x in line.strip()] for line in f.readlines()]
w = len(grid[0])
h = len(grid)

start = None
end = None

for y in range(h):
    for x in range(w):
        if grid[y][x] == "S":
            start = (y, x)
            grid[y][x] = "a"
        if grid[y][x] == "E":
            end = (y, x)
            grid[y][x] = "z"

distance = {
    start: 0
}
queue = PriorityQueue()

queue.put((0, start))

adj = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1),
]

while queue.qsize():
    d, (y, x) = queue.get()
    curr = ord(grid[y][x])

    for dy, dx in adj:
        yy = y + dy
        xx = x + dx
        if (yy, xx) in distance:
            continue
        try:
            a = ord(grid[yy][xx])
        except IndexError:
            continue

        if a - curr <= 1:
            distance[(yy, xx)] = d+1
            queue.put((d+1, (yy, xx)))

print(distance[end])


if __name__ == "__main__":
    pass
