from alive_progress import alive_bar


file_name = 'Day14/input_day14.txt'
input_array = []
file = open(file_name, 'r')
for i, line in enumerate(file):
    input_array.append(list(line.strip()))


def move_stone(stone_coordinates, direction):
    global input_array
    destination = ()

    match direction:
        case 'north':
            if stone_coordinates[0] == 0:
                return

            i = stone_coordinates[0]
            i -= 1
            while True:
                if i < 0:
                    destination = (0, stone_coordinates[1])
                    break
                if input_array[i][stone_coordinates[1]] in ['#', 'O']:
                    destination = (i+1, stone_coordinates[1])
                    break
                i -= 1

    input_array[stone_coordinates[0]][stone_coordinates[1]] = '.'
    input_array[destination[0]][destination[1]] = 'O'


def tilt_platform(direction):
    global input_array
    for i, line in enumerate(input_array):
        for j, character in enumerate(line):
            if character == 'O':
                move_stone((i, j), direction)


def get_weight_of_stone(stone_coordinates):
    global input_array
    max_weight = len(input_array)

    stone_weight = abs(stone_coordinates[0] - max_weight)
    return stone_weight


tilt_platform('north')

output = 0
for y, line in enumerate(input_array):
    for x, character in enumerate(line):
        if character == 'O':
            output += get_weight_of_stone((y, x))

print(output)
