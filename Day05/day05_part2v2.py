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

    def calculate_range_that_fits_and_return_rest(self, seed_ranges: list[Seed]):
        """
        Returns two Seed-objects. The first one did not fit, the second one did
        """
        ranges_that_fitted = []
        ranges_that_did_not_fit = []

        for seed_range in seed_ranges:
            if self.source_start <= seed_range.start <= self.source_end:
                # If entire seed-range fits in the map range
                if seed_range.end <= self.source_end:
                    offset = seed_range.start - self.source_start
                    delta = seed_range.end - seed_range.start
                    ranges_that_fitted.append(Seed(self.destination_start + offset, self.destination_start + offset + delta))
                # If only part of the seeds fit in the map range
                else:
                    overflow = seed_range.end - self.source_end
                    delta = self.source_end - seed_range.start
                    offset = seed_range.start - self.source_start
                    first_element_that_does_not_fit = seed_range.end - overflow + 1
                    ranges_that_fitted.append(Seed(self.destination_start + offset, self.destination_start + offset + delta))
                    ranges_that_did_not_fit.append(Seed(first_element_that_does_not_fit, seed_range.end))
            elif self.source_start <= seed_range.end <= self.source_end:
                delta = seed_range.end - self.source_start
                last_element_that_does_not_fit = self.source_start - 1
                ranges_that_fitted.append(Seed(self.destination_start, self.destination_start + delta))
                ranges_that_did_not_fit.append(Seed(seed_range.start, last_element_that_does_not_fit))
            elif seed_range.start < self.source_start and seed_range.end > self.source_end:
                # seed_range = 50   -   150
                # map_range=     75 - 125
                left_last_element_that_does_not_fit = self.source_start-1
                right_first_element_that_does_not_fit = self.source_end+1
                start_element_that_fits = self.destination_start
                end_element_that_fits = self.destination_start + self.range_length - 1
                ranges_that_fitted.append(Seed(start_element_that_fits, end_element_that_fits))
                ranges_that_did_not_fit.append(Seed(seed_range.start, left_last_element_that_does_not_fit))
                ranges_that_did_not_fit.append(Seed(right_first_element_that_does_not_fit, seed_range.end))
            # If none of the seeds fit in the range
            else:
                ranges_that_did_not_fit.append(seed_range)

        return ranges_that_fitted, ranges_that_did_not_fit


# Getting file as array of lines
file_name = 'input_day05.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    if 'map' not in line:
        input_array.append(line.strip())


# Get a list of seeds and their range
seeds_array_unformatted = input_array[0].split(': ')[1].split(' ')
seed_range_array = []
i = 0
while i < len(seeds_array_unformatted):
    seed_starting_point = seeds_array_unformatted[i]
    seed_amount = seeds_array_unformatted[i+1]
    seed_range_array.append(Seed(int(seed_starting_point), (int(seed_starting_point) + int(seed_amount) - 1)))
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


def put_ranges_trough_mapping(ranges: list[Seed], mappings: list[Map]):
    mapped_ranges = []
    for mapping in mappings:
        fitted_ranges, not_fitted_ranges = mapping.calculate_range_that_fits_and_return_rest(ranges)
        mapped_ranges.extend(fitted_ranges)
        ranges = not_fitted_ranges
    mapped_ranges.extend(ranges)
    return mapped_ranges


final_ranges = []
with alive_bar(len(seed_range_array)) as bar:
    for seed_range in seed_range_array:
        previous_range = [seed_range]
        for map_set in all_map_arr:
            previous_range = put_ranges_trough_mapping(previous_range, map_set)
        final_ranges.extend(previous_range)
        bar()


# Output = inf
output = float('inf')

for range in final_ranges:
    if range.start < output:
        output = range.start

print(output)
