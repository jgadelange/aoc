from collections import defaultdict

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

total_per_sequence = defaultdict(int)
ans =0
for n in ns:
    diffs = []
    price_after_sequence = {}
    price = n % 10
    for i in range(2000):
        n = evolve(n)
        next_price = n % 10
        diffs.append(next_price-price)
        price = next_price
        if len(diffs) >= 4:
            sequence = tuple(diffs[-4:])
            price_after_sequence.setdefault(sequence, price)

    for key, value in price_after_sequence.items():
        total_per_sequence[key] += value
    ans += n

print(ans)
print(max(total_per_sequence.values()))

if __name__ == "__main__":
    pass
