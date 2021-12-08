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
    0: set("#"),
    1: set("#"),
    2: set("#"),
    3: set("#"),
    4: set("#"),
    5: set("#"),
    6: set("#"),
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
    print(get_segment_display_str(segments_on_off, segment_mapping))


def get_segment_display_str(segments_on_off, segment_mapping=None):
    if segment_mapping is None:
        segment_mapping = default_segment_mapping
    return segment_format.format(
        **dict(zip("abcdefg", [segment_mapping[i].copy().pop() if x else "." for i, x in enumerate(segments_on_off)])))


def join_by_line(strs):
    per_line = [string.split("\n") for string in strs]
    max_lines = max(len(lines) for lines in per_line)
    max_line_length = max(len(line) for lines in per_line for line in lines)

    return "\n".join(
        " ".join(
            per_line[j][i].ljust(max_line_length, " ")
            for j in range(len(strs))
        )
        for i in range(max_lines)
    )


def print_segment_displays(n, segment_mapping=None):
    print(join_by_line([
        get_segment_display_str(segments[int(i)], segment_mapping)
        for i in str(n)
    ]).replace("x", "#"))


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
    print_segment_displays(out_str, segment_map)

# print(total)
print_segment_displays(total)
f.close()
