data = open("data_demo.txt").read().splitlines()

x_register = 1
cycle_count = 0
values = []
image = ""


def should_draw(cycle_count, x_value):
    # stuff is 1 indexed
    x_values = [x_value, x_value + 1, x_value + 2]
    if cycle_count % 40 in x_values:
        return "#"  # True
    return "."  # False


for line in data:
    instructions = line.split(" ")
    if instructions[0] == "noop":
        cycle_count += 1

        image += should_draw(cycle_count, x_register)

        if (cycle_count % 40) == 20:
            values.append(cycle_count * x_register)

        if (cycle_count % 40) == 0:
            image += "\n"
    else:
        for i in range(2):
            cycle_count += 1

            image += should_draw(cycle_count, x_register)

            if (cycle_count % 40) == 20:
                values.append(cycle_count * x_register)

            if (cycle_count % 40) == 0:
                image += "\n"

        x_register += int(instructions[1])

part_1_solution = sum(values)  # 13480
part_2_solution = image
print(part_1_solution)
print(part_2_solution)
