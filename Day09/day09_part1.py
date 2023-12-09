
file_name = 'Day09/input_day09.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())

input_data = []
for line in input_array:
    line_arr = []
    splitted_strings = line.split(' ')
    for splitted_string in splitted_strings:
        if splitted_string[0] == '-':
            line_arr.append(-int(splitted_string[1:]))
        else:
            line_arr.append(int(splitted_string))
    input_data.append(line_arr)


# -------- calculate new value -------- #

def get_new_value_of_line(line: list):
    differences_between_each_step = []
    for i in range(len(line)-1):
        difference = line[i+1] - line[i]
        differences_between_each_step.append(difference)

    # If every value is '0'
    length_of_new_array = len(differences_between_each_step)
    if differences_between_each_step.count(0) == length_of_new_array:
        return line[len(line) - 1]
    else:
        new_value = line[len(line) - 1] + get_new_value_of_line(differences_between_each_step)
        return new_value


output = 0

for line in input_data:
    output += get_new_value_of_line(line)

print(output)
