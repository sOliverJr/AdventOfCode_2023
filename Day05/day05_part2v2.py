from alive_progress import alive_bar
class Seed:
    def __init__(self, seed_range_start, seed_range_end):
        self.start = seed_range_start
        self.end = seed_range_end

class Map:
    def __init__(self, destination_start, source_start, range_length):
        self.destination_start = destination_start
        self.source_start = source_start
        self.range_length = range_length
        self.source_end = self.source_start + self.range_length -1

    def calculate_range_that_fits_and_return_rest(self, seed_range: Seed):
        """
        Returns two Seed-objects. The first one did not fit, the second one did
        """
        if self.source_start <= seed_range.start <= self.source_end:
            # If entire seed-range fits in the map range
            if seed_range.end <= self.source_end:
                return [Seed(self.destination_start, seed_range)]
            # If only part of the seeds fit in the map range
            else:
                overflow = seed_range.end - self.source_end
                first_element_that_does_not_fit = seed_range.end - overflow + 1
                return [Seed(first_element_that_does_not_fit, seed_range.end), Seed(seed_range.start, seed_range.end-overflow)]
        elif self.source_start <= seed_range.end <= self.source_end:
            overflow = seed_range.end - self.source_start
            last_element_that_does_not_fit = seed_range.end - overflow - 1
            return [Seed(seed_range.start, last_element_that_does_not_fit),
                    Seed(seed_range.end - overflow, seed_range.end)]
        elif seed_range.start < self.source_start and seed_range.end > self.source_end:
            print('ALL HOPE IS LOST')
            raise Exception('exiting....')
        # If none of the seeds fit in the range
        else:
            return [seed_range]


# Getting file as array of lines
file_name = 'Day05/input_day05.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    if 'map' not in line:
        input_array.append(line.strip())

# Output = inf
output = float('inf')

# Get a list of seeds and their range
seeds_array_unformatted = input_array[0].split(': ')[1].split(' ')
seed_range_array = []
i = 0
while i < len(seeds_array_unformatted):
    seed_starting_point = seeds_array_unformatted[i]
    seed_amount = seeds_array_unformatted[i+1]
    seed_range_array.append(Seed(seed_starting_point, (seed_starting_point + seed_amount - 1)))
    i += 2

# Remove first two lines of input_file
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

def ka():
    for map in map_arr:
        response = map.calculate_range_that_fits_and_return_rest(seed_range)
        if response[1] is None:
            continue

        new_calculated_range.extend(calculated_range[1])
        if response[0] is None:
            break
        else:

new_seed_range = []
calculated_range = seed_range_array
for map_arr in all_map_arr:
    for seed_range in calculated_range:
        new_calculated_range = []
        unchanged_ranges = []


        calculated_range = new_calculated_range





print(output)
