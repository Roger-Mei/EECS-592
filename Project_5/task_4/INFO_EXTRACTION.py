from Graph_construction import *
import csv
def INFO_EXTRACTION(tree,temp_list):
    """
    This function will recursively extract information from tree and subtree
    """
    initial_node = tree.node_list[0]
    sort_list = []
    for item in initial_node.child:
        if isinstance(item, Node):
            sort_list.insert(0,item)
        else:
            sort_list.append(item)
    # Judge whether every item in the sort_list is node
    Node_justification_list = []
    for item in sort_list:
        Node_justification_list.append(isinstance(item, Node))
    if all(Node_justification_list):
        for item in sort_list:
            label = tree.edge_dict[initial_node.name, item.name]
            line = str(initial_node.name) + '? ' + str(label) + ', ' + str(item.name) + '\n'
            temp_list.append(line)
        with open('dtree.txt', 'w') as outfile:
            for i in range(len(temp_list)):
                outfile.write(temp_list[i])
        return temp_list
    else:
        for i in range(len(sort_list)):
            if i < len(sort_list)-1:
                # For node condition
                label = tree.edge_dict[initial_node.name, sort_list[i].name]
                line = str(initial_node.name) + '? ' + str(label) + ', ' + str(sort_list[i].name) + '\n'
                temp_list.append(line)
            else:
                label = tree.edge_dict[initial_node.name, sort_list[i].name]
                line = str(initial_node.name) + '? ' + str(label) + ', ' + str(sort_list[i].name) + '?\n'
                temp_list.append(line)
                temp_list = INFO_EXTRACTION(item, temp_list)