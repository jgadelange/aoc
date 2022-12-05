f = open('./input', 'r')

data = [x.strip().split(",") for x in f.readlines()]

count = 0
count2 = 0
for l, r in data:
    a, b = l.split("-")
    c, d = r.split("-")

    one = set(range(int(a), int(b)+1))
    # print(a, b, one)
    two = set(range(int(c), int(d)+1))
    # print(c, d, two)

    if len(one.difference(two)) == 0 or len(two.difference(one)) == 0:
        # print(l, r)
        count+=1

    if len(one.intersection(two)) != 0:
        count2+=1

print(count, count2)


if __name__ == "__main__":
    pass
