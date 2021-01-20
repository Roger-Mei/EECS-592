import copy
from PLURARITY_VALUE import *
from HAVE_SAME_CLASSIFICATOIN import *
from IMPORTANCE import *
from SEARCH import *
from Graph_construction import *
def DECISION_TREE_LEARNING(examples, attributes, parent_examples):
    """
    This function aims to recursively construct the simplest decision tree.
    Input:
    examples is a list whose elements are also lists
    attributes is a dictionary whose key is attibute name and value is the corresponding possible values
    parent_examples is a list whose elements are also lists
    Output:
    it will return a tree structue which is a graph
    """
    if not examples:
        return Node(PLURARITY_VALUE(parent_examples))
    elif HAVE_SAME_CLASSIFICATION(examples):
        return Node(CLASSIFICATION(examples))
    elif not attributes:
        return Node(PLURARITY_VALUE(examples))
    else:
        ImportanceDict = {}
        for a in attributes.keys():
            ImportanceDict[a] = IMPORTANCE(a, examples, attributes)
        # A is the optimal attribute to construct the tree at this step
        A = max(ImportanceDict,key = ImportanceDict.get)
        # Tree is a graph
        tree = Graph()
        # Put the attribute's name A into a node 
        node_A = Node(A)
        # Add A as the root node
        tree.add_vertex(node_A)
        # Deep copy attribute
        temp_attributes = copy.deepcopy(attributes)
        del temp_attributes[A]
        for value in attributes[A]:
            exs = SEARCH(examples, A, value)
            SubTree = DECISION_TREE_LEARNING(exs, temp_attributes, examples)
            # Add Subtree into the graph
            tree.add_vertex(SubTree)
            label = str(value)
            if isinstance(SubTree, Node):
                tree.add_edge(label, node_A, SubTree)
            else:
                SubTree.name = SubTree.node_list[0].name
                tree.add_edge(label, node_A, SubTree)
    return tree