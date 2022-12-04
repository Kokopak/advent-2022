import string

priorities = string.ascii_lowercase + string.ascii_uppercase

sum_priorities = 0
sum_priorities_p2 = 0

n_elf = 0
elves_badge = None

with open("input.txt") as f:

    for l in f.read().splitlines():
        size = len(l) // 2
        fc, sc = set(l[:size]), set(l[size:])

        sum_priorities += priorities.index((fc & sc).pop()) + 1

        if n_elf % 3 == 0:
            elves_badge = set(l)

        elves_badge &= set(l)

        if len(elves_badge) == 1:
            sum_priorities_p2 += priorities.index(elves_badge.pop()) + 1

        n_elf += 1


print(sum_priorities)
print(sum_priorities_p2)
