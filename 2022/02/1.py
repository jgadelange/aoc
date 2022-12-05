f = open('./input', 'r')

data = [x.split() for x in f.readlines()]

# print(data)

score_choice = {"X": 1, "Y": 2, "Z": 3}
score_compare = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

print(sum(
    score_choice[b] + score_compare[a][b]
    for a, b in data
))

score_choice = {"X": 0, "Y": 3, "Z": 6}
score_compare = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1},
}

print(sum(
    score_choice[b] + score_compare[a][b]
    for a, b in data
))

if __name__ == "__main__":
    pass
