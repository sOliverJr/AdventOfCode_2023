
file_name = 'Day11/input_day11.txt'
input_array = []
file = open(file_name, 'r')
for i, line in enumerate(file):
    input_array.append(list(line.strip()))


def expand_space_vertically():
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

    offset = 0
    for index in empty_line_indices:
        input_array[index + offset:] = input_array[index + offset], *input_array[index + offset:]
        offset += 1


def expand_space_horizontally():
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

    offset = 0
    for index in empty_columns_indices:
        for i, line in enumerate(input_array):
            input_array[i][index + offset:] = input_array[i][index + offset], *input_array[i][index + offset:]
        offset += 1


expand_space_vertically()
expand_space_horizontally()

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
while len(solar_system_keys) != 0:
    current_solar_system = solar_system_keys.pop(0)
    ss_one = solar_systems[current_solar_system]
    for solar_system_key in solar_system_keys:
        ss_two = solar_systems[solar_system_key]
        minimal_distance = abs(ss_two[0] - ss_one[0]) + abs(ss_two[1] - ss_one[1])
        output += minimal_distance


print(output)
