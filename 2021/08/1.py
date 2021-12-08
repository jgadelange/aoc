f = open('./input', 'r')

c = 0
for line in f.readlines():
    _, out = line.split("|")
    for x in out.split(" "):
        c += 1 if len(x.strip()) in [2, 3, 4, 7] else 0

print(c)

f.close()
