
number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

number_dict_reversed = {
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9'
}


file_name = 'Day01/input_day01.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())

output = 0

def test_line(line, numbers_dict):
    string_till_now = ''
    for character in line:
        string_till_now += character

        for number_key in numbers_dict:
            if number_key in string_till_now:
                return numbers_dict[number_key]

        try:
            return int(character)
        except ValueError:
            pass

    return -1

for input_line in input_array:
    input_line_reversed = input_line[::-1]

    first_n = test_line(input_line, number_dict)
    last_n = test_line(input_line_reversed, number_dict_reversed)

    if first_n == -1:
        continue

    if last_n == -1:
        last_n = first_n
    number = str(first_n) + str(last_n)
    output += int(number)

print(output)
