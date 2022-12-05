import re

with open("data_demo.txt") as f:
    data = f.read().splitlines()

stacks = data[: data.index("") - 1]
instructions = data[data.index("") + 1 :]


def convert_stacks_to_colums(input_list):
    split_stacks = [crate.replace("    ", " ").split(" ") for crate in input_list]
    columnar_stacks = [list(stack) for stack in zip(*split_stacks)]
    filtered_stack = [
        list(filter(lambda crate: bool(crate), column)) for column in columnar_stacks
    ]
    return filtered_stack


def parse_instruction(instruction):
    instruction_numbers = list(map(int, re.findall(r"\d+", instruction)))
    return instruction_numbers


def move_crates_1(current_instruction, current_stacks):
    crates, start_crate_idx, end_crate_idx = parse_instruction(current_instruction)
    start_crate = current_stacks[start_crate_idx - 1]
    end_crate = current_stacks[end_crate_idx - 1]
    # Part 1
    for c in range(crates):
        element = start_crate[0]
        end_crate.insert(0, element)
        start_crate.pop(0)
    return current_stacks


def move_crates_2(current_instruction, current_stacks):
    crates, start_crate_idx, end_crate_idx = parse_instruction(current_instruction)
    start_crate = current_stacks[start_crate_idx - 1]
    end_crate = current_stacks[end_crate_idx - 1]
    # Part 2
    end_crate[:0] = start_crate[:crates]
    del start_crate[:crates]
    return current_stacks


def part_1_solution(input_stack, input_instruction):
    stack = convert_stacks_to_colums(stacks)
    for line in instructions:
        stack = move_crates_1(line, stack)
    message = ""
    for crate in stack:
        message += crate[0].replace("[", "").replace("]", "")
        message += re.findall(r"\[([A-Z])\]", crate[0])[0]
    return message


def part_2_solution(input_stack, input_instruction):
    stack = convert_stacks_to_colums(stacks)
    for line in instructions:
        stack = move_crates_2(line, stack)
    message = ""
    for crate in stack:
        # message += crate[0].replace("[", "").replace("]", "")
        message += re.findall(r"\[([A-Z])\]", crate[0])[0]
    return message


solution_part_1 = part_1_solution(stacks, instructions)
solution_part_2 = part_2_solution(stacks, instructions)

print(solution_part_1, solution_part_2)
