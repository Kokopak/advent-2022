forest = {}
with open("input.txt") as f:
    forest = {
        (r, c): int(t)
        for r, l in enumerate(f.read().splitlines())
        for c, t in enumerate(list(l))
    }

p1 = 0
p2 = 0


def count_visible_trees(tree, trees):
    count = 0

    for t in trees:
        count += 1
        if t >= tree:
            break

    return count


max_row = max(forest, key=lambda k: k[0])[0]
max_col = max(forest, key=lambda k: k[1])[1]

for (row, col) in forest:
    tree = forest[row, col]

    if row > 0 and row < max_row and col > 0 and col < max_col:
        left_trees = [forest[row, icol] for icol in range(0, col)][::-1]
        right_trees = [forest[row, icol] for icol in range(col + 1, max_col + 1)]
        up_trees = [forest[irow, col] for irow in range(0, row)][::-1]
        down_trees = [forest[irow, col] for irow in range(row + 1, max_row + 1)]

        scenic_score = (
            count_visible_trees(tree, left_trees)
            * count_visible_trees(tree, right_trees)
            * count_visible_trees(tree, up_trees)
            * count_visible_trees(tree, down_trees)
        )

        if (
            max(left_trees) < tree
            or max(right_trees) < tree
            or max(up_trees) < tree
            or max(down_trees) < tree
        ):
            p1 += 1

        if scenic_score > p2:
            p2 = scenic_score

    else:
        p1 += 1

print(p1)
print(p2)
