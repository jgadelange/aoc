f = open('./input', 'r')

UP = (0, -1)
LEFT = (-1, 0)
DOWN = (0, 1)
RIGHT = (1, 0)
dmap = {
    "^": UP,
    "<": LEFT,
    "v": DOWN,
    ">": RIGHT,
}

m, ds = f.read().split('\n\n')

g = [
    line.strip() for line in m.split("\n")
    if line.strip()
]
h, w = len(g), len(g[0])

boxes = {(x,y) for y in range(h) for x in range(w) if g[y][x] == "O"}
walls = {(x,y) for y in range(h) for x in range(w) if g[y][x] == "#"}
robot = next((x,y) for y in range(h) for x in range(w) if g[y][x] == "@")
print(robot)

moves = "".join(ds.split("\n"))
x, y = robot
for move in moves:
    print(move)
    dx, dy = dmap[move]
    xx, yy = x + dx, y + dy
    if (xx, yy) in walls:
        print("WALL")
        continue
    if (xx, yy) in boxes:
        print("BOX")
        i = 1
        xxx, yyy = xx+dx, yy+dy
        while (xxx, yyy) in boxes:
            xxx, yyy = xxx+dx, yyy+dy
        if (xxx, yyy) in walls:
            continue
        boxes.remove((xx,yy))
        boxes.add((xxx, yyy))
    x,y = xx, yy

    # print(
    #     "\n".join(
    #         "".join("#" if (a,b) in walls else "O" if (a,b) in boxes else "@" if (a,b) == (x,y) else "." for a in range(w))
    #         for b in range(h)
    #     )
    # )


print(sum(y*100 + x for x,y in boxes))

#
# print(
#     "\n".join(
#         "".join("#" if (x,y) in walls else "O" if (x,y) in boxes else "." for x in range(w))
#         for y in range(h)
#     )
# )



if __name__ == "__main__":
    pass
