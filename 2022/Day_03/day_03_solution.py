data = open("data.txt").read().splitlines()


def convert_data_to_triples(data):
    data_triples = []
    for idx, item in enumerate(data):
        if idx % 3 == 0:
            triple = []
        triple.append(set(item))
        if len(triple) == 3:
            data_triples.append(triple)
    return data_triples


def split_package_in_two(input_string):
    first_half = input_string[: int(len(input_string) / 2)]
    second_half = input_string[int(len(input_string) / 2) :]
    return [set(first_half), set(second_half)]


def common_character(list_of_sets):
    common_character = list(set.intersection(*list_of_sets))[0]
    return common_character


def calculate_score(input_character):
    if input_character.islower():
        score = ord(input_character) - 96
    else:
        score = ord(input_character) - 64 + 26
    return score


def calculate_priority_p_1(input_string):
    return calculate_score(common_character(split_package_in_two(input_string)))


def calculate_priority_p_2(input_string):
    return calculate_score(common_character(input_string))


part_1_total_priority = sum([calculate_priority_p_1(package) for package in data])
part_2_total_priority = sum(
    [calculate_priority_p_2(package) for package in convert_data_to_triples(data)]
)

print(f"Part 1: Total priority is {part_1_total_priority}")  # Returns 7701
print(f"Part 2: Total priority is {part_2_total_priority}")  # Returns 2644
