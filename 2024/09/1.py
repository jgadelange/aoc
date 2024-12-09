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
while i < j:
    l, n = m[j]
    # print(i,j)
    if n is None or l == 0:
        j -= 1
        continue

    while m[i][1] is not None:
        res.append(m[i])
        i += 1

    ll = m[i][0]

    d = abs(ll - l)
    if l > ll:
        res.append((ll, n))
        m[j] = (l - ll, n)
        i += 1
    else:
        res.append((l, n))
        m[j] = (0, n)
        j -= 1
        m[i] = (ll-l, None)
        if ll-l == 0:
            i += 1

res.extend((l, n) for l, n in m[i:] if l>0 and n is not None)

c = 0
# print(res)
# print("".join(str(n)*l for l,n in res))
for l, n in res:
    first = c
    last = c + l - 1
    ans += ((l * (first + last))/2) * n
    c = last + 1
print(ans)



if __name__ == "__main__":
    pass
