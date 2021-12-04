import sys

f = open('./input', 'r')

numbers = [int(n) for n in f.readline().strip().split(",")]
print(numbers)

line_counter = 0
boards = []
i = -1
for line in f.readlines():
    if line == "\n":
        continue
    if line_counter % 5 == 0:
        i += 1
        boards.append([])
    boards[i].append([[int(number), False] for number in line.strip().split(" ") if number])
    line_counter += 1

def print_board(b):
    print("\n".join([
        "".join([
            str("*{}*".format(c) if v else c).center(6)
            for (c, v) in r
        ])
        for r in b
    ]))

def check_board(b):

    return any(
        all(v for _,v in b[i]) or all(b[j][i][1] for j in range(5))
        for i in range(5)
    )


found = False
for n in numbers:
    keep_boards = [True for _ in range(len(boards))]
    for i, b in enumerate(boards):
        for j, r in enumerate(b):
            for k, (c, _) in enumerate(r):
                if c == n:
                    boards[i][j][k][1] = True
        if check_board(b):
            keep_boards[i] = False
            print_board(b)
            if len(boards) == 1:
                found = True
    if found:
        break
    boards = [boards[i] for i, keep in enumerate(keep_boards) if keep]

print_board(boards[0])
unchecked = sum([c for r in boards[0] for c,v in r if not v])
print(n, unchecked)
print(n * unchecked)
f.close()
