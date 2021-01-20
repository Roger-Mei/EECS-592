import csv
from bayes_net_construction import *
from Enumeration_Ask import *

# Read the Bayes' Net file
F = open('bn2.txt', 'r')
READER1 = csv.reader(F)

# Read the input file
G = open('input2.txt', 'r')
READER2 = csv.reader(G)

# Graph Initialization
GRAPH = Graph()

# Construct Bayes' Net graph
PROB_DICT = {} # This dict is used to store the probability table
for rows in READER1:
    # Filter out the comment
    if rows[0][0] == '%':
        continue
    # Filter out the variable declaration line
    if len(rows) > 2 and rows[0][0] != 'P':
        # Variable Declaration
        for i in range(len(rows)):
            rows[i] = rows[i].strip()
            temp_node = Node(rows[i])
            GRAPH.add_node(temp_node)
    # Filter out the probability declaration line and construct the prob_dict
    elif rows[0][0] == 'P':
        # Probability Declaration
        # Probability with no condition or single condition
        if len(rows) == 1:
            prob_key = rows[0][:-4]
            prob_value = float(rows[0][-3:])
            PROB_DICT[prob_key] = prob_value
        # Probability with multiple conditions
        else:
            for i in range(len(rows)):
                if i == 0:
                    prob_key = rows[i]
                elif i == len(rows) - 1:
                    prob_key = str(prob_key) + ',' + str(rows[i][:-4])
                    prob_value = float(rows[i][-1][-3:])
                else:
                    prob_key = prob_key + rows[i]
            prob_value = float(rows[-1][-3:])
            PROB_DICT[prob_key] = prob_value

    elif len(rows) == 2 and rows[0][0] != 'P':
        # Edges
        rows[1] = rows[1].strip()
        GRAPH.node_dict[rows[0]].child.append(GRAPH.node_dict[rows[1]])
        GRAPH.node_dict[rows[1]].parent.append(GRAPH.node_dict[rows[0]])

# Construct the bn.Var
GRAPH.add_Var()

# Define the Query Variable and Evidence
EVIDENCE = []
TEMP_I = 0
for rows in READER2:
    # Filter out the comment line
    if rows[0][0] == '%':
        TEMP_I += 1
        continue
    elif TEMP_I == 1:
        QueryVar = rows[0]
    else:
        for element in rows:
            element = element.strip()
            EVIDENCE.append(element)

# Run the Query Function
Enumeration_Ask(QueryVar, EVIDENCE, GRAPH, PROB_DICT)
