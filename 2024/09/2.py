f = open('./input', 'r')

inp = list(map(int, f.read().strip()))

m = []
for i, n in enumerate(inp):
    m.append((n, i//2 if i % 2 == 0 else None))

# print(m)
# exit()
i = 0
c = 0
j = len(m)-1

res = []
ans = 0

while j > 0:
    l, n = m[j]
    if n is None:
        j -= 1
        continue

    i = 0
    while i < j:
        if m[i][1] is not None:
            i += 1
            continue
        ll = m[i][0]

        if ll >= l:
            new = [(l, n)]
            if l < ll:
                new += [(ll - l, None)]
            m[j] = (l, None)
            m = m[:i] + new + m[i+1:]

            break
        i += 1
    # print("".join((str(n) if n is not None else ".")*l for l,n in m))
    j-=1


c = 0
# print(res)

for l, n in m:
    n = 0 if n is None else n
    first = c
    last = c + l - 1
    ans += ((l * (first + last))/2) * n
    c = last + 1
print(ans)



if __name__ == "__main__":
    pass
