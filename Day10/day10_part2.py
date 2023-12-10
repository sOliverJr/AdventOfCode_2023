import numpy as np


file_name = 'Day10/input_day10.txt'
maze = []
starting_tile = (0, 0)
file = open(file_name, 'r')
for i, line in enumerate(file):
    maze.append(list(line.strip()))
    for j, character in enumerate(list(line.strip())):
        if character == 'S':
            starting_tile = (i, j)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

navigation_help = {
    '|': {'down': (1, 0, 'down'), 'up': (-1, 0, 'up')},
    '-': {'right': (0, 1, 'right'), 'left': (0, -1, 'left')},
    'L': {'down': (0, 1, 'right'), 'left': (-1, 0, 'up')},
    'J': {'right': (-1, 0, 'up'), 'down': (0, -1, 'left')},
    '7': {'right': (1, 0, 'down'), 'up': (0, -1, 'left')},
    'F': {'up': (0, 1, 'right'), 'left': (1, 0, 'down')}

}

def scan_for_starting_pipe(tile):
    global maze
    # test vertically
    next_tile = (0, 0)
    possible_directions = []
    if maze[tile[0]-1][tile[1]] in ['|', 'F', '7']:
        next_tile = (tile[0]-1, tile[1])
        possible_directions.append('up')
    if maze[tile[0]+1][tile[1]] in ['|', 'L', 'J']:
        next_tile = (tile[0]+1, tile[1])
        possible_directions.append('down')
    # test horizontally
    if maze[tile[0]][tile[1]] in ['-', 'J', '7']:
        next_tile = (tile[0], tile[1]+1)
        possible_directions.append('right')
    if maze[tile[0]][tile[1-1]] in ['-', 'F', 'L']:
        next_tile = (tile[0], tile[1]-1)
        possible_directions.append('left')

    if set(['up', 'down']) == set(possible_directions):
        return next_tile, possible_directions.pop(), '/'
    if set(['left', 'right']) == set(possible_directions):
        return next_tile, possible_directions.pop(), '_'
    return next_tile, possible_directions.pop(), 'S'


def get_next_tile(current_tile, where_i_came_from):
    global maze
    current_tile_character = maze[current_tile[0]][current_tile[1]]
    response = navigation_help[current_tile_character][where_i_came_from]
    next_tile = (current_tile[0] + response[0], current_tile[1] + response[1])

    if current_tile_character == '|':
        maze[current_tile[0]][current_tile[1]] = '/'
    elif current_tile_character == '-':
        maze[current_tile[0]][current_tile[1]] = '_'
    elif current_tile_character == 'L':
        maze[current_tile[0]][current_tile[1]] = '⎣'
    elif current_tile_character == 'F':
        maze[current_tile[0]][current_tile[1]] = '⎡'
    elif current_tile_character == 'J':
        maze[current_tile[0]][current_tile[1]] = '⎦'
    elif current_tile_character == '7':
        maze[current_tile[0]][current_tile[1]] = '⎤'

    return next_tile, response[2]


def shoelace_algo(list_of_tiles):
    sum_xa_yb = 0
    for i, tile in enumerate(list_of_tiles):
        if i == len(list_of_tiles)-1:
            sum_xa_yb += list_of_tiles[i][0] * list_of_tiles[0][1]
        else:
            sum_xa_yb += list_of_tiles[i][0] * list_of_tiles[i+1][1]

    sum_ya_xb = 0
    for i, tile in enumerate(list_of_tiles):
        if i == len(list_of_tiles)-1:
            sum_ya_xb += list_of_tiles[i][1] * list_of_tiles[0][0]
        else:
            sum_ya_xb += list_of_tiles[i][1] * list_of_tiles[i+1][0]

    area = abs(sum_xa_yb - sum_ya_xb)
    return area / 2


current_tile, last_direction, new_character = scan_for_starting_pipe(starting_tile)

list_of_pipe_tiles = [starting_tile, current_tile]
amount_of_tiles_in_loop = 1

maze[starting_tile[0]][starting_tile[1]] = new_character
while current_tile != starting_tile:
    current_tile, last_direction = get_next_tile(current_tile, last_direction)
    list_of_pipe_tiles.append(current_tile)
    amount_of_tiles_in_loop += 1

# See shoelace-algorythm!
area = shoelace_algo(list_of_pipe_tiles)

# Pick's theorem:
# area = number_of_points_inside_the_polygon + (number_of_points_on_the_edge / 2) - 1
# <=>
# number_of_points_inside_the_polygon = area - (number_of_points_on_the_edge / 2) + 1
output = area - (amount_of_tiles_in_loop / 2) + 1

print(output)
