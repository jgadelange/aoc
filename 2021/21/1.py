import time

f = open('./input', 'r')
starttime = time.time()

pos = [
    int(line.strip().split(":")[1]) - 1
    for line in f.readlines()
]


def det_die_gen():
    i = 0
    while True:
        yield i, 6 + i*9
        i += 1


scores = [0, 0]


rolls = det_die_gen()
print(1, pos, scores)
while True:
    i, roll = next(rolls)
    player = i % 2
    pos[player] = (pos[player] + roll) % 10
    scores[player] += pos[player] + 1

    if scores[player] >= 1000:
        break

print((i+1)*3*scores[1-player])

print(f"Took {time.time()-starttime}s")
f.close()
