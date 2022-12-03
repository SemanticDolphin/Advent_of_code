data = open("data.txt").read().split("\n")[:-1]  # Returns a list of all the games


# ---
# Part 1
# ---


def game_score(input_game):
    shapes = input_game.split(" ")
    score = (ord(shapes[0]) + ord(shapes[1]) + ord(shapes[0]) + 2) % 3 * 3
    return score


def shape_score(input_game):
    shapes = input_game.split(" ")
    score = ord(shapes[1]) % 4 + 1
    return score


def combined_score(input_game):
    shapes = input_game.split(" ")
    shape_score = ord(shapes[1]) % 4 + 1
    game_score = (ord(shapes[0]) + ord(shapes[1]) + ord(shapes[0]) + 2) % 3 * 3
    return shape_score + game_score


def total_score(data):
    score = 0
    for game in data:
        if len(game) > 1:
            score += game_score(game) + shape_score(game)
    return score


score = sum([(game_score(game) + shape_score(game)) for game in data])
combi_score = sum([combined_score(game) for game in data])
combi_score_compact = sum(
    [
        (
            (ord(g.split(" ")[1]) % 4 + 1)
            + (
                (ord(g.split(" ")[0]) + ord(g.split(" ")[1]) + ord(g.split(" ")[0]) + 2)
                % 3
                * 3
            )
        )
        for g in data
    ]
)
print(score)
print(combi_score)
print(combi_score_compact)
print(total_score(data))
# Result: 14827
# ---
# Part 2
# ---


# def game_score(letter):
#     # The last letter
#     return (ord(letter) - 1) % 3 * 3
#
#
# def shape_score(pair_of_letters):
#     letter = pair_of_letters.split(" ")
#     return (ord(letter[0]) + ord(letter[1]) - 1) % 3 + 1
#
#
# def total_score(data):
#     total = 0
#     for game in data:
#         if len(game) > 1:
#             gs = game_score(game.split(" ")[1])
#             ss = shape_score(game)
#             total += gs + ss
#     return total
#
#
# print(total_score(data))
