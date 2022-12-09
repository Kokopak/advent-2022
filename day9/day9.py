from collections import defaultdict

motions = []
motion_to_pos = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

with open("input.txt") as f:
    for l in f.read().splitlines():
        d, n = l.split(" ")

        motions.append((motion_to_pos[d], int(n)))


def move_knot(from_knot, to_knot):
    from_row, from_col = from_knot
    to_row, to_col = to_knot

    step_row = 0
    step_col = 0

    if (from_row - to_row, from_col - to_col) in [
        (-1, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (0, 0),
    ]:
        return from_knot

    if from_row == to_row:
        if from_col - to_col == -2:
            step_col = 1
        elif from_col - to_col == 2:
            step_col = -1
    elif from_col == to_col:
        if from_row - to_row == -2:
            step_row = 1
        elif from_row - to_row == 2:
            step_row = -1
    else:
        if from_row > to_row and from_col < to_col:
            step_row = -1
            step_col = 1
        elif from_row > to_row and from_col > to_col:
            step_row = -1
            step_col = -1
        elif from_row < to_row and from_col < to_col:
            step_row = 1
            step_col = 1
        elif from_row < to_row and from_col > to_col:
            step_row = 1
            step_col = -1

    from_knot[0] += step_row
    from_knot[1] += step_col

    return from_knot


def get_tail_moves(n):
    knots = defaultdict(lambda: [15, 11])
    moves = set()
    moves.add(tuple(knots[0]))

    for m_pos, c in motions:
        for _ in range(c):
            knots[0] = [knots[0][0] + m_pos[0], knots[0][1] + m_pos[1]]

            for i in range(1, n + 1):
                m = move_knot(knots[i], knots[i - 1])

                if i == n:
                    moves.add(tuple(m))

    return moves


p1 = get_tail_moves(n=1)
p2 = get_tail_moves(n=9)

print(len(p1))
print(len(p2))
