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
        all(v for _, v in b[i]) or all(b[j][i][1] for j in range(5))
        for i in range(5)
    )


found = False
for n in numbers:
    for i, b in enumerate(boards):
        for j, r in enumerate(b):
            for k, (c, _) in enumerate(r):
                if c == n:
                    boards[i][j][k][1] = True
        if check_board(b):
            found = True
            print_board(b)
            break
    if found:
            print(n)
            break

unchecked = sum([c for r in b for c,v in r if not v])
print(unchecked)
print(n * unchecked)
f.close()
