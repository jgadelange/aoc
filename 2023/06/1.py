import math

f = open('./input', 'r')

ts, ds = f.readlines()[:2]

races = list(zip(
    map(int, ts.split()[1:]),
    map(int, ds.split()[1:])
))



print(math.prod(sum(
    (i * (t - i)) > d
    for i in range(t)
)
for t, d in races))


if __name__ == "__main__":
    pass
