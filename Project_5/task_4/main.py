import csv
from PARSE import *
from DECISION_TREE_LEARNING import *
from IMPORTANCE import *
from INFO_EXTRACTION import *
# Read the csv file
INPUT = open('examples.txt', 'r')
READER1 = csv.reader(INPUT)

# Indicator flags
ATTRIBUTE_FLAG = 0
DECISION_FLAG = 0
EXAMPLE_FLAG = 0

# Variables
Attributes = {}
Decisions = []
Examples = []

# Parse the input
for rows in READER1:
    if rows[0][0] == '%' and rows[0][2:7] == 'Input':
        ATTRIBUTE_FLAG = 1
    if ATTRIBUTE_FLAG == 1 and rows[0][0] != '%':
        temp_list = PARSE(rows)
        Attributes[temp_list[0]] = []
        for i in range(1, len(temp_list)):
            Attributes[temp_list[0]].append(temp_list[i])
    if rows[0][0] == '%' and rows[0][2:10] == 'Decision':
        ATTRIBUTE_FLAG = 0
        DECISION_FLAG = 1
    if DECISION_FLAG == 1 and rows[0][0] != '%':
        for item in rows:
            Decisions.append(item.strip())
    if rows[0][0] == '%' and rows[0][2:11] == 'Attribute':
        DECISION_FLAG = 0
        EXAMPLE_FLAG = 1
    if EXAMPLE_FLAG == 1 and rows[0][0] != '%':
        temp_list = []
        for item in rows:
            temp_list.append(item.strip())
        Examples.append(temp_list)

# Run the DECISION_TREE_LEARNING function
ParentExamples = []
Tree = DECISION_TREE_LEARNING(Examples, Attributes, ParentExamples)
# Print out result
temp_list = []
result = INFO_EXTRACTION(Tree, temp_list)
    