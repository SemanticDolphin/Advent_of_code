data = open("data.txt").read().splitlines()
# print(data)
data = list(data[0])
part_1_substrings = [len(set(data[i : i + 4])) for i in range(len(data) - 4 + 1)]
part_2_substrings = [len(set(data[i : i + 14])) for i in range(len(data) - 14 + 1)]
print(part_2_substrings.index(14) + 14)
