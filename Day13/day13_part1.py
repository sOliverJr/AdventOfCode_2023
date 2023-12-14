
file_name = 'Day13/input_day13.txt'
input_array = []
file = open(file_name, 'r')
for i, line in enumerate(file):
    input_array.append(list(line.strip()))

field_list = []
field = []
for i, line in enumerate(input_array):
    if i == (len(input_array)-1):
        field.append(line)
        field_list.append(field)
        field = []
        break
    if len(line) == 0:
        field_list.append(field)
        field = []
        continue
    field.append(line)


def is_vertical_symmetrical_axis(offset, field):
    if offset == 0 or offset >= len(field):
        return False
    top = field[:offset][::-1]
    bottom = field[offset:]
    for i, line in enumerate(top):
        if i >= (len(bottom)):
            return True
        if line != bottom[i]:
            return False
    return True


def is_horizontal_symmetrical_axis(offset, field):
    if offset == 0 or offset >= len(field[0]):
        return False

    left = []
    right = []

    for i, line in enumerate(field):
        left_chars = []
        right_chars = []
        for j, character in enumerate(line):
            if j+1 <= offset:
                left_chars.append(character)
            else:
                right_chars.append(character)
        left.append(left_chars[::-1])
        right.append(right_chars)

    for i, line in enumerate(left):
        for j, character in enumerate(line):
            if j >= len(right[i]):
                break
            if character != right[i][j]:
                return False
    return True


def find_vertical_axis(field):
    for offset, line in enumerate(field):
        if is_vertical_symmetrical_axis(offset, field):
            return offset
    return 0


def find_horizontal_axis(field):
    for offset, char in enumerate(field[0]):
        if is_horizontal_symmetrical_axis(offset, field):
            return offset
    return 0


vertical_value = 0
horizontal_value = 0

for field in field_list:
    vertical_value += find_vertical_axis(field)
    horizontal_value += find_horizontal_axis(field)

output = horizontal_value + (100 * vertical_value)
print(output)
