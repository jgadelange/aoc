f = open('./input', 'r')

elves = {
    (x, y)
    for y, line in enumerate(f.readlines())
    for x, c in enumerate(line)
    if c == "#"
}

dirs = (
    ((0, -1), [(-1, -1), (0, -1), (1, -1)]),
    ((0, 1), [(-1, 1), (0, 1), (1, 1)]),
    ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
    ((1, 0), [(1, -1), (1, 0), (1, 1)]),
)


def add(a, b):
    x, y = a
    xx, yy = b
    return x+xx, y+yy


def adj():
    return set(
        x
        for _, cs in dirs
        for x in cs
    )

i = 0
while True:
    new_elves = {}
    for e in elves:
        if not any(add(e, c) in elves for c in adj()):
            new_elves[e] = [(e, False)]
            continue

        added = False
        for j in range(4):
            d, check = dirs[(j+i) % 4]
            if any(add(e, c) in elves for c in check):
                continue

            ne = add(e, d)
            if ne not in new_elves:
                new_elves[ne] = [(e, True)]
            else:
                new_elves[ne].append((e, True))
            added = True
            break
        if not added:
            new_elves[e] = [e]

    elves = set()
    all_stand_still = True
    for e, es in new_elves.items():
        if len(es) > 1:
            elves.update(x for x, _ in es)
        else:
            _, moved = es.pop()
            elves.add(e)
            all_stand_still = all_stand_still and not moved

    i += 1
    if i == 10:
        w = abs(max(x for x, y in elves) - min(x for x, y in elves)) + 1
        h = abs(max(y for x, y in elves) - min(y for x, y in elves)) + 1
        print("Pt1")
        print(
            (w * h) - len(elves)
        )

    if all_stand_still:
        print("pt2")
        print(i)
        break


if __name__ == "__main__":
    pass
