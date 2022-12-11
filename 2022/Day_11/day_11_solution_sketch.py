from math import prod

data = open("data.txt").read().split("\n\n")


def parse_monkey(monkey_data):
    m_stats = monkey_data.split("\n")[1:]
    starting_items = list(map(int, m_stats[0].split(":")[1].split(",")))
    op_values = m_stats[1].split("= ")[1].split(" ")
    operation_func = eval(
        f"lambda {op_values[0]}: {op_values[0]} {op_values[1]} {op_values[2]}"
    )
    test_number = int(m_stats[2].split(" ")[-1])
    test_func = lambda item: item % test_number == 0
    test_true = int(m_stats[3].split(" ")[-1])
    test_false = int(m_stats[4].split(" ")[-1])

    monkey = {
        "starting items": starting_items,
        "operation": operation_func,
        "test": test_func,
        "test_number": test_number,
        "truthy": test_true,
        "falsy": test_false,
        "inspection": 0,
    }
    return monkey


def parse_into_monkeys(raw_data):
    monkeys = []
    for monkey in raw_data:
        monkeys.append(parse_monkey(monkey))

    return monkeys


def simulate_round(monkeys_list):
    monkeys = list(monkeys_list)
    for monkey in monkeys:
        items = monkey["starting items"]
        operated_items = [monkey["operation"](item) for item in items]
        # Part 1
        # calmed_items = [int(item / 3) for item in operated_items]

        # Part 2
        calmed_items = [item % prime_factor for item in operated_items]

        for item in calmed_items:
            monkey["inspection"] += 1
            if monkey["test"](item):
                monkeys[monkey["truthy"]]["starting items"].append(item)
            else:
                monkeys[monkey["falsy"]]["starting items"].append(item)
        monkey["starting items"] = []

    return monkeys


monkeys = parse_into_monkeys(data)
prime_factor = prod([m["test_number"] for m in monkeys])
print(prime_factor)
for i in range(10000):
    monkeys = simulate_round(monkeys)


monkey_business = prod(sorted([m["inspection"] for m in monkeys])[-2:])

print(monkey_business)
