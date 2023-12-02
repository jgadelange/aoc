from collections import defaultdict
from functools import reduce

f = open('./input', 'r')

games = {}

allowed_maxs = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
s = 0
p = 0

def product(*vs):
    return reduce(lambda acc, v: acc*v, vs, 1)


for line in f.readlines():
    line = line.strip()
    if not line:
        continue

    game, draws = line.split(': ')
    game_id = int(game.split(" ")[-1])
    draws = [dict(reversed(color.split(" ")) for color in draw.split(", ")) for draw in draws.split("; ")]

    maxs = defaultdict(int)
    for draw in draws:
        for c, v in draw.items():
            maxs[c] = max(int(v), maxs[c])

    if all(allowed_maxs[c] >= maxs[c] for c in allowed_maxs):
        s += game_id

    min_draw = {
        c: max(int(d[c]) for d in draws if c in d)
        for c in allowed_maxs
    }

    p += product(*min_draw.values())

print(s)
print(p)

if __name__ == "__main__":
    pass
