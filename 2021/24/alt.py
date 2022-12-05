def execute_program(inp):
    w, x, y, z = 0, 0 ,0, 0
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 13
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += 0
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 4
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 15
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -13
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 10
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 16
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -9
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 13
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -14
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 6
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -3
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 7
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -2
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 13
    y *= x
    z += y
    w = inp.pop()
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -14
    x = x == w
    x = x == 0
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 3
    y *= x
    z += y
    return z

try:
    x = 99999359416613
    for i in range(1, 10**13):
        inp = list(int(a) for a in reversed(str(x-i)))
        if 0 in inp:
            continue
        if execute_program(inp) == 0:
            print(x-i)
            break
except KeyboardInterrupt:
    print(x-i)
