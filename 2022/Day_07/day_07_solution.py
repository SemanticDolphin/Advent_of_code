data = open("data.txt").read().splitlines()


def get_folders_sizes(folder_text):
    folders = {}
    cur_path = []
    for line in folder_text:
        command = line.split(" ")
        filesize = 0
        if not ("dir" in command or "ls" in command):
            if "cd" in command:
                if ".." in command:
                    cur_path.pop()
                else:
                    try:
                        dash = "" if cur_path[-1] == "/" else "/"
                        cur_path.append(f"{cur_path[-1]}{dash}{command[2]}")
                    except IndexError:
                        cur_path.append(command[2])

            else:
                filesize = int(command[0])
            if filesize > 0:
                for folder in cur_path:
                    folders[folder] = folders.get(folder, 0) + filesize
    return folders


def total_size_above_thresh(folders, threshold):
    return sum([value for value in folders.values() if value <= threshold])


def smallest_folder_to_delete(folders):
    needed_space = 30000000 - (70000000 - folders["/"])
    min_file = min([size for size in folders.values() if size >= needed_space])
    return min_file


folder_structure = get_folders_sizes(data)
solution_part_1 = total_size_above_thresh(folder_structure, 100000)
solution_part_2 = smallest_folder_to_delete(folder_structure)

print(f"Total sum is: {solution_part_1}")  # 1086293
print(f"Total size of smalles dir to delete is: {solution_part_2}")  # 366028
