# THIS DOESN'T WORK!

import functools
import operator
from functools import reduce

f = open('./input', 'r')

inp = []
for line in f.readlines():
    if not line.strip():
        continue
    a, b = line.split(": ")
    inp.append((int(a), list(map(int, b.split()))))


def f(tots, rest, total):
    if len(rest) == 0:
        return tots
    com = set()
    if len(rest) > 1:
        c = rest[0] * 10 + rest[1]
        nts = set()
        a = f({rest[0]}, rest[1:], total) | f({c}, rest[2:], total)
        for tot in tots:
            nts |= {tot + c, tot * c}

        com = f(nts, rest[2:], total)
        for tot in tots:
            com |= reduce(operator.or_, ({tot + aa, tot * aa, int(str(tot)+str(aa))} for aa in a))


    nts = set()
    for tot in tots:
        nts |= {tot * rest[0], tot + rest[0], tot * 10 + rest[0]}
    com |= f(nts, rest[1:], total)

    return set(filter(lambda x: x <= total, com))


# @functools.cache
def g(rest, total):
    if len(rest) == 0:
        return set()
    if len(rest) == 1:
        return {rest[0]}
    # if len(rest) == 2:
    #     a, b = rest
    #     return {a+b, a*b, concat(a,b)}

    a = rest[-1]
    rr = g(rest[:-1], total)

    n = reduce(operator.or_, ({a + b, a * b, concat(b, a)} for b in rr))

    return filter(lambda x: x <= total, n)

def concat(a, b):
    return a*10 + b


ans = 0
for total, nums in inp:
    # print("start", total, nums)
    x = g(tuple(nums), total)

    #
    # for i in range(len(nums)-1):
    #     a, b = nums[:i+1], nums[i+1:]
    #     # print(a,b)
    #     aa = g(tuple(a))
    #     bb = g(tuple(b))
    #     # print(aa,bb)
    #     x|= reduce(operator.or_, ({a + b, a * b, concat(a, b)} for a in aa for b in bb))

    print(total, x)
    if total in x:
        print(ans, total)
        ans += total

print(ans)

if __name__ == "__main__":
    pass
