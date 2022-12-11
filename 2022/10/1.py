f = open('./input', 'r')

counter = 0
X = 1
check_at = iter(range(20, 221, 40))
next_stop = next(check_at)
total = 0
grid = {}


def check_stop():
    global next_stop, counter, check_at, X, total
    try:
        if counter == next_stop:
            total += counter * X
            next_stop = next(check_at)
    except StopIteration:
        pass


def increase_counter():
    global counter, grid, X
    if X-1 <= counter % 40 <= X+1:
        grid[counter] = True
    counter += 1


increase_counter()


try:
    for line in f.readlines():
        check_stop()
        ins = line.strip().split()
        if ins[0] == "noop":
            increase_counter()
            continue
        if ins[0] == "addx":
            increase_counter()
            check_stop()

            X += int(ins[1])
            increase_counter()

except StopIteration:
    pass

print(total)
out = ""
for i in range(240):
    if i % 40 == 0:
        out += "\n"
    out += "#" if grid.get(i, False) else " "

print(out)

if __name__ == "__main__":
    pass
