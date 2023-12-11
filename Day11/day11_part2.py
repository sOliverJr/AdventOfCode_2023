
file_name = 'Day11/input_day11.txt'
input_array = []
file = open(file_name, 'r')
for i, line in enumerate(file):
    input_array.append(list(line.strip()))


def get_empty_lines_vertically():
    global input_array
    empty_line_indices = []

    for i, line in enumerate(input_array):
        empty = True
        for character in input_array[i]:
            if character != '.':
                empty = False
                break
        if empty:
            empty_line_indices.append(i)

    return empty_line_indices


def get_empty_lines_horizontally():
    global input_array
    empty_columns_indices = []

    for j in range(len(input_array[0])):
        empty = True
        for line in input_array:
            if line[j] != '.':
                empty = False
                break
        if empty:
            empty_columns_indices.append(j)

    return empty_columns_indices


def get_amount_of_empty_lines_in_between(ss_one, ss_two):
    global empty_line_indices
    global empty_columns_indices

    match ss_one[0] < ss_two[0]:
        case True:
            vertical_range = range(ss_one[0], ss_two[0])
        case False:
            vertical_range = range(ss_two[0], ss_one[0])

    match ss_one[1] < ss_two[1]:
        case True:
            horizontal_range = range(ss_one[1], ss_two[1])
        case False:
            horizontal_range = range(ss_two[1], ss_one[1])

    empty_lines = 0
    empty_columns = 0
    for empty_line_index in empty_line_indices:
        if empty_line_index in vertical_range:
            empty_lines += 1
    for empty_column_index in empty_columns_indices:
        if empty_column_index in horizontal_range:
            empty_columns += 1

    return empty_lines, empty_columns


empty_line_indices = get_empty_lines_vertically()
empty_columns_indices = get_empty_lines_horizontally()

solar_system_index = 1
solar_systems = {}
for i, line in enumerate(input_array):
    for j, character in enumerate(line):
        if character != '.':
            input_array[i][j] = solar_system_index
            solar_systems.update({solar_system_index: (i, j)})
            solar_system_index += 1


# for line in input_array:
#     print(line)

output = 0
solar_system_keys = list(solar_systems.keys())
multiplier = 1000000
while len(solar_system_keys) != 0:
    current_solar_system = solar_system_keys.pop(0)
    ss_one = solar_systems[current_solar_system]
    for solar_system_key in solar_system_keys:
        ss_two = solar_systems[solar_system_key]
        empty_lines, empty_columns = get_amount_of_empty_lines_in_between(ss_one, ss_two)

        empty_lines = (empty_lines * multiplier) - empty_lines
        empty_columns = (empty_columns * multiplier) - empty_columns
        ss_one_copy = ss_one

        # Adjust the bigger j-coordinate
        # (i-coordinate is not necessary because values are calculated from top to bottom)
        if ss_one[1] < ss_two[1]:
            ss_two = ss_two[0], (ss_two[1] + empty_columns)
        else:
            ss_one_copy = ss_one_copy[0], (ss_one_copy[1] + empty_columns)

        ss_two = (ss_two[0] + empty_lines), ss_two[1]
        minimal_distance = (abs(ss_two[0] - ss_one_copy[0]) + abs(ss_two[1] - ss_one_copy[1]))
        output += minimal_distance


print(output)
