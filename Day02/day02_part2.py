
file_name = 'Day02/input_day03.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())

output = 0

for game in input_array:
    min_amount_of_cubes = {
    'red': 0,
    'green': 0,
    'blue': 0
    }
    game = game.split(': ')
    game_number = int(game[0].split(' ')[1])

    grabs = game[1].split('; ')
    for grab in grabs:
        numbers_and_colors = grab.split(', ')
        for number_and_color in numbers_and_colors:
            number = int(number_and_color.split(' ')[0])
            color = number_and_color.split(' ')[1]
            if number > min_amount_of_cubes[color]:
                min_amount_of_cubes[color] = number

    power = min_amount_of_cubes['red'] * min_amount_of_cubes['green'] * min_amount_of_cubes['blue']
    output += power

print(output)
