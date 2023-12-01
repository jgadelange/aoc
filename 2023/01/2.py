f = open('./input', 'r')

data = f.read()

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

def isdigit(s):
    try:
        int(s)
    except:
        return False
    else:
        return True

numbers = []
for line in data.split("\n"):
    if not line.strip():
        continue

    first = sorted([key for key in number_map if key in line], key=lambda x: line.index(x))[0]
    last = sorted([key for key in number_map if key in line], key=lambda x: line.rindex(x))[-1]

    numbers.append(int(number_map[first]+number_map[last]))

print(numbers)

print(sum(
    numbers
))

if __name__ == "__main__":
    pass
