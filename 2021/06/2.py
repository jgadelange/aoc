import sys
from collections import defaultdict

f = open('./input', 'r')
inp = [int(x) for x in f.readline().split(",") if x]
# print(inp)
days = 256

fish = defaultdict(int)
for fi in inp:
    fish[fi] += 1

for d in range(days):
    new_fish = defaultdict(int)
    for fi, n in fish.items():
        if fi == 0:
            new_fish[8] += n
            new_fish[6] += n
        else:
            new_fish[fi-1] += n
    fish = new_fish
    print(d+1, fish, sum(fish.values()))
    # print(sum(fish.values()))

print(sum(fish.values()))

f.close()
