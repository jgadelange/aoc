f = open('./example2', 'r')


def print_rope(rope):
    out = ""
    min_x = min(x[0] for x in rope)
    max_x = max(x[0] for x in rope)
    min_y = min(x[1] for x in rope)
    max_y = max(x[1] for x in rope)

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            out += "x" if (x, y) in rope else "."
        out += "\n"
    print(out)
    print()


lines = list(f.readlines())

for l in [2, 10]:
    rope = [(0, 0)] * l
    visited_by_tail = {(0, 0): True}
    for line in lines:
        d, n = line.strip().split()
        for _ in range(int(n)):
            old_head = rope[0]
            if d == "U":
                new_head = (old_head[0], old_head[1] - 1)
            if d == "D":
                new_head = (old_head[0], old_head[1] + 1)
            if d == "L":
                new_head = (old_head[0] - 1, old_head[1])
            if d == "R":
                new_head = (old_head[0] + 1, old_head[1])

            rope[0] = new_head
            old_prev = old_head

            for i in range(len(rope)-1):
                (x, y), (xx, yy) = rope[i], rope[i+1]

                if abs(x - xx) < 2 and abs(y - yy) < 2:
                    continue

                diffx = x - xx
                newx = xx
                if diffx < 0:
                    newx -=1
                if diffx > 0:
                    newx +=1
                diffy = y - yy
                newy = yy
                if diffy < 0:
                    newy -=1
                if diffy > 0:
                    newy +=1
                rope[i+1] = (newx, newy)

            visited_by_tail[rope[-1]] = True
            if len(rope) == 10: print_rope(rope)
    print(len(visited_by_tail))

if __name__ == "__main__":
    pass
