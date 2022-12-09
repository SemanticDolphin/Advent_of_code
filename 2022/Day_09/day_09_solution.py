data = open("data.txt").read().splitlines()

moves = {
    "D": (0, -1),
    "U": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def convert_to_coordinates(input_lines):
    head = (0, 0)
    points = [head]
    for line in data:
        direction, amount = line.split(" ")
        x, y = moves[direction]
        for i in range(int(amount)):
            head = (head[0] + x, head[1] + y)
            points.append(head)
    return points


def calulate_visited_points(coordinates, knots):
    visited_points = set()
    rope = [(0, 0) for _ in range(knots)]
    for coord in coordinates:
        rope[0] = (coord[0], coord[1])

        for i in range(knots - 1):
            head = rope[i]
            tail = rope[i + 1]

            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]

            if abs(diff_x) > 1 or abs(diff_y) > 1:
                if diff_x == 0:
                    rope[i + 1] = (tail[0], tail[1] + (diff_y // 2))
                elif diff_y == 0:
                    rope[i + 1] = (tail[0] + (diff_x // 2), tail[1])
                else:
                    tx = 1 if diff_x > 0 else -1
                    ty = 1 if diff_y > 0 else -1
                    rope[i + 1] = (tail[0] + tx, tail[1] + ty)
        visited_points.add(rope[-1])
    return len(visited_points)


coordinates = convert_to_coordinates(data)
part_1_solution = calulate_visited_points(coordinates, 2)
part_2_solution = calulate_visited_points(coordinates, 10)

print(part_1_solution)  # 6243
print(part_2_solution)  # 2630
