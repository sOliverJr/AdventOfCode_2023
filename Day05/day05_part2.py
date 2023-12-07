from alive_progress import alive_bar

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
del input_array[0:2]


# ['source_start', 'source_end', 'destination_start']
all_map_arr = []
map_arr = []
for i, line in enumerate(input_array):
    if len(line) == 0 or i+1 == len(input_array):
        all_map_arr.append(map_arr)
        map_arr = []
        continue
    else:
        line_values = line.split(' ')
        map_arr.append(Map(int(line_values[0]), int(line_values[1]), int(line_values[2])))

seeds = {}
for i_seed_start, seed_starting_point in enumerate(seed_starting_points):
    with alive_bar(int(seed_amounts[i_seed_start])) as bar:
        for i_amount in range(int(seed_amounts[i_seed_start])):
            seed_number = int(seed_starting_point) + i_amount
            for map_arr in all_map_arr:
                for map in map_arr:
                    new_value_bool, seed_number = map.calculate_new_value_from_instructions(seed_number)
                    if new_value_bool:
                        break
            if seed_number < output:
                output = seed_number
            bar()

print(output)

#
# on 50198205: 4111139999
# |████████████████████████████████████████| 50198205/50198205 [100%] in 9:28.8 (88250.87/s)
# on 110151761: 942937748
# |████████████████████████████████████████| 110151761/110151761 [100%] in 23:54.8 (76773.63/s)
# on 139825503: 714677337
# |████████████████████████████████████████| 139825503/139825503 [100%] in 41:06.1 (56698.40/s)
# on 8913570: 714677337
# |████████████████████████████████████████| 8913570/8913570 [100%] in 1:46.9 (83404.87/s)
# on 489996751: 2520479
# |████████████████████████████████████████| 489996751/489996751 [100%] in 2:27:37.2 (55321.45/s)
# on 100080382: 2520479
# |████████████████████████████████████████| 100080382/100080382 [100%] in 26:34.5 (62764.45/s)
# on 42158689: 2520479
# |████████████████████████████████████████| 42158689/42158689 [100%] in 13:01.7 (53929.52/s)
# on 312026427: 2520479
# |████████████████████████████████████████| 312026427/312026427 [100%] in 1:31:49.6 (56632.93/s)
# on 97088268: 2520479
# |████████████████████████████████████████| 97088268/97088268 [100%] in 24:28.3 (66124.85/s)
# on 336766062: 2520479
# |████████████████████████████████████████| 336766062/336766062 [100%] in 1:34:21.9 (59478.53/s)
# 2520479
