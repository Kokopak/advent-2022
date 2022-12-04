with open("input.txt") as f:
    calories = {}
    cur_elf = 0

    for l in f.read().splitlines():
        l = l.strip()

        if l != "":
            calories[cur_elf] = calories.get(cur_elf, 0) + int(l)
        else:
            cur_elf += 1

print(max(calories.values()))
print(sum(sorted(calories.values(), reverse=True)[:3]))
