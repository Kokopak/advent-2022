import numpy as np

AIR = 0
ROCK = 1
SAND = 2
ABYSS = -1

cave = np.zeros((600, 600))

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

cave[abyss_row + 1, :] = ABYSS


def get_fall_coordinates(cave, r, c):
    diag = -1

    origin_r, origin_c = r, c

    while not (
        cave[r + 1, c] in (ROCK, SAND)
        and cave[r + 1, c - 1] in (ROCK, SAND)
        and cave[r + 1, c + 1] in (ROCK, SAND)
    ):

        if np.any(cave[r, :] == ABYSS):
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


fall_coord = get_fall_coordinates(cave, 0, 500)

while fall_coord != (0, 500):
    cave[fall_coord] = SAND
    fall_coord = get_fall_coordinates(cave, 0, 500)


print(np.count_nonzero(cave == SAND))
