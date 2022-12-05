import re

# Part 1

# data = open("data.txt").read().splitlines()
data = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2".split("\n")
# Split data into the stacks and instructions
stacks = data[: data.index("") - 1]
stacks_width = int(data[data.index("") - 1].replace(" ", "")[-1])
instructions = data[data.index("") + 1 :]


# Create an empty array for new stacks data shape
stacks_data = []
for stack in range(stacks_width):
    stacks_data.append([])

crates_regex = re.compile(r"\[([A-Z])\]")
# Populate the new stacks data with each stack of crates
for stack in stacks:
    crates = stack.replace("    ", " ").split(" ")
    # crates = crates_regex.findall(stack)
    for idx, crate in enumerate(crates):
        if bool(crate):
            stacks_data[idx].append(crate)

# Parse instructions:
for step in instructions:
    amount_of_crates, start_stack_index, end_stack_index = re.findall(r"\d+", step)
    start_stack = stacks_data[int(start_stack_index) - 1]
    end_stack = stacks_data[int(end_stack_index) - 1]
    print(step)
    # Part 1
    # for c in range(int(amount_of_crates)):
    #     element = start_stack[0]
    #     end_stack.insert(0, element)
    #     start_stack.pop(0)
    # Part 2
    # for c in range(int(amount_of_crates)):
    # elements = start_stack[0 : int(amount_of_crates)]
    # for element in reversed(elements):
    #     end_stack.insert(0, element)
    #     start_stack.pop(0)
    end_stack[:0] = start_stack[:int(amount_of_crates)]
    del start_stack[:int(amount_of_crates)]
#
#
message = ""
for data in stacks_data:
    message += data[0]

print(stacks_data)
print(message) #Expected output is MCD
