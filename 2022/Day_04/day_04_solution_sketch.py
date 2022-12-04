data = open("data.txt").read().splitlines()

# Part 1
# total_pairs = 0

# for line in data:
#     section_ids_a, section_ids_b = line.split(",")
#     a_start = int(section_ids_a.split("-")[0])
#     a_end = int(section_ids_a.split("-")[1])
#     a_set = set(range(a_start, a_end + 1))
#
#     b_start = int(section_ids_b.split("-")[0])
#     b_end = int(section_ids_b.split("-")[1])
#     b_set = set(range(b_start, b_end + 1))
#     if (a_set.issubset(b_set) or b_set.issubset(a_set)):
#         total_pairs += 1
#
# print(total_pairs)  # 644

# Part 2
total_pairs = 0

for line in data:
    section_ids_a, section_ids_b = line.split(",")
    a_start = int(section_ids_a.split("-")[0])
    a_end = int(section_ids_a.split("-")[1])
    a_set = set(range(a_start, a_end + 1))

    b_start = int(section_ids_b.split("-")[0])
    b_end = int(section_ids_b.split("-")[1])
    b_set = set(range(b_start, b_end + 1))
    if a_set & b_set:
        total_pairs += 1

print(total_pairs)  # 926
