from copy import copy

f = open('./input', 'r')

data = [(int(x), False) for x in f.readlines()]
n = len(data)

while True:
    try:
        i, d = next((i, d) for i, (d, moved) in enumerate(data) if moved is False)
    except StopIteration:
        break

    data.pop(i)
    new_i = (i+d) % (n-1)
    data.insert(new_i, (d, True))

i = data.index((0, True))
print(data)
print(
    data[(i+1000) % len(data)][0] +
    data[(i+2000) % len(data)][0] +
    data[(i+3000) % len(data)][0]
)


if __name__ == "__main__":
    pass
