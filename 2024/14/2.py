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

s = 0
while True:
    s+=1
    robots = [
        ((x+dx) % w, (y+dy) % h, dx, dy)
        for x,y,dx,dy in robots
    ]
    locs = Counter((x,y) for x,y,_,_ in robots)

    if len(locs) == len(robots):
        print("\n".join(
            "".join(["#" if (x,y) in locs else "." for x in range(w)])
            for y in range(h)
        ))
        print(s)
        break
    if s == 100:
        a,b,c,d = 0,0,0,0
        for x,y in locs:
            if x < w//2:
                if y < h//2:
                    a+=locs[(x,y)]
                elif y > h//2:
                    b+=locs[(x,y)]
            elif x > w//2:
                if y < h//2:
                    c+=locs[(x,y)]
                elif y > h//2:
                    d+=locs[(x,y)]


        print(a*b*c*d)


if __name__ == "__main__":
    pass
