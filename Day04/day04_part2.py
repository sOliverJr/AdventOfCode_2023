
file_name = 'Day04/input_day04.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())

output = 0
amount_of_scratch_cards = [1] * (len(input_array))

for i, game in enumerate(input_array):
    numbers = game.replace('  ', ' ').split(': ')[1]
    winning_numbers = numbers.split(' | ')[0].split(' ')
    my_numbers = numbers.split(' | ')[1].split(' ')
    points_for_game = 0
    for my_number in my_numbers:
        for winning_number in winning_numbers:
            if my_number == winning_number:
                    points_for_game += 1

    for points in range(points_for_game):
        amount_of_scratch_cards[i + points + 1] += amount_of_scratch_cards[i]

for games in amount_of_scratch_cards:
    output += games

print(output)
