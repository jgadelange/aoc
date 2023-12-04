f = open('./input', 'r')

cards = [
    {int(x) for x in line.split(": ")[1].split(" | ")[0].split()}.intersection(
     {int(x) for x in line.split("|")[1].split()})
    for line in f.readlines()
    if line.strip()
]

print(sum(
    2**(len(x)-1)
    for x in cards
    if len(x)
))


if __name__ == "__main__":
    pass
