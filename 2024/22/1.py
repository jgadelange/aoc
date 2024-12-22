f = open('./input', 'r')


def mix(a, b):
    return a ^ b


def prune(a):
    return a % 16777216


def evolve(a):
    b = a * 64
    a = prune(mix(a, b))
    b = a // 32
    a = prune(mix(a, b))
    b = a * 2048
    a = prune(mix(a, b))
    return a

ns = list(map(int, [l.strip() for l in f.readlines() if l.strip()]))

for _ in range(2000):
    ns = [evolve(n) for n in ns]

print(sum(ns))

if __name__ == "__main__":
    pass
