
file_name = 'Day03/input_day03.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(list(line.strip()))

output = 0

# TODO:
#   - Iterate through lines
#   - Save Line before and after
#   - Save numeric position in horizontal string
#   - If char != number or '.' -> test if lines (above, same, below) has number (left, same, right)
#   - Test if number continues
#   - Remove found characters!

def get_entire_number_from_spot(current_line, vert_i, hori_i):
    global input_array
    nb = current_line[hori_i]
    input_array[vert_i][hori_i] = '.'
    # test to the left
    i = hori_i
    while True:
        i -= 1
        if i < 0:
            break
        try:
            new_digit = int(current_line[i])
            nb = str(new_digit) + nb
            input_array[vert_i][i] = '.'
        except ValueError:
            break
    # test to the right
    i = hori_i
    while True:
        i += 1
        if i == len(current_line):
            break
        try:
            new_digit = int(current_line[i])
            nb = nb + str(new_digit)
            input_array[vert_i][i] = '.'
        except ValueError:
            break
    return int(nb)



def test_fields_all_around(vert_i, hori_i):
    global output
    global input_array
    line = input_array[vert_i]

    try:            # test char on the same spot (for the line above and beneath)
        int(line[hori_i])
        output += get_entire_number_from_spot(line, vert_i, hori_i)
        return
    except ValueError:
        pass
    try:            # test char to the left
        if hori_i != 0:
            int(line[hori_i-1])
            output += get_entire_number_from_spot(line,  vert_i, hori_i-1)
    except ValueError:
        pass
    try:            # test char to the right
        if hori_i != len(line)-1:
            int(line[hori_i+1])
            output += get_entire_number_from_spot(line,  vert_i, hori_i+1)
    except ValueError:
        pass



for vertical_i, line in enumerate(input_array):
    for horizontal_i, character in enumerate(line):
        if character == '.':
            continue
        else:
            try:
                number = int(character)
            except ValueError:              # character is a symbol
                test_fields_all_around(vertical_i, horizontal_i)
                if vertical_i != 0:
                    test_fields_all_around(vertical_i-1, horizontal_i)
                if vertical_i != (len(input_array) - 1):
                    test_fields_all_around(vertical_i+1, horizontal_i)

print(output)
