f = open('./example', 'r')

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

boxes = {(x*2,y) for y in range(h) for x in range(w) if g[y][x] == "O"}
walls = [[(x*2,y), (x*2+1, y)] for y in range(h) for x in range(w) if g[y][x] == "#"]
ws = set()
for (x,y), (xx, yy) in walls:
    ws|= {(x,y), (xx, yy)}

robot = next((x*2,y) for y in range(h) for x in range(w) if g[y][x] == "@")

print(
    "\n".join(
        "".join("#" if (x,y) in ws else "[" if (x,y) in boxes else "]" if (x-1, y) in boxes else "@" if (x,y) == robot else "." for x in range(w*2))
        for y in range(h)
    )
)

print(robot)

moves = "".join(ds.split("\n"))
print(len(moves))
x, y = robot

for j, move in enumerate(moves):
    if j > 370:
        print(
            "\n".join(
                "".join("#" if (a,b) in ws else "[" if (a,b) in boxes else "]" if (a-1, b) in boxes else move if (a,b) == (x,y) else "." for a in range(w*2))
                for b in range(h)
            )
        )
        # print(j, move)
        input("")
    dx, dy = dmap[move]
    xx, yy = x + dx, y + dy
    if (xx, yy) in ws:
        print("WALL")
        continue
    if (dx, dy) == RIGHT:
        if (xx, yy) not in boxes:
            x, y = xx, yy
            continue

        to_move_boxes = {(xx, yy)}
        xxx, yyy = xx + dx * 2, yy + dy * 2
        i = 1
        while (xxx, yyy) in boxes:
            to_move_boxes.add((xxx,yyy))
            xxx, yyy = xxx + dx * 2, yyy + dy * 2
        if (xxx, yyy) in ws:
            continue
        boxes -= to_move_boxes
        boxes |= {
            (xxx+dx, yyy)
            for xxx, yyy in to_move_boxes
        }
        x,y = xx, yy
        continue

    if (dx, dy) == LEFT:
        print("LEFT")
        if (xx-1, yy) not in boxes:
            x, y = xx, yy
            continue

        xxx, yyy = xx-1 + dx * 2, yy + dy * 2
        i = 1
        to_move_boxes = {(xx - 1,yy)}
        while (xxx, yyy) in boxes:
            to_move_boxes.add((xxx,yyy))
            i += 1
            xxx, yyy = xxx + dx * 2, yyy + dy * 2
        if (xxx+1, yyy) in ws or xxx<0:
            continue
        xxx, yyy = xx-1, yy
        boxes -= to_move_boxes
        boxes |= {
            (xxx+dx, yyy)
            for xxx, yyy in to_move_boxes
        }
        x,y = xx, yy
        continue
    if (dx, dy) in [DOWN, UP]:

        to_move_boxes = {
            (xx+i, yy)
            for i in [-1, 0]
            if (xx+i, yy) in boxes
        }
        print(to_move_boxes)
        if not to_move_boxes:
            x, y = xx, yy
            continue
        bs = to_move_boxes

        can_move = True
        while can_move:
            next_bs = set()
            for xxx, yyy in bs:
                yyy = yyy + dy
                if (xxx, yyy) in ws or (xxx+1, yyy) in ws:
                    can_move = False
                    break

                if (xxx-1, yyy) in boxes:
                    next_bs.add((xxx-1,yyy))
                if (xxx, yyy) in boxes:
                    next_bs.add((xxx,yyy))
                if (xxx+1, yyy) in boxes:
                    next_bs.add((xxx+1, yyy))
            if len(next_bs) == 0:
                break
            to_move_boxes |= next_bs
            bs = next_bs

        if not can_move:
            continue

        boxes -= to_move_boxes
        boxes |= {
            (xxx, yyy+dy)
            for (xxx, yyy) in to_move_boxes
        }

    x,y = xx, yy

print(
    "\n".join(
        "".join("#" if (a,b) in ws else "[" if (a,b) in boxes else "]" if (a-1, b) in boxes else "@" if (a,b) == (x,y) else "." for a in range(w*2))
        for b in range(h)
    )
)

print(sum(y*100 + x for x,y in boxes))


if __name__ == "__main__":
    pass
