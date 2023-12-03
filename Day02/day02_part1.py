
file_name = 'Day02/input_day03.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())

colors_and_max_amount = {
    'red': 12,
    'green': 13,
    'blue': 14
}

output = 0

for game in input_array:
    possible = True
    game = game.split(': ')
    game_number = int(game[0].split(' ')[1])

    grabs = game[1].split('; ')
    for grab in grabs:
        numbers_and_colors = grab.split(', ')
        for number_and_color in numbers_and_colors:
            number = int(number_and_color.split(' ')[0])
            color = number_and_color.split(' ')[1]
            if number > colors_and_max_amount[color]:
                possible = False

    if possible:
        output += game_number

print(output)
