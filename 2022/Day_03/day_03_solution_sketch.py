data = open("data.txt").read().splitlines()

# ---
# Part 1
# ---

# def find_common_character(input_string):
#     first_half = input_string[: int(len(input_string) / 2)]
#     second_half = input_string[int(len(input_string) / 2) :]
#     common_character = set(first_half).intersection(second_half)
#     return list(common_character)[0]


def calculate_score(input_character):
    if input_character.islower():
        score = ord(input_character) - 96
    else:
        score = ord(input_character) - 64 + 26
    return score


# def calculate_priority(input_string):
#     return calculate_score(find_common_character(input_string))


# total_priority = sum([calculate_priority(package) for package in data])

# print(total_priority)  # Returns 7701

# ---
# Part 2
# ---

# Converting the data in to sets of three elements
# Find intersection of those three elements
# calculate score of the intersection and sum it


def convert_data_to_triples(data):
    data_triples = []
    for idx, item in enumerate(data):
        if idx % 3 == 0:
            triple = []
        triple.append(set(item))
        if len(triple) == 3:
            data_triples.append(triple)
    return data_triples


def common_character_triple(list_of_sets):
    return list(set.intersection(*list_of_sets))[0]


data_3 = convert_data_to_triples(data)

total_priority = sum([calculate_score(common_character_triple(x)) for x in data_3])

print(total_priority)
