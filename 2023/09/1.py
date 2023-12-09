import re

f = open('./input', 'r')

histories = list(list(map(int, line.split())) for line in f.readlines() if line.strip())

s = 0
ss = 0
for h in histories:
    dss = [h]
    ds = h
    while True:
        ds = [b-a for a, b in zip(ds[:-1], ds[1:])]
        if not any(ds):
            break
        dss.append(ds)
    s += sum(ds[-1] for ds in dss)

    prev = 0
    for x in dss[::-1]:
        prev = x[0]-prev
    ss += prev
print(s)
print(ss)

if __name__ == "__main__":
    pass
