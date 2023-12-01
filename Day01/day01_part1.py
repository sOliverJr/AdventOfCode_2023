
def get_input():
    file_name = 'Day01/input_day01.txt'
    input_array = []
    file = open(file_name, 'r')
    for line in file:
        input_array.append(line.strip())
    return input_array

input_lines = get_input()
output = 0

for input_line in input_lines:
    first_n = -1
    last_n = -1
    for character in input_line:
        try:
            n = int(character)
            if first_n == -1:
                first_n = n
            else:
                last_n = n
        except ValueError:
            pass

    if first_n == -1:
        continue

    if last_n == -1:
        last_n = first_n
    number = str(first_n) + str(last_n)
    output += int(number)

print(output)