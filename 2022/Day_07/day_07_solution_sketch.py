data = open("data.txt").read().splitlines()

# print(data)


def count_size_of_file(input_data):
    folders = {}
    active_folders = []
    for idx, line in enumerate(input_data):
        command = line.split(" ")
        command_filesize = 0
        if command[1] == "cd":
            if command[2] == "..":
                active_folders.pop()
            else:
                active_folders.append(f"{command[2]}_{idx}")

        else:
            try:
                command_filesize = int(command[0])
            except ValueError:
                pass
        if command_filesize > 0:
            for folder in active_folders:
                try:
                    folders[folder] += command_filesize
                except KeyError:
                    folders[folder] = command_filesize

    return folders


def find_total_size_above_threshold(data, threshold):
    filtered_dict = list(filter(lambda item: item <= threshold, list(data.values())))
    summed_values = sum(filtered_dict)
    return summed_values


def part_2(data):
    unused_space = 70000000 - data["/_0"]
    needed_space = 30000000 - unused_space
    filtered_dict = list(filter(lambda item: item >= needed_space, list(data.values())))
    min_needed = min(filtered_dict)
    return min_needed


solution_part_1 = find_total_size_above_threshold(count_size_of_file(data), 100000)
solution_part_2 = part_2(count_size_of_file(data))  # 366028

print(f"Total sum is: {solution_part_1}")
print(f"Total size of smalles dir to delete to update is: {solution_part_2}")
