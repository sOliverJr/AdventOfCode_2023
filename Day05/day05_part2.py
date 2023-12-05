
class Map:
    def __init__(self, destination_start, source_start, range_length):
        self.destination_start = destination_start
        self.source_start = source_start
        self.range_length = range_length
        self.source_end = self.source_start + self.range_length -1

    def calculate_new_value_from_instructions(self, position):
        if self.source_start <= position <= self.source_end:
            offset = position - self.source_start
            new_value = self.destination_start + offset
            return True, new_value
        else:
            return False, position


file_name = 'Day05/input_day05.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    if 'map' not in line:
        input_array.append(line.strip())

output = float('inf')

seeds_array = input_array[0].split(': ')[1].split(' ')
seed_starting_points = seeds_array[0::2]
seed_amounts = seeds_array[1::2]

seeds = {}
for i_seed_start, seed_starting_point in enumerate(seed_starting_points):
    for i_amount in range(int(seed_amounts[i_seed_start])):
        seed_number = int(seed_starting_point) + i_amount
        seeds.update({seed_number: seed_number})
del input_array[0:2]


def map_seeds_to_new_position():
    global seeds
    global map_arr
    for seed in seeds:
        for map in map_arr:
            new_value_bool, seeds[seed] = map.calculate_new_value_from_instructions(seeds[seed])
            if new_value_bool:
                break


# ['source_start', 'source_end', 'destination_start']
map_arr = []
for i, line in enumerate(input_array):
    if len(line) == 0 or i+1 == len(input_array):
        map_seeds_to_new_position()
        map_arr = []
        continue
    else:
        line_values = line.split(' ')
        map_arr.append(Map(int(line_values[0]), int(line_values[1]), int(line_values[2])))

for seed_value in seeds.values():
    if seed_value < output:
        output = seed_value

print(output)
