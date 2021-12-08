from typing import List

f = open('./input', 'r')

segments = [
    (1, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 0, 1, 0),
    (1, 0, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 1),
    (0, 1, 1, 1, 0, 1, 0),
    (1, 1, 0, 1, 0, 1, 1),
    (1, 1, 0, 1, 1, 1, 1),
    (1, 0, 1, 0, 0, 1, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 1, 1),
]

default_segment_mapping = {
    0: set("x"),
    1: set("x"),
    2: set("x"),
    3: set("x"),
    4: set("x"),
    5: set("x"),
    6: set("x"),
}
segment_format = """
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg 
    """
segment_format = segment_format.replace("a", "{a}")
segment_format = segment_format.replace("b", "{b}")
segment_format = segment_format.replace("c", "{c}")
segment_format = segment_format.replace("d", "{d}")
segment_format = segment_format.replace("e", "{e}")
segment_format = segment_format.replace("f", "{f}")
segment_format = segment_format.replace("g", "{g}")


def print_segment_display(segments_on_off, segment_mapping=None):
    if segment_mapping is None:
        segment_mapping = default_segment_mapping
    print(segment_format.format(**dict(zip("abcdefg", [segment_mapping[i].copy().pop() if x else "." for i, x in enumerate(segments_on_off)]))))


def find_map(inp: List[set]):
    sort = sorted(inp, key=len)
    one = sort[0]
    seven = sort[1]
    four = sort[2]
    eight = sort[9]

    found = {
        0: (seven - one),  # a
        1: set("?"),  # b
        2: set("?"),  # c
        3: set("?"),  # d
        4: set("?"),  # e
        5: set("?"),  # f
        6: set("?"),  # g
    }

    sort.remove(one)
    sort.remove(seven)
    sort.remove(four)
    sort.remove(eight)

    # Find segment 6:
    for x in sort:
        rest = x - found[0] - four
        if len(rest) == 1:
            found[6] = rest
            break
    # Find segment 4
    for x in sort:
        rest = x - four - found[0] - found[6]
        if len(rest) == 1:
            found[4] = rest
            break
    # Find segment 1 and 3
    zero = None
    for x in sort:
        if len(x) != 6:
            continue
        rest = x - seven - found[4] - found[6]
        if len(rest) == 1:
            zero = x
            break
    sort.remove(zero)

    found[3] = four - zero
    found[1] = four - one - found[3]

    # Find number 5 (for segment 5):
    for x in sort:
        if len(x) != 5:
            continue
        rest = x - found[0] - found[1] - found[3] - found[5] - found[6]
        if len(rest) == 1:
            found[5] = rest
            break

    found[2] = one - found[5]

    return (
        [
            found[i].copy().pop()
            for i in range(7)
        ],
        found
    )


total = 0
for line in f.readlines():
    _numbers, _out = line.split("|")
    numbers = [set(x.strip()) for x in _numbers.split(" ") if len(x.strip())]
    out = [x.strip() for x in _out.split(" ") if len(x.strip())]

    letter_to_segment, segment_map = find_map(numbers)
    out_str = "".join(
        str(segments.index(tuple(
            int(a in x)
            for a in letter_to_segment
        )))
        for x in out
    )
    total += int(out_str)

print(total)
f.close()
