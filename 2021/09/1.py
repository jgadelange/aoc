f = open('./input', 'r')


class Inf:
    pass


heights = [
    [Inf] + [int(c) for c in r if c != "\n"] + [Inf]
    for r in f.readlines()
]
heights.insert(0, [Inf for _ in range(len(heights[1]))])
heights += [[Inf for _ in range(len(heights[1]))]]


def lt(a, b):
    if b is Inf:
        return True
    return a < b


cells = [
    (heights[i][j])
    for i in range(1, len(heights)-1)
    for j in range(1, len(heights[0])-1)
    if (
        lt(heights[i][j], heights[i-1][j]) and
        lt(heights[i][j], heights[i+1][j]) and
        lt(heights[i][j], heights[i][j-1]) and
        lt(heights[i][j], heights[i][j+1])
    )
]


# print(cells)
print(sum(cells) + len(cells))

f.close()
