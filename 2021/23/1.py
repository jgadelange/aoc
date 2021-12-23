import sys
import time
from copy import deepcopy
from queue import PriorityQueue

f = open('./input', 'r')
starttime = time.time()

"""
#############
#...........#
###C#B#D#D###
  #B#C#A#A#
  #########
"""
extra = ["  #D#C#B#A#  ", "  #D#B#A#C#  "]

bins = range(1,12)
lookup = "ABCD"
dests = [2+2*i for i in range(4)]

lines = list(f.readlines())

stacks = tuple(
    (tuple(
        lookup.index(line[loc])
        for line in lines[2:3] + extra + lines[3:4]
        if line[loc] in lookup
    ))
    for loc in bins
)
num = len(stacks[2])

max_size = [
    (1 if loc not in dests else num)
    for loc in range(len(bins))
]

queue = PriorityQueue()

queue.put_nowait((0, stacks))

print(dests)
print(max_size)
print(stacks)


def finished(s, num):
    return all(
        len(s[loc]) == num
        and all(
            s[loc][j] == i
            for j in range(num)
        )
        for i, loc in enumerate(dests)
    )

in_queue = {stacks:True}
new = None
# min_cost = sys.maxsize
min_cost = {stacks: 0}
fin = None


def move(state, orig, dest, letter):
    new_state = list(deepcopy(state))
    new_i = list(state[orig])
    del new_i[0]
    new_state[orig] = tuple(new_i)
    new_state[dest] = (letter,) + new_state[dest]
    new_state = tuple(new_state)

    n = get_steps(state, orig, dest)

    return new_state, (n * (10 ** letter))


def get_steps(state, i, j):
    num_steps = 0 if i not in dests else (max_size[i] - size + 1)
    num_steps += 0 if j not in dests else (max_size[j] - len(state[j]))
    num_steps += abs(i - j)
    return num_steps


def get_cost(prev_cost, n, letter):
    return prev_cost + (n * (10 ** letter))


while not queue.empty():
    cost, stack = queue.get()
    in_queue[new] = False

    if finished(stack, num):
        print("possible answer", cost)

    for i, bin in enumerate(stack):
        size = len(bin)
        if size == 0:
            continue
        item = stack[i][0]

        if dests[item] == i and all(item == x for x in bin):
            # print("Already in final bin", i, bin, item, stack)
            continue

        for j in range(len(stacks)):
            new = None
            if i == j:
                continue
            if i not in dests and j != dests[item]:
                continue

            if any(
                    len(stack[x])
                    for x in range(min(i, j)+1, max(i, j))
                    if x not in dests
            ):
                continue

            if j == dests[item]:
                if len(stack[j]) == 0 or all(x == item for x in stack[j]):
                    new, move_cost = move(stack, i, j, item)
                    new_cost = cost + move_cost

                    if not in_queue.setdefault(new, False):
                        in_queue[new] = True
                        queue.put(
                            (new_cost, new)
                        )
                continue
            if j in dests:
                new = "invalid dest"
                continue
            if len(stack[j]) < max_size[j]:
                new, move_cost = move(stack, i, j, item)
                new_cost = cost + move_cost
                old_cost = min_cost.get(new, sys.maxsize)

                if not in_queue.setdefault(new, False):
                    in_queue[new] = True
                    queue.put(
                        (new_cost, new)
                    )

print(f"Took {time.time()-starttime}s")
f.close()
