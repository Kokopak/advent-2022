import numpy as np

AIR = 0
ROCK = 1
SAND = 2
ABYSS = -1

cave = np.zeros((1000, 1000))

abyss_row = 0

with open("input.txt") as f:
    for l in f.read().splitlines():
        coords = [
            (int(el.split(",")[0]), int(el.split(",")[1])) for el in l.split(" -> ")
        ]

        for i in range(len(coords) - 1):
            x, y = coords[i]
            x2, y2 = coords[i + 1]

            if x == x2:
                if y <= y2:
                    cave[y : y2 + 1, x] = ROCK
                else:
                    cave[y2 : y + 1, x] = ROCK

            if y == y2:
                if x <= x2:
                    cave[y, x : x2 + 1] = ROCK
                else:
                    cave[y, x2 : x + 1] = ROCK

            abyss_row = max(y, y2) if max(y, y2) > abyss_row else abyss_row


cave_p1 = cave.copy()
cave_p2 = cave.copy()

cave_p1[abyss_row + 1, :] = ABYSS
cave_p2[abyss_row + 2, :] = ROCK


def get_fall_coordinates(cave, r, c, abyss=True):
    origin_r, origin_c = r, c

    while not (
        cave[r + 1, c] in (ROCK, SAND)
        and cave[r + 1, c - 1] in (ROCK, SAND)
        and cave[r + 1, c + 1] in (ROCK, SAND)
    ):

        if abyss and np.any(cave[r, :] == ABYSS):
            return (origin_r, origin_c)

        if not cave[r + 1, c] in (ROCK, SAND):
            r += 1
            continue

        if not cave[r + 1, c - 1] in (ROCK, SAND):
            r += 1
            c -= 1
            continue

        if not cave[r + 1, c + 1] in (ROCK, SAND):
            r += 1
            c += 1
            continue

    return (r, c)


p1 = 0
p2 = 0

fall_coord = get_fall_coordinates(cave_p1, 0, 500)
while fall_coord != (0, 500):
    cave_p1[fall_coord] = SAND
    fall_coord = get_fall_coordinates(cave_p1, 0, 500)

p1 = np.count_nonzero(cave_p1 == SAND)

fall_coord = get_fall_coordinates(cave_p2, 0, 500)
while fall_coord != (0, 500):
    cave_p2[fall_coord] = SAND
    fall_coord = get_fall_coordinates(cave_p2, 0, 500, abyss=False)
cave_p2[fall_coord] = SAND

p2 = np.count_nonzero(cave_p2 == SAND)

print(p1)
print(p2)
