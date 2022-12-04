data = open("data.txt").read().splitlines()


def convert_to_set(data_line):
    a_ids, b_ids = data_line.split(",")
    a_start, a_end = a_ids.split("-")
    b_start, b_end = b_ids.split("-")
    a_set = set(range(int(a_start), int(a_end) + 1))
    b_set = set(range(int(b_start), int(b_end) + 1))
    return [a_set, b_set]


def check_subsset(pair_of_sets):
    return pair_of_sets[0].issubset(pair_of_sets[1]) or pair_of_sets[1].issubset(
        pair_of_sets[0]
    )


def check_overlap(pair_of_sets):
    return bool(pair_of_sets[0] & pair_of_sets[1])


solution_part_1 = sum([check_subsset(convert_to_set(ids)) for ids in data])
solution_part_2 = sum([check_overlap(convert_to_set(ids)) for ids in data])

print(
    f"In how many assignment pairs does one range fully contain the other?: {solution_part_1}"
)
print(f"In how many assignment pairs do the ranges overlap?: {solution_part_2}")
