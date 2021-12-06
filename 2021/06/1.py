import sys
from collections import defaultdict

f = open('./example', 'r')
inp = [int(x) for x in f.readline().split(",") if x]
# print(inp)
days = 80
fish = inp.copy()

for d in range(days):
    new_fish = 0
    for i, fi in enumerate(fish):
        if fi == 0:
            fish[i] = 6
            new_fish += 1
        else:
            fish[i] -= 1
    fish.extend(8 for _ in range(new_fish))
    print(d+1, len(fish))

print(len(fish))

f.close()
