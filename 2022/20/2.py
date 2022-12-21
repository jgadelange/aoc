from copy import copy

f = open('./input', 'r')

data = list(enumerate(int(x) * 811589153 for x in f.readlines()))
# print(data)
n = len(data)

for x in range(10):
    for ii in range(n):
        i, (j, d) = next((i, (j, d)) for i, (j, d) in enumerate(data) if j == ii)
        data.pop(i)
        new_i = (i+d) % (n-1)
        data.insert(new_i, (j, d))

i = next(i for i, (j, d) in enumerate(data) if d == 0)
print(i)
print(data)
print(
    data[(i+1000) % n][1] +
    data[(i+2000) % n][1] +
    data[(i+3000) % n][1]
)


if __name__ == "__main__":
    pass
