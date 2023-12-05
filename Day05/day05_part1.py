
file_name = 'Day05/input_day05.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    if 'map' not in line:
        input_array.append(line.strip())

output = float('inf')

seeds = {}
for seed in input_array[0].split(': ')[1].split(' '):
    seeds.update({int(seed): int(seed)})
del input_array[0:2]


def map_seeds_to_new_position():
    global seeds
    global mapping_arr
    for seed in seeds:
        for mapping in mapping_arr:
            if mapping[0] <= seeds[seed] <= mapping[1]:
                offset = seeds[seed] - mapping[0]
                seeds[seed] = mapping[2] + offset
                break


# ['source_start', 'source_end', 'destination_start']
mapping_arr = []
for i, line in enumerate(input_array):
    if len(line) == 0 or i+1 == len(input_array):
        map_seeds_to_new_position()
        mapping_arr = []
        continue
    else:
        line_values = line.split(' ')
        mapping_arr.append([int(line_values[1]), ((int(line_values[1]) + int(line_values[2]))-1), int(line_values[0])])

for seed_value in seeds.values():
    if seed_value < output:
        output = seed_value

print(output)