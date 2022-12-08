from itertools import takewhile

import numpy as np

forest = np.genfromtxt("input.txt", delimiter=1, dtype=int)

p1 = 0
p2 = 0


def count_visible_trees(tree, trees):
    count = 0

    for t in trees:
        count += 1
        if t >= tree:
            break

    return count


for (row, col), tree in np.ndenumerate(forest):

    if (row > 0 and row < len(forest) - 1) and (col > 0 and col < len(forest[0]) - 1):
        left_trees = forest[row, :col][::-1]
        right_trees = forest[row, col + 1 :]
        up_trees = forest[:row, col][::-1]
        down_trees = forest[row + 1 :, col]

        scenic_score = (
            count_visible_trees(tree, left_trees)
            * count_visible_trees(tree, right_trees)
            * count_visible_trees(tree, up_trees)
            * count_visible_trees(tree, down_trees)
        )

        if (
            np.all(left_trees - tree < 0)
            or np.all(right_trees - tree < 0)
            or np.all(up_trees - tree < 0)
            or np.all(down_trees - tree < 0)
        ):
            p1 += 1

        if scenic_score > p2:
            p2 = scenic_score

    else:
        p1 += 1

print(p1)
print(p2)
