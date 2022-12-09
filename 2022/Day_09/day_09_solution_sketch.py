# This day broke me brain
# Shout out to hyper-neutrino for shairng an excellent guide
# https://github.com/hyper-neutrino/advent-of-code

data = open("data.txt").read().splitlines()

directions = {
    "D": (0, -1),
    "U": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def parse_input(input_lines):
    head = (0, 0)
    points = [head]
    for line in data:
        direction, amount = line.split(" ")
        x, y = directions[direction]
        for i in range(int(amount)):
            head = (head[0] + x, head[1] + y)
            points.append(head)
    return points


def part1(coordinates):
    tail = (0, 0)
    visited_positions = set()
    for head in coordinates:
        dx = head[0] - tail[0]
        dy = head[1] - tail[1]

        if abs(dx) > 1 or abs(dy) > 1:
            if dx == 0:
                tail = (tail[0], tail[1] + (dy // 2))
            elif dy == 0:
                tail = (tail[0] + (dx // 2), tail[1])
            else:
                tx = 1 if dx > 0 else -1
                ty = 1 if dy > 0 else -1
                tail = (tail[0] + tx, tail[1] + ty)
        visited_positions.add(tail)
    return len(visited_positions)


def part2(coordinates):
    visited_points = set()
    rope = [(0, 0) for _ in range(10)]
    for coord in coordinates:
        rope[0] = (coord[0], coord[1])

        for i in range(9):
            head = rope[i]
            tail = rope[i + 1]

            dx = head[0] - tail[0]
            dy = head[1] - tail[1]

            if abs(dx) > 1 or abs(dy) > 1:
                if dx == 0:
                    rope[i + 1] = (tail[0], tail[1] + (dy // 2))
                elif dy == 0:
                    rope[i + 1] = (tail[0] + (dx // 2), tail[1])
                else:
                    tx = 1 if dx > 0 else -1
                    ty = 1 if dy > 0 else -1
                    rope[i + 1] = (tail[0] + tx, tail[1] + ty)
        visited_points.add(rope[9])
    return len(visited_points)


def calulate_visited_points(coordinates, knots):
    visited_points = set()
    rope = [(0, 0) for _ in range(knots)]
    for coord in coordinates:
        rope[0] = (coord[0], coord[1])

        for i in range(knots - 1):
            head = rope[i]
            tail = rope[i + 1]

            dx = head[0] - tail[0]
            dy = head[1] - tail[1]

            if abs(dx) > 1 or abs(dy) > 1:
                if dx == 0:
                    rope[i + 1] = (tail[0], tail[1] + (dy // 2))
                elif dy == 0:
                    rope[i + 1] = (tail[0] + (dx // 2), tail[1])
                else:
                    tx = 1 if dx > 0 else -1
                    ty = 1 if dy > 0 else -1
                    rope[i + 1] = (tail[0] + tx, tail[1] + ty)
        visited_points.add(rope[-1])
    return len(visited_points)


coordinates = parse_input(data)
part_1_solution = calulate_visited_points(coordinates, 2)
part_2_solution = calulate_visited_points(coordinates, 10)
print(part_1_solution)
print(part_2_solution)
# print(coordinates)
# print(part1(coordinates))
# print(part2(coordinates))

# head_pos = (0, 0)
# # prev_head_pos = (0, 0)
# tail_pos = (0, 0)
# visited_points = set()
# visited_points.add((tail_pos))
#
# for line in data:
#     direction, amount = line.split(" ")
#     x, y = directions[direction]
#     for a in range(int(amount)):
#         # prev_head_pos = head_pos
#         head_pos = (head_pos[0] + x, head_pos[1] + y)
#
#         dx = head_pos[0] - tail_pos[0]
#         dy = head_pos[1] - tail_pos[1]
#
#         if abs(dx) > 1:
#             dx_diff = int(dx / abs(dx))
#             tail_pos = (tail_pos[0] + dx_diff, tail_pos[1])
#         if abs(dy) > 1:
#             dy_diff = int(dy / abs(dy))
#             tail_pos = (tail_pos[0], tail_pos[1] + dy_diff)
#         visited_points.add(tail_pos)
#         # if check_distance(head_pos, tail_pos):
#         #     tail_pos = prev_head_pos
#         #     visited_points.add((tail_pos))

# print(len(visited_points))
