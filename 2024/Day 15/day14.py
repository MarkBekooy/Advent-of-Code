width = 101
height = 103
# width = 11
# height = 7


def parse_file(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            p = tuple(map(int, parts[0][2:].split(',')))
            v = tuple(map(int, parts[1][2:].split(',')))
            result.append((p, v))
    return result

def print_grid(points):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for point in points:
        if grid[point[1]][point[0]] == '.':
            grid[point[1]][point[0]] = 1
        else:
            grid[point[1]][point[0]] += 1

    for row in grid:
        print(' '.join(str(cell) for cell in row))
        
file_path = 'input.txt'
parsed_data = parse_file(file_path)

# Part 1
new_points = []
for point, velocity in parsed_data:
    new_point = ((point[0] + velocity[0] * 100) % width, (point[1] + velocity[1] * 100) % height)
    new_points.append(new_point)

def count_points_in_quadrants(points):
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in points:
        if x == mid_x or y == mid_y:
            continue  # Skip points on the middle lines
        if x < mid_x and y < mid_y:
            quadrants[0] += 1  # Top-left quadrant
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1  # Top-right quadrant
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1  # Bottom-left quadrant
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1  # Bottom-right quadrant

    return quadrants

quadrant_counts = count_points_in_quadrants(new_points)
total = 1
for count in quadrant_counts:
    total *= count
print(total)


# Part 2
# for i in range(100):
#     new_points = []
#     for point, velocity in parsed_data:
#         new_point = ((point[0] + velocity[0] * i) % width, (point[1] + velocity[1] * i) % height)
#         new_points.append(new_point)
#         print_grid(new_points)
#         print("-" * 20)