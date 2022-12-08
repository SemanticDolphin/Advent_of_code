from math import prod

data = open("data.txt").read().splitlines()

data_rows = [list(map(int, x)) for x in data]
data_cols = [list(x) for x in zip(*data_rows)]
rows = len(data_rows)
columns = len(data_rows[0])


def visible_tree(x, y, input_list):
    tree = input_list[x][y]
    left_side = input_list[x][:y]
    right_side = input_list[x][y + 1 :]
    if left_side == [] or right_side == []:
        return True
    elif tree > max(left_side) or tree > max(right_side):
        return True
    else:
        return False


def find_distance(input_list, tree):
    for i, element in enumerate(input_list):
        if element >= tree:
            return i + 1
    return len(input_list)


def calculate_tree_score(row, col):
    tree = data_rows[row][col]
    sides = [
        data_rows[row][:col][::-1],
        data_rows[row][col + 1 :],
        data_cols[col][:row][::-1],
        data_cols[col][row + 1 :],
    ]
    scores = [find_distance(side, tree) for side in sides]
    return prod(scores)


visible_trees = [[0 for c in range(columns)] for r in range(rows)]
tree_scores = [[0 for c in range(columns)] for r in range(rows)]

for row in range(rows):
    for column in range(columns):
        tree_scores[row][column] = calculate_tree_score(row, column)
        if visible_tree(row, column, data_rows) or visible_tree(column, row, data_cols):
            visible_trees[row][column] = 1

solution_part_1 = sum([sum(tree) for tree in visible_trees])
solution_part_2 = max([max(tree) for tree in tree_scores])

print(solution_part_1, solution_part_2)


# Part 1 1715
# Part 2 374400
