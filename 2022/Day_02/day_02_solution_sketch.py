# A / X = Rock
# B / Y = Paper
# C / Z = Scissors
#
# A > C / Z  Rock > Scissors
# B > A / X Paper > Rock
# C > B / Y  Scissors > Paper
#
# Rock > Scissors > Paper > Rock ...
# Score for each round:
#     shape + outcome
#
# points for shape:
#     Rock    / A / X :   1
#     Paper   / B / Y :   2
#     Scissors/ C / Z :   3
# points for outcome:
#     Loose   :   0
#     Draw    :   3
#     Win     :   6
#
# possible outcomes:
# opponent / you = shape_point + outcome_points
#     A / X = 1 + 3 = 4        1 / 1 -> 1 - 1 =  0 D
#     A / Y = 2 + 6 = 8        1 / 2 -> 1 - 2 = -1 W
#     A / Z = 3 + 0 = 3        1 / 3 -> 1 - 3 = -2 L
#
#     B / X = 1 + 0 = 1        2 / 1 -> 2 - 1 =  1 L
#     B / Y = 2 + 3 = 5        2 / 2 -> 2 - 2 =  0 D
#     B / Z = 3 + 6 = 9        2 / 3 -> 2 - 3 = -1 W
#
#     C / X = 1 + 6 = 7        3 / 1 -> 3 - 1 =  2 W
#     C / Y = 2 + 0 = 2        3 / 2 -> 3 - 2 =  1 L
#     C / Z = 3 + 3 = 6        3 / 3 -> 3 - 3 =  0 D
#
#
#   1 + 1 = 2 D % 3 = 2     + 1 = 3 0
#   1 + 2 = 3 W % 3 = 0     + 1 = 1 1
#   1 + 3 = 4 L % 3 = 1     + 1 = 2 2
#
#   2 + 1 = 3 L % 3 = 0     + 2 = 2 1
#   2 + 2 = 4 D % 3 = 1     + 2 = 3 0
#   2 + 3 = 5 w % 3 = 2     + 2 = 4 2
#
#   3 + 1 = 4 w % 3 = 1     + 3 = 4 2
#   3 + 2 = 5 L % 3 = 2     + 3 = 5 1
#   3 + 3 = 6 D % 3 = 0     + 3 = 6 0
#
#
# Demo Strategy guide
# A > Y
# B > X
# C > Z
# -----
# Simple Solution
# -----
data = open("data.txt").read().split("\n")  # Returns a list of all the games


# def shape_score(input_shape):
#     if input_shape == "X":
#         return 1
#     if input_shape == "Y":
#         return 2
#     if input_shape == "Z":
#         return 3
#
#
# def outcome_score(elf_shape, my_shape):
#     if elf_shape == "A" and my_shape == "X":
#         return 3
#     if elf_shape == "A" and my_shape == "Y":
#         return 6
#     if elf_shape == "A" and my_shape == "Z":
#         return 0
#     if elf_shape == "B" and my_shape == "X":
#         return 0
#     if elf_shape == "B" and my_shape == "Y":
#         return 3
#     if elf_shape == "B" and my_shape == "Z":
#         return 6
#     if elf_shape == "C" and my_shape == "X":
#         return 6
#     if elf_shape == "C" and my_shape == "Y":
#         return 0
#     if elf_shape == "C" and my_shape == "Z":
#         return 3
#
#
# def game_score(input_game):
#     shapes = input_game.split(" ")
#     shape = shape_score(shapes[1])
#     outcome = outcome_score(shapes[0], shapes[1])
#     total = shape + outcome
#     return total

# # Part 1
# def total_score(data):
#     score = 0
#     for game in data:
#         if len(game) > 1:
#             score += game_score(game)
#     return score
#
#
# print(total_score(data))

# ---
# Part 2
# ---
#
# X = Loose
# Y = Draw
# Z = Win


# ----
# Refined solution
# ----


# outcomes = ["D", "W", "L"]
# shapes = ["A", "B", "C", "X", "Y", "Z"]
#
# for i in range(3):
#     for j in range(3):
#         print(f"{i} {j}: {(i + j + i + 1) % 3 * 3} {outcomes[(j - i)]}")
#     print("---")
#
# for first in range(3):
#     for second in range(3, 6):
#         # print(f"{shapes[first]} {shapes[second]}")
#         print(
#             f"{ord(shapes[first])} {ord(shapes[second])} : diff {(ord(shapes[first]) + ord(shapes[second]) + ord(shapes[first]) + 2) % 3}"
#         )
#     print("---")
#
# possible_data = []
# for first in range(3):
#     for second in range(3, 6):
#         # print(f"{shapes[first]} {shapes[second]}")
#         possible_data.append(f"{shapes[first]} {shapes[second]}")
#
# print(possible_data)

# ---
# Part 1
# ---


# def game_score(input_game):
#     shapes = input_game.split(" ")
#     score = (ord(shapes[0]) + ord(shapes[1]) + ord(shapes[0]) + 2) % 3 * 3
#     return score
#
#
# def shape_score(input_game):
#     shapes = input_game.split(" ")
#     score = ord(shapes[1]) % 4 + 1
#     return score
#
#
# def total_score(data):
#     score = 0
#     for game in data:
#         if len(game) > 1:
#             print(
#                 f"game: {game_score(game)} shape: {shape_score(game)} total:{game_score(game) + shape_score(game)}"
#             )
#             score += game_score(game) + shape_score(game)
#     return score
#

#
# print(total_score(data))

# ---
# Part 2
# ---
# X = Loose 0
# Y = Draw 1
# Z = Win 2
#
# A = 1
# B = 2
# C = 3

outcomes = ["X", "Y", "Z"]

# A X -> A C 3      idx + 1 L
# A Y -> A A 1      idx + 0 D
# A Z -> A B 2      idx + 2 W

# B X -> B A 1      idx + 1
# B Y -> B B 2      idx + 0
# B Z -> B C 3      idx + 2 % 3

# C X -> C B 2      idx + 1
# C Y -> C C 3      idx + 0
# C Z -> C A 1      idx + 2


def game_score(letter):
    # The last letter
    return (ord(letter) - 1) % 3 * 3


combos = [
    "A X",
    "A Y",
    "A Z",
    "B X",
    "B Y",
    "B Z",
    "C X",
    "C Y",
    "C Z",
]


def shape_score(pair_of_letters):
    letter = pair_of_letters.split(" ")
    return (ord(letter[0]) + ord(letter[1]) - 1) % 3 + 1


total = 0
for game in data:
    if len(game) > 1:
        gs = game_score(game.split(" ")[1])
        ss = shape_score(game)
        print(f"shape: {ss} game: {gs}  total: {gs + ss} ")
        total += gs + ss

print(total)
