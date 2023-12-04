f = open('./input', 'r')

cards = [
    len({int(x) for x in line.split(": ")[1].split(" | ")[0].split()}.intersection(
     {int(x) for x in line.split("|")[1].split()}))
    for line in f.readlines()
    if line.strip()
]

n = len(cards)

ncards = [1]*n
for i in range(n):
    nc = ncards[i]
    nw = cards[i]
    if nw:
        for j in range(0, nw):
            try:
                ncards[i+j+1] += nc
            except:
                pass
print(ncards)

print(sum(
    ncards
))


if __name__ == "__main__":
    pass
