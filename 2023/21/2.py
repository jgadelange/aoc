# Took some inspiration from: https://github.com/jmerle/advent-of-code-2023/blob/13b424e9cebbfebf4f5c7629c36cab8dca50af37/src/day21/part2.py
f = open('./input', 'r')

grid = [line.strip() for line in f.readlines() if line.strip()]
h, w = len(grid), len(grid[0])
print(h,w)

start = None
nwalls = 0
for y in range(h):
    for x in range(w):
        if grid[y][x] == "S":
            start = (x,y)
        if grid[y][x] == "#":
            nwalls+=1

print(nwalls)
N = (0, -1)
W = (-1, 0)
S = (0, 1)
E = (1, 0)
adj = [N,W,E,S]

current = {start}
prev = 0

always= set()

ns = [1]
wdiff = 0
first_wdiff= 0
target = 26_501_365
for i in range(target):
    if first_wdiff and i == first_wdiff+w:
        break

    next = set()
    for x,y in current:
        for dx,dy in adj:
            xx, yy = x+dx, y+dy
            # if xx < 0 or xx >=w or yy <0 or yy>=h:
            #     continue
            try:
                if grid[yy%h][xx%w] != "#":
                    next.add((xx,yy))
            except:
                pass
    current = next
    ns.append(len(current))

    if i > 3*w:
        diff = ns[i] - ns[i-w]
        diff2 = ns[i-w] -ns[i-2*w]
        diff3 = ns[i-2*w] - ns[i-3*w]

        if diff - diff2 == diff2 - diff3:
            wdiff = diff-diff2
            if not first_wdiff:
                first_wdiff = i
            print(i, diff-diff2)

            if (target-i) % w == 0:
                break

print(wdiff)


offset = (target - first_wdiff) %w

i = first_wdiff+offset
print(first_wdiff, offset, i)
c = ns[i]
diff = ns[i] - ns[i-w]
while i != target:
    diff += wdiff
    i += w
    c += diff

print(c)

if __name__ == "__main__":
    pass
