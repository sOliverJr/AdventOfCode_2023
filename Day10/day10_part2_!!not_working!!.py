from pprint import pprint


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


def tile_is_infected(current_tile):
    global maze
    # horizontal
    for i in range(len(maze[0])):
        if current_tile[1] + i == len(maze[0]):
            break
        if maze[current_tile[0]][current_tile[1] + i] == '/':
            break
        if maze[current_tile[0]][current_tile[1] + i] == ' ':
            return True
    for i in range(len(maze[0])):
        if current_tile[1] - i < 0:
            break
        if maze[current_tile[0]][current_tile[1] - i] == '/':
            break
        if maze[current_tile[0]][current_tile[1] - i] == ' ':
            return True

    # vertical
    for i in range(len(maze)):
        if current_tile[1] + i == len(maze):
            break
        if maze[current_tile[0] + i][current_tile[1]] == '/':
            break
        if maze[current_tile[0] + i][current_tile[1]] == ' ':
            return True
    for i in range(len(maze)):
        if current_tile[1] - i < 0:
            break
        if maze[current_tile[0] - i][current_tile[1]] == '/':
            break
        if maze[current_tile[0] - i][current_tile[1]] == ' ':
            return True

    return False


def print_maze():
    print('------------------------------------------------------------------')
    for line in maze:
        print(line)

test = 1
current_tile, last_direction, new_character = scan_for_starting_pipe(starting_tile)
maze[starting_tile[0]][starting_tile[1]] = new_character
while current_tile != starting_tile:
    current_tile, last_direction = get_next_tile(current_tile, last_direction)
    test += 1

print('test: ' + str(test/2))

for i, line in enumerate(maze):
    for j, character in enumerate(line):
        if character not in ['/', '_', '⎡', '⎤', '⎣', '⎦', '.', 'S']:
            maze[i][j] = ' '

print_maze()

# Scan and replace all outside blocks with ' '
for i, line in enumerate(maze):
    line_length = len(line) - 1
    # forward
    for j, character in enumerate(line):
        if character == '/':
            break
        if character == 'S':
            continue
        if character not in ['/', '_', '⎡', '⎤', '⎣', '⎦']:
            maze[i][j] = ' '
    # backward
    for j, character in enumerate(line[::-1]):
        if character == '/':
            break
        if character == 'S':
            continue
        if character not in ['/', '_', '⎡', '⎤', '⎣', '⎦']:
            maze[i][line_length - j] = ' '

for i in range(len(maze[0])):       # vertical
    # top to bottom
    for j in range(len(maze)):      # horizontal
        current_character = maze[j][i]
        if current_character == '_':
            break
        if character == 'S':
            continue
        if current_character not in ['/', '_', '⎡', '⎤', '⎣', '⎦']:
            maze[j][i] = ' '
    # bottom to top
    for j in range(len(maze)):
        current_character = maze[len(maze) - 1 - j][i]
        if current_character == '_':
            break
        if character == 'S':
            continue
        if current_character not in ['/', '_', '⎡', '⎤', '⎣', '⎦']:
            maze[len(maze) - 1 - j][i] = ' '

print_maze()

# For all remaining '.', test if they have a ' ' in proximity
for i, line in enumerate(maze):
    for j, character in enumerate(line):
        if character == '.' and tile_is_infected((i, j)):
            maze[i][j] = ' '

print_maze()

output = 0
for i, line in enumerate(maze):
    for j, character in enumerate(line):
        if character == '.':
            output += 1
print(output)

# 3
#