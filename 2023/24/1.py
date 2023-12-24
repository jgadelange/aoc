# https://www.mathsisfun.com/algebra/line-equation-2points.html
# https://cp-algorithms.com/geometry/lines-intersection.html
f = open('./input', 'r')

stones = []
for line in f.readlines():
    line = line.strip()
    if not line:
        continue
    coords, velocity = line.split("@")
    stones.append((
        tuple(map(int, coords.split(","))),
        tuple(map(int, velocity.split(","))),
    ))

print(stones)


lines = [] # aX + bY + c = 0
for (x,y,z), (dx,dy,dz) in stones:
    m = dy/dx
# Y - y = m(X - x)
# Y - y = mX - mx
# Y - y - mX + mx = 0
    a = -m
    b = 1
    c = (m*x) - y
    lines.append((a,b,c))

def det(a,b,c,d):
    return a*d - b*c

lb, ub = 200000000000000, 400000000000000
# lb, ub = 7, 27
intersecting = set()
ans = 0
for i in range(len(stones)-1):
    for j in range(i+1, len(stones)):
        if i == j or i in intersecting or j in intersecting:
            continue
        a1, b1, c1 = lines[i]
        a2, b2, c2 = lines[j]
        zn = det(a1,b1,a2,b2)
        (x1, y1, z1), (dx1, dy1, dz1) = stones[i]
        (x2, y2, z2), (dx2, dy2, dz2) = stones[j]

        if zn == 0:
            # print("no intersect")
            continue

        x = -det(c1,b1,c2,b2) / zn
        y = -det(a1,c1,a2,c2) / zn

        if (
                dx1 < 0 and x > x1 or
                dy1 < 0 and y > y1 or
                dx1 > 0 and x < x1 or
                dx1 > 0 and x < x1 or
                dx2 < 0 and x > x2 or
                dy2 < 0 and y > y2 or
                dx2 > 0 and x < x2 or
                dx2 > 0 and x < x2
        ):
        # if x > maxx or y > maxy:
        #     print("PAST")
            continue
        if lb <= x <= ub and lb <= y <= ub:
            # print(stones[i])
            # print(stones[j])
            # print(x,y)

            # intersecting.add(i)
            # intersecting.add(j)
            ans += 1
        # print(x,y)


print(ans)

if __name__ == "__main__":
    pass
