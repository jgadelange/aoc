import re
from collections import Counter

file, w, h = "./input", 101, 103
# file, w, h = "./example", 11, 7
f = open(file, 'r')


m = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

robots = []
for line in f:
    if not line.strip():
        continue
    robots.append(tuple(map(int,m.match(line).groups())))

locs = [
    ((x+dx*100) % w, (y+dy*100) % h)
    for x,y,dx,dy in robots
]

a,b,c,d = 0,0,0,0
for x,y in locs:
    if x < w//2:
        if y < h//2:
            a+=1
        elif y > h//2:
            b+=1
    elif x > w//2:
        if y < h//2:
            c+=1
        elif y > h//2:
            d+=1

print(a,b,c,d)

print(a*b*c*d)


if __name__ == "__main__":
    pass
