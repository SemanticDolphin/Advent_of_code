data = open("data.txt").read()

find_first_char = (
    lambda window_length: [
        len(set(data[i : i + window_length]))
        for i in range(len(data) - window_length + 1)
    ].index(window_length)
    + window_length
)

part_1_solution = find_first_char(4)
part_2_solution = find_first_char(14)

print(f"First start-of-packet marker is detected at {part_1_solution}")
print(f"First start-of-message marker is detected at {part_2_solution}")
