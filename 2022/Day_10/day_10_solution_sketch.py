data = open("data.txt").read().splitlines()

x_register = 1
cycle_count = 0
values = []
image = ""
# addx takes two cycles
# noop takes one cycles

##########
# Part 1 #
##########
# for line in data:
#     instructions = line.split(" ")
#     if instructions[0] == "noop":
#         # Start cycle
#         cycle_count += 1
#         if (cycle_count % 40) == 20:
#             # print(f"X: {x_register}, Cycle:{cycle_count}")
#             values.append(cycle_count * x_register)
#     else:
#         cycle_count += 1
#         if (cycle_count % 40) == 20:
#             # print(f"X: {x_register}, Cycle:{cycle_count}")
#             values.append(cycle_count * x_register)
#         cycle_count += 1
#         if (cycle_count % 40) == 20:
#             # print(f"X: {x_register}, Cycle:{cycle_count}")
#             values.append(cycle_count * x_register)
#         x_register += int(instructions[1])

##########
# Part 2 #
##########


def should_draw(cycle_count, x_value):
    # stuff is 1 indexed 
    x_values = [x_value, x_value + 1, x_value + 2]
    if cycle_count % 40 in x_values:
        return True
    return False


for line in data:
    instructions = line.split(" ")
    if instructions[0] == "noop":
        # Start cycle
        cycle_count += 1
        if should_draw(cycle_count, x_register):
            image += "#"
        else:
            image += "."
        
        if (cycle_count % 40) == 0:
            image += "\n"
            # print(f"X: {x_register}, Cycle:{cycle_count}")
            values.append(cycle_count * x_register)
    else:
        cycle_count += 1
        if should_draw(cycle_count, x_register):
            image += "#"
        else:
            image += "."

        if (cycle_count % 40) == 0:
            image += "\n"
            # print(f"X: {x_register}, Cycle:{cycle_count}")
            values.append(cycle_count * x_register)
        
        cycle_count += 1
        if should_draw(cycle_count, x_register):
            image += "#"
        else:
            image += "."
        
        if (cycle_count % 40) == 0:
            image += "\n"
            # print(f"X: {x_register}, Cycle:{cycle_count}")
            values.append(cycle_count * x_register)
        x_register += int(instructions[1])
part_1_solution = sum(values)
print(image)
