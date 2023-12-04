
file_name = 'Day04/input_day04.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())

output = 0

for game in input_array:
    numbers = game.replace('  ', ' ').split(': ')[1]
    winning_numbers = numbers.split(' | ')[0].split(' ')
    my_numbers = numbers.split(' | ')[1].split(' ')
    points_for_game = 0
    for my_number in my_numbers:
        for winning_number in winning_numbers:
            if my_number == winning_number:
                if points_for_game == 0:
                    points_for_game = 1
                else:
                    points_for_game *= 2
    output += points_for_game

print(output)
