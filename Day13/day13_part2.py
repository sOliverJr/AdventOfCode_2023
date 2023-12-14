from Day13.day13_part1 import find_vertical_axis, find_horizontal_axis


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


def test_amount_of_differences_between_two_lines(line_one, line_two):
    amount_of_differences = 0
    for i, character in enumerate(line_one):
        if line_two[i] != line_one[i]:
            amount_of_differences += 1
    return amount_of_differences


def find_vertical_axis_smudge(offset, field):
    if offset == 0 or offset >= len(field):
        return False, field

    top = field[:offset][::-1]
    bottom = field[offset:]

    amount_of_differences = 0
    last_difference_line = -1
    for i, line in enumerate(top):
        if i >= (len(bottom)):
            continue
        if line != bottom[i]:
            amount_of_differences += 1
            last_difference_line = i

    if amount_of_differences == 1:
        if test_amount_of_differences_between_two_lines(top[last_difference_line],
                                                        bottom[last_difference_line]) == 1:
            bottom[last_difference_line] = top[last_difference_line]
            new_field = *top[::-1], *bottom
            return True, new_field

    return False, field


def find_horizontal_axis_smudge(offset, field):
    if offset == 0 or offset >= len(field[0]):
        return False, field

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

    amount_of_differences = 0
    ldl = -1, -1        # ldl: last_difference_line
    for i, line in enumerate(left):
        for j, character in enumerate(line):
            if j >= len(right[i]):
                break
            if character != right[i][j]:
                amount_of_differences += 1
                ldl = i, j

    if amount_of_differences == 1:
        right[ldl[0]][ldl[1]] = left[ldl[0]][ldl[1]]

        new_field = field
        new_field[ldl[0]] = [*left[ldl[0]][::-1], *right[ldl[0]]]

        return True, new_field
    return False, field


def fix_vertical_axis(field):
    for offset, line in enumerate(field):
        fixed, new_field = find_vertical_axis_smudge(offset, field)
        if fixed:
            return True, new_field
    return False, field


def fix_horizontal_axis(field):
    for offset, char in enumerate(field[0]):
        fixed, new_field = find_horizontal_axis_smudge(offset, field)
        if fixed:
            return True, new_field
    return False, field


def is_vertical_symmetrical_axis_v2(offset, field):
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


def is_horizontal_symmetrical_axis_v2(offset, field):
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


def find_vertical_axis_v2(field, index):
    for offset, line in enumerate(field):
        if offset == initial_values[index][0]:
            continue
        if is_vertical_symmetrical_axis_v2(offset, field):
            return offset
    return 0


def find_horizontal_axis_v2(field, index):
    for offset, char in enumerate(field[0]):
        if offset == initial_values[index][1]:
            continue
        if is_horizontal_symmetrical_axis_v2(offset, field):
            return offset
    return 0


# Get Initial values
initial_values = []
for field in field_list:
    initial_values.append([find_vertical_axis(field), find_horizontal_axis(field)])

# Fix Smudges
for x, field in enumerate(field_list):
    fixed, new_field = fix_vertical_axis(field)
    if fixed:
        field_list[x] = new_field
        continue

    fixed, new_field = fix_horizontal_axis(field)
    if fixed:
        field_list[x] = new_field
        continue

    print('oh oh...')


vertical_value = 0
horizontal_value = 0

for y, field in enumerate(field_list):
    vv = find_vertical_axis_v2(field, y)
    hv = find_horizontal_axis_v2(field, y)

    if vv != 0 and hv != 0:
        vv -= initial_values[y][0]
        hv -= initial_values[y][1]
        # print(str(vv) + ', ' + str(hv))

    if vv != 0 and hv != 0:
        print('ANOTHER PROBLEM')
    if vv == 0 and hv == 0:
        print('ANOTHER PROBLEM')

    vertical_value += vv
    horizontal_value += hv

    vv = 0
    hv = 0

output = horizontal_value + (100 * vertical_value)
print(output)

# 47155 -> high
# 46876 -> high
# 27097 -> Low
