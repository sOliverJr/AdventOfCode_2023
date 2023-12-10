
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
    # test vertically
    if maze[tile[0]-1][tile[1]] in ['|', 'F', '7']:
        return (tile[0]-1, tile[1]), 'up'
    if maze[tile[0]+1][tile[1]] in ['|', 'L', 'J']:
        return (tile[0]+1, tile[1]), 'down'
    # test horizontally
    if maze[tile[0]][tile[1+1]] in ['-', 'J', '7']:
        return (tile[0], tile[1]+1), 'right'
    if maze[tile[0]][tile[1-1]] in ['-', 'F', 'L']:
        return (tile[0], tile[1]-1), 'left'

    print('Additional Exception!')
    raise Exception


def get_next_tile(current_tile, where_i_came_from):
    current_tile_character = maze[current_tile[0]][current_tile[1]]
    response = navigation_help[current_tile_character][where_i_came_from]
    next_tile = (current_tile[0] + response[0], current_tile[1] + response[1])
    return next_tile, response[2]

amount_of_steps_for_iteration = 1
current_tile, last_direction = scan_for_starting_pipe(starting_tile)
while current_tile != starting_tile:
    current_tile, last_direction = get_next_tile(current_tile, last_direction)
    amount_of_steps_for_iteration += 1

print((amount_of_steps_for_iteration)/2)
