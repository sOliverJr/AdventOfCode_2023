
input = [{'time': 42, 'distance': 284}, {'time': 68, 'distance': 1005}, {'time': 69, 'distance': 1122}, {'time': 85, 'distance': 1341}]

output = 1

for race in input:
    number_of_ways_to_win = 0
    for i in range(race['time']):
        speed = i
        distance = speed * (race['time'] - i)
        if distance > race['distance']:
            number_of_ways_to_win += 1
    output *= number_of_ways_to_win

print(output)
