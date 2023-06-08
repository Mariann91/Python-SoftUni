from math import floor

x1, y1, x2, y2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))


def find_distance(input_x, input_y, start_x, start_y):
    return (start_x - input_x)**2 + (start_y - input_y) ** 2


distance_x1_y1 = find_distance(x1, y1, 0, 0)
distance_x2_y2 = find_distance(x2, y2, 0, 0)


if distance_x1_y1 > distance_x2_y2:
    print((x2, y2))
else:
    print((x1, y1))
