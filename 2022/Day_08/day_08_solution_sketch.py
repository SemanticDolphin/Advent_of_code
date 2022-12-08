data = open("data.txt").read().splitlines()

data_rows = [list(map(int, x)) for x in data]
data_cols = [list(x) for x in zip(*data_rows)]
# print(len(data_array))
rows = len(data_rows)
columns = len(data_rows[0])


def visible_tree(x, y, input_list):
    point = input_list[x][y]
    left_side = input_list[x][:y]
    right_side = input_list[x][y + 1 :]
    # print(f"point: {point} l: {left_side}, r: {right_side}")
    if left_side == [] or right_side == []:
        return True
    elif point > max(left_side) or point > max(right_side):
        return True
    else:
        return False


def find_distance(input_list, tree):
    return next(
        (i + 1 for i, element in enumerate(input_list) if element >= tree),
        len(input_list),
    )


def calculate_tree_score(row, col):
    point = data_rows[row][col]
    left_side = list(reversed(data_rows[row][:col]))
    right_side = data_rows[row][col + 1 :]
    up_side = list(reversed(data_cols[col][:row]))
    dow_side = data_cols[col][row + 1 :]
    up_score = find_distance(up_side, point)
    down_score = find_distance(dow_side, point)
    left_score = find_distance(left_side, point)
    right_score = find_distance(right_side, point)
    return up_score * down_score * left_score * right_score


# # Part 1
# visible_trees = [[0 for c in range(columns)] for r in range(rows)]
# # print(visible_trees)
#
# for row in range(rows):
#     for column in range(columns):
#         # print(data_rows[row][collumn])
#         # print(
#         #     point_visible(row, collumn, data_rows)
#         #     or point_visible(collumn, row, data_cols)
#         # )
#         if visible_tree(row, column, data_rows) or visible_tree(column, row, data_cols):
#             visible_trees[row][column] = 1
#         else:
#             visible_trees[row][column] = 0
# print(sum([sum(t) for t in visible_trees]))

# # Part 2

tree_scores = [[0 for c in range(columns)] for r in range(rows)]
for row in range(rows):
    for column in range(columns):
        score = calculate_tree_score(row, column)
        tree_scores[row][column] = score

print(tree_scores)
print(max([max(tree) for tree in tree_scores]))


# point = data_rows[1][2]
# left_side = list(reversed(data_rows[1][:2]))
# right_side = data_rows[1][2 + 1 :]
# up_side = list(reversed(data_cols[2][:1]))
# dow_side = data_cols[2][1 + 1 :]
# u_idx_bigger = find_distance(up_side, point)
# d_idx_bigger = find_distance(dow_side, point)
# l_idx_bigger = find_distance(left_side, point)
# r_idx_bigger = find_distance(right_side, point)
#
# print(l_idx_bigger, left_side, point, right_side, r_idx_bigger)
# print(u_idx_bigger, up_side, point, dow_side, d_idx_bigger)
