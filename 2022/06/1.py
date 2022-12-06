from itertools import islice, tee

f = open('./input', 'r')

data = f.read().strip()


def grouping(iterable, n):
    iterables = tee(iterable, n)
    for i, it in enumerate(iterables):
        for _ in range(i):
            next(it, None)
    return zip(*iterables)


for i, x in enumerate(grouping(data, 4)):
    if len(set(x)) == 4:
        print(i+4)
        break


for i, x in enumerate(grouping(data, 14)):
    if len(set(x)) == 14:
        print(i+14)
        break


if __name__ == "__main__":
    pass
