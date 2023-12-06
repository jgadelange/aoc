import math

f = open('./input', 'r')

ts, ds = f.readlines()[:2]

t,d = (
    int("".join(ts.split()[1:])),
    int("".join(ds.split()[1:]))
)



print(sum(
    (i * (t - i)) > d
    for i in range(t)
))



if __name__ == "__main__":
    pass
