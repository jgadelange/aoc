f = open('./example', 'r')


hm = [
    [
        int(h)
        for h in line.strip()
    ]
    for line in f.readlines()
]

w = len(hm[0])
h = len(hm)

visible = [
    [
        {"t": False, "b": False, "l":False, "r": False}
        for _ in range(w)
    ]
    for _ in range(h)
]

num_visible = 0
best_scenic_score = 0
for y in range(h):
    for x in range(w):
        if any([
            all(hm[y][a] < hm[y][x] for a in range(x)),
            all(hm[a][x] < hm[y][x] for a in range(y)),
            all(hm[y][w-a-1] < hm[y][x] for a in range(w-x-1)),
            all(hm[h-a-1][x] < hm[y][x] for a in range(h-y-1)),
        ]):
            num_visible += 1

        scenic_score = 1
        d = 0
        for a in reversed(range(x)):
            d += 1
            if hm[y][a] >= hm[y][x]:
                break

        scenic_score *= d
        d = 0
        for a in reversed(range(y)):
            d += 1
            if hm[a][x] >= hm[y][x]:
                break

        scenic_score *= d
        d = 0
        for a in reversed(range(w-x-1)):
            d += 1
            if hm[y][w-a-1] >= hm[y][x]:
                break

        scenic_score *= d
        d = 0
        for a in reversed(range(h-y-1)):
            d += 1
            if hm[h-a-1][x] >= hm[y][x]:
                break

        scenic_score *= d

        best_scenic_score = max(scenic_score, best_scenic_score)


print(num_visible)
print(best_scenic_score)

if __name__ == "__main__":
    pass
