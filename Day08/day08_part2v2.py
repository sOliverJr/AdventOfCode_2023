from math import lcm
from alive_progress import alive_bar

file_name = 'input_day08.txt'
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


iterations_for_loop_of_all_starting_nodes = []
with alive_bar(len(starting_nodes), ) as bar:
    for node in starting_nodes:
        current_node = node
        iterations_for_loop = 0
        i = 0
        while True:
            # Die Art und Weise auf das Ergebnis zu kommen ist falsch und funktioniert nur, weil die Anzahl an Schritten
            # von A -> Z die gleiche ist wie von Z -> Z. A kommt erst viel viel später wieder auf A zurück (+- 6h),
            # womit man hätte das richtige Ergebnis berechnen können...
            if current_node.name[2] == 'Z' and iterations_for_loop != 0:
                break
            if current_node.name == node.name:
                ...
            if i == len(navigation_instructions):
                i = 0
            if navigation_instructions[i] == 'L':
                current_node = node_dict[current_node.left]
            else:
                current_node = node_dict[current_node.right]
            iterations_for_loop += 1
            i += 1
            bar.text(iterations_for_loop)
        iterations_for_loop_of_all_starting_nodes.append(iterations_for_loop)
        print(iterations_for_loop_of_all_starting_nodes)
        bar()

output = lcm(*iterations_for_loop_of_all_starting_nodes)
print(output)
