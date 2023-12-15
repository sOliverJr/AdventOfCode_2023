import copy
import json

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

        case 'east':
            if stone_coordinates[1] == len(input_array[0])-1:
                return

            i = stone_coordinates[1]
            i += 1
            while True:
                if i == len(input_array[0]):
                    destination = (stone_coordinates[0], len(input_array[0])-1)
                    break
                if input_array[stone_coordinates[0]][i] in ['#', 'O']:
                    destination = (stone_coordinates[0], i-1)
                    break
                i += 1

        case 'south':
            if stone_coordinates[0] == len(input_array)-1:
                return

            i = stone_coordinates[0]
            i += 1
            while True:
                if i == len(input_array):
                    destination = (len(input_array)-1, stone_coordinates[1])
                    break
                if input_array[i][stone_coordinates[1]] in ['#', 'O']:
                    destination = (i-1, stone_coordinates[1])
                    break
                i += 1

        case 'west':
            if stone_coordinates[1] == 0:
                return

            i = stone_coordinates[1]
            i -= 1
            while True:
                if i < 0:
                    destination = (stone_coordinates[0], 0)
                    break
                if input_array[stone_coordinates[0]][i] in ['#', 'O']:
                    destination = (stone_coordinates[0], i+1)
                    break
                i -= 1

    input_array[stone_coordinates[0]][stone_coordinates[1]] = '.'
    try:
        input_array[destination[0]][destination[1]] = 'O'
    except Exception:
        pass


def tilt_platform(direction):
    global input_array

    if direction in ['north', 'west']:
        for i, line in enumerate(input_array):
            for j, character in enumerate(line):
                if character == 'O':
                    move_stone((i, j), direction)

    if direction in ['south', 'east']:
        total_length_i = len(input_array) - 1
        total_length_j = len(input_array[0]) - 1

        for i, line in enumerate(input_array):
            for j, field in enumerate(line):
                coords = (total_length_i - i, total_length_j - j)
                character = input_array[coords[0]][coords[1]]
                if character == 'O':
                    move_stone(coords, direction)


def spin_one_cycle():
    tilt_platform('north')
    tilt_platform('west')
    tilt_platform('south')
    tilt_platform('east')


def get_weight_of_stone(stone_coordinates):
    global input_array
    max_weight = len(input_array)

    stone_weight = abs(stone_coordinates[0] - max_weight)
    return stone_weight


def calculate_weight():
    global input_array
    weight = 0
    for y, line in enumerate(input_array):
        for x, character in enumerate(line):
            if character == 'O':
                weight += get_weight_of_stone((y, x))
    return weight
#
# print()
# for line in input_array:
#     print(line)
# print('-----------------------------------')
# tilt_platform('north')
# for line in input_array:
#     print(line)
# print('-----------------------------------')
# tilt_platform('west')
# for line in input_array:
#     print(line)
# print('-----------------------------------')
# tilt_platform('south')
# for line in input_array:
#     print(line)
# print('-----------------------------------')
# tilt_platform('east')
# for line in input_array:
#     print(line)


with alive_bar(1000000000) as bar:
    past_states = [json.dumps(input_array)]
    input_before = json.dumps(input_array)
    for i in range(1000000000):
        spin_one_cycle()
        bar()
        input_now = json.dumps(input_array)
        if calculate_weight() == 79723:
            print(i)
            print('Got the weight')
            break


print(calculate_weight())

# 153469 -> high
#
# 79723 -> right
