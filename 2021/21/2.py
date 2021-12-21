import time
from collections import Counter
from queue import Queue

f = open('./input', 'r')
starttime = time.time()

start = [
    int(line.strip().split(":")[1]) - 1
    for line in f.readlines()
]

rolls = [sum([i+1,j+1,k+1]) for i in range(3) for j in range(3) for k in range(3)]
counter = Counter(rolls)

def generator_det():
    i = 0
    while True:
        yield [(6 + i*9, 1)]
        i += 1


def generator():
    while True:
        yield counter.items()


roller = generator_det()


def execute(roller, starting_pos, goal_score):
    queue = Queue()
    queue.put_nowait((0, tuple(starting_pos), (0, 0)))
    universes = {
        (0, tuple(starting_pos), (0, 0)): 1
    }

    wins = [0, 0]

    while not queue.empty():
        i, pos, scores = queue.get_nowait()
        player = i % 2
        num = universes.pop((player, pos, scores))
        for roll, n in next(roller):
            _pos = (pos[0] + (1-player) * roll) % 10, (pos[1] + (player) * roll) % 10
            _scores = scores[0] + ((1-player) * (_pos[0]+1)), scores[1] + ((player) * (_pos[1]+1))
            state = (1-player, _pos, _scores)
            if _scores[player] >= goal_score:
                wins[player] += num * n
            else:
                if state not in universes:
                    queue.put_nowait((i+1, _pos, _scores))
                    universes[state] = 0
                universes[state] += num * n
    return i, _scores, wins


i, score, _ = execute(generator_det(), start, 1000)
print("part1: ", 3 * (i + 1) * score[1 - (i % 2)])

_, _, wins = execute(generator(), start, 21)
print("part2: ", max(wins))

print(f"Took {time.time()-starttime}s")
f.close()
