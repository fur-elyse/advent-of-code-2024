top_map = []

def find_possible_neighbors(coordinates: tuple):
    row, col = coordinates
    is_up_valid = (row - 1, col) if row - 1 >= 0 else False
    is_down_valid = (row + 1, col) if row + 1 < len(top_map) else False
    is_left_valid = (row, col - 1) if col - 1 >= 0 else False
    is_right_valid = (row, col + 1) if col + 1 < len(top_map[0]) else False
    return [i for i in [is_up_valid, is_down_valid, is_left_valid, is_right_valid] if i != False]

def get_number_from_coordinates(coordinates):
    row, col = coordinates
    return top_map[row][col]


def check_valid_neighbors(coordinates):
    complete_paths = list()
    visited = set()
    valid_coordinates_list = [coordinates]
    
    while len(valid_coordinates_list) > 0:
        current = valid_coordinates_list.pop(0)

        if current not in visited:
            visited.add(current)
        if int(get_number_from_coordinates(current)) == 9:
            complete_paths.append(current)

        valid_neighbors = find_possible_neighbors(current)
        for neighbor in valid_neighbors:
            if neighbor not in visited and int(get_number_from_coordinates(neighbor)) == int(get_number_from_coordinates(current)) + 1:
                valid_coordinates_list.append(neighbor)
    return complete_paths


with open("day10_input.txt") as txt_file:
    for line in txt_file:
        top_map.append(line.strip())


all_zeros = []
for x, row in enumerate(top_map):
    for y, col in enumerate(row):
        if int(col) == 0:
            all_zeros.append((x, y))

result = 0
for curr_coordinates in all_zeros:
    possible_neighbors = find_possible_neighbors(curr_coordinates)
    result += len(check_valid_neighbors(curr_coordinates))
print(result)