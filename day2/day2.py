total_score = 0
total_score_p2 = 0

rps_score = {
    ("A", "X"): 3 + 1,
    ("B", "X"): 0 + 1,
    ("C", "X"): 6 + 1,
    ("A", "Y"): 6 + 2,
    ("B", "Y"): 3 + 2,
    ("C", "Y"): 0 + 2,
    ("A", "Z"): 0 + 3,
    ("B", "Z"): 6 + 3,
    ("C", "Z"): 3 + 3,
}

rps_score_p2 = {
    ("A", "X"): 3 + 0,
    ("B", "X"): 1 + 0,
    ("C", "X"): 2 + 0,
    ("A", "Y"): 1 + 3,
    ("B", "Y"): 2 + 3,
    ("C", "Y"): 3 + 3,
    ("A", "Z"): 2 + 6,
    ("B", "Z"): 3 + 6,
    ("C", "Z"): 1 + 6,
}

with open("input.txt") as f:
    for l in f.read().splitlines():
        rps_round = tuple(l.split(" "))

        total_score += rps_score[rps_round]
        total_score_p2 += rps_score_p2[rps_round]

print(total_score)
print(total_score_p2)
