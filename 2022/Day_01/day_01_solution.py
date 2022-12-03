# Quick solution
#
# fhand = open("data.txt")
# data = [[]]

# for line in fhand:
#     # print(f"line: {line}")
#     if line == "\n":
#         data.append([])
#     else:
#         data[-1].append(int(line.strip("\n")))
#
# for idx, elf in enumerate(data):
#     data[idx] = sum(elf)
#
# data.sort(reverse=True)
#
# print(sum(data[:3]))
# ---
#
# Improved solution

data = open("data.txt").read().split("\n\n")

answer_1 = max([sum(map(int, elf.split())) for elf in data])
answer_2 = sum(sorted([sum(map(int, elf.split())) for elf in data])[-3:])

print(f"""Answer 1: {answer_1}\nAnswer 2: {answer_2}""")
