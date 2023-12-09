
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


def test_if_done(node_list: list[Node]):
    amount_of_final_nodes = 0
    for node in node_list:
        node_name = node.name[2]
        if node_name == 'Z':
            amount_of_final_nodes += 1

    if amount_of_final_nodes > 3:
        print('AHHHHH')

    return amount_of_final_nodes == len(node_list)


navigation_instructions = list(input_array[0])
del input_array[0:2]

starting_nodes = []
node_dict = {}
for node_line in input_array:
    node_line_split = node_line.split(' = (')
    node_name = str(node_line_split[0])

    related_nodes = node_line_split[1].split(', ')
    node_to_the_left = str(related_nodes[0])
    node_to_the_right = str(related_nodes[1][:-1])

    node_dict.update({node_name: Node(node_name, node_to_the_left, node_to_the_right)})
    if node_name[2] == 'A':
        starting_nodes.append(Node(node_name, node_to_the_left, node_to_the_right))


output = 0

current_nodes = starting_nodes
i = 0
done = False
while not done:
    if i == len(navigation_instructions):
        i = 0

    for j, current_node in enumerate(current_nodes):
        if navigation_instructions[i] == 'L':
            new_node_name = current_node.left
            current_nodes[j] = node_dict[new_node_name]
        else:
            new_node_name = current_node.right
            current_nodes[j] = node_dict[new_node_name]

    output += 1
    i += 1

    done = test_if_done(current_nodes)

print(output)
