from collections import defaultdict

f = open('./input', 'r')

stones = list(map(int, f.read().strip().split()))

st = {
    stone: 1
    for stone in stones
}

for _ in range(75):
    ne = defaultdict(lambda: 0)
    for stone, n in st.items():
        if stone == 0:
            ne[1] += n
            continue
        s = str(stone)
        l = len(s)
        if l % 2 == 0:
            ne[int(s[:l//2])] += n
            ne[int(s[l//2:])] += n
        else:
            ne[stone*2024] += n
    st = ne
    if _ == 24:
        print(sum(st.values()))


print(sum(st.values()))

if __name__ == "__main__":
    pass
