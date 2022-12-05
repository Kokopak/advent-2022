n_overlap = 0
n_overlap_p2 = 0

with open("input.txt") as f:

    for l in f.read().splitlines():
        section = l.split(",")

        s1_min, s1_max = map(int, section[0].split("-"))
        s2_min, s2_max = map(int, section[1].split("-"))

        if (s1_min <= s2_min and s1_max >= s2_max) or (
            s2_min <= s1_min and s2_max >= s1_max
        ):
            n_overlap += 1

        if not (s1_max < s2_min or s2_max < s1_min):
            n_overlap_p2 += 1


print(n_overlap)
print(n_overlap_p2)
