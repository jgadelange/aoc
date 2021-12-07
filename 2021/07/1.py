f = open('./input', 'r')
inp = [int(x) for x in f.readline().split(",") if x]

# sort = sorted(inp)


def calc_fuel(lst, loc):
    return sum(abs(x-loc) for x in lst)

# low = sort[0]
# low_value = calc_fuel(sort, low)
# high = sort[len(sort)-1]
# high_value = calc_fuel(sort, high)
#
# guess_index = len(sort) // 2
# n = sort[guess_index]
#
# while low <= high:
#     guess = low + high // 2
#     guess_value = calc_fuel(sort, guess)
#
#     if guess_value <
#
#
# print(sort)
# print(calc_fuel(sort, n))


print(calc_fuel(inp, min(range(max(inp)), key=lambda x: calc_fuel(inp, x))))

f.close()
