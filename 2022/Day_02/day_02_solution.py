data = open("data.txt").read().splitlines()  # Returns a list of all the games
# Super opaque and I have little clue why it works.
# TODO: Write an explanation.

def game_score_p1(input_game):
    shapes = input_game.split(" ")
    shape_score = ord(shapes[1]) % 4 + 1
    game_score = (ord(shapes[0]) + ord(shapes[1]) + ord(shapes[0]) + 2) % 3 * 3
    return shape_score + game_score


def game_score_p2(input_game):
    shapes = input_game.split(" ")
    shape_score = (ord(shapes[0]) + ord(shapes[1]) - 1) % 3 + 1
    game_score = (ord(shapes[1]) - 1) % 3 * 3
    return shape_score + game_score


part_1_solution = sum([game_score_p1(game) for game in data])  # 14827
part_2_solution = sum([game_score_p2(game) for game in data])  # 13889

print(f"Part 1: Total score is {part_1_solution}")
print(f"Part 2: Total score is {part_2_solution}")
