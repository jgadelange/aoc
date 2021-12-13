import sys
from collections import defaultdict

f = open('./input', 'r')
inp = [int(x) for x in f.readline().split(",") if x]
# print(inp)
days = 256

new_fish_templ = {
    i:0
    for i in range(9)
}

fish = new_fish_templ.copy()
for fi in inp:
    fish[fi] += 1

for d in range(days):
    new_fish = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
    }
    for fi, n in fish.items():
        if fi == 0:
            new_fish[8] += n
            new_fish[6] += n
        else:
            new_fish[fi-1] += n
    fish = new_fish

    # print(d+1, fish, sum(fish.values()))
    # print(sum(fish.values()))

# print(sum(fish.values()))
sys.stdout.write(str(sum(fish.values())))
sys.stdout.write("\n")

f.close()
