
file_name = 'Day08/input_day08.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


navigation_instructions = list(input_array[0])
del input_array[0:2]

node_dict = {}
for node_line in input_array:
    node_line_split = node_line.split(' = (')
    node_name = str(node_line_split[0])

    related_nodes = node_line_split[1].split(', ')
    node_to_the_left = str(related_nodes[0])
    node_to_the_right = str(related_nodes[1][:-1])

    node_dict.update({node_name: Node(node_name, node_to_the_left, node_to_the_right)})


output = 0

current_node = node_dict['AAA']
i = 0
while current_node.name != 'ZZZ':
    if i == len(navigation_instructions):
        i = 0
    if navigation_instructions[i] == 'L':
        current_node = node_dict[current_node.left]
    else:
        current_node = node_dict[current_node.right]

    output += 1
    i += 1

print(output)
