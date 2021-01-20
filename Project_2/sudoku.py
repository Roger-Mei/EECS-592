"""
This file includes the main sudoku solver. It should read in a file called "suinput.csv". If you want to 
check the result in the command line, please uncomment the visualize(CSP) line. To run this file, you 
should first create an empty csvfile whose name is "suoutput.csv"!!!
If you wish to test the hardes sudoku problem listed in piazza, please change the file name in line 15 into 
'suinput2.csv'.
"""
import operator
import csv
import copy
import numpy as np
from csp import *


# Read the csv file
FILE = open('suinput2.csv', 'r')
READER = csv.reader(FILE)

# Construct the Sudoku board
BOARD = []
for row in READER:
    BOARD.append(row)

# Construc the CSP problem
CSP = csp(BOARD)

# Define a function to check whether a inconsistency happens
def Inconsistency_check(obj):
    for location in obj.domain.keys():
        # Check whether some certain domain is empty. If yes, return True
        if not obj.domain[location]:
            return True

# Define AC-3 check function
def ac_3(obj):
    # Do inconsistency check first
    if Inconsistency_check(obj):
        return False
    queue = obj.constraint.copy()

    while queue:
        temp_constraint = queue.pop(0)
        x_i = temp_constraint[0]
        x_j = temp_constraint[1]
        if revise(obj, x_i, x_j):
            d_i = obj.domain[x_i] # Extract the domain of X_i
            if len(d_i) == 0:
                return False
            temp_list = obj.neighbor_dict[x_i].copy()
            temp_list.remove(x_j)
            for x_k in temp_list:
                queue.append([x_k, x_i])
    return True

# Define the Revise function. This function returns True iff we revise the domain of X_i
def revise(obj, x_i, x_j):
    revised = False
    d_i = obj.domain[x_i]
    d_j = obj.domain[x_j]
    for domain_value_i in d_i:
        temp_d_j = d_j.copy()
        # If no value in D_j satisfy the constraint between X_i and X_j,
        # delete the domain_value_i in D_i
        if domain_value_i in temp_d_j:
            temp_d_j.remove(domain_value_i)
        if not temp_d_j: # Judge whether the list is empty
            d_i.remove(domain_value_i)
            revised = True
    return revised

# Define the Backtracking function
def backtracking(obj):
    if  assignment_accomplished_check(obj):
        assignment = obj
        return assignment
    # Search for the unassigned variable with shortest domain
    temp_domain_len_dict = {}
    for location in obj.variable.keys():
        if obj.variable[location] == 0:
            temp_domain_len_dict[location] = len(obj.domain[location])
    # Sort the dict by its key which is the length of variable's domain.
    # Note that the sorted_dict is a list of tuples
    sorted_dict = sorted(temp_domain_len_dict.items(), key=operator.itemgetter(1))
    temp_tuple = sorted_dict.pop(0)
    location = temp_tuple[0]
    for domain_value in obj.domain[location]:
        temp_obj = copy.deepcopy(obj)
        temp_obj.variable[location] = domain_value
        temp_obj.domain[location] = [domain_value]

        if ac_3(temp_obj):
            result = backtracking(temp_obj)
            if result != False:
                return result
        temp_obj.variable[location] = 0
        if domain_value in temp_obj.domain[location]:
            temp_obj.domain[location].remove(domain_value)
    return False

# Define function to check whether the assignment is accomplished
def assignment_accomplished_check(obj):
    indicator = False
    sum_of_unassinged_value = 0
    for value in obj.variable.values():
        if value == 0:
            sum_of_unassinged_value += 1
    if sum_of_unassinged_value == 0:
        indicator = True
    return indicator

# Define a visualize function
def visualize(obj):
    for i in range(np.shape(obj.state)[0]):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - - - -')
        for j in range(np.shape(obj.state)[1]):
            location = str(i) + str(j)
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j == 8:
                print(obj.variable[location])
            else:
                print(obj.variable[location], ' ', end='')

# Implement the program!
ac_3(CSP)
Result = backtracking(CSP)

# Uncomment this line if you want to obtain a visual output in your command line.
visualize(Result)

# Write the file into csv file
with open('suoutput.csv', 'w') as outfile:
    for Row in range(np.shape(CSP.state)[0]):
        for Column in range(np.shape(CSP.state)[1]):
            Location = str(Row) + str(Column)
            if Column == 8:
                outfile.write(str(CSP.variable[Location]) + '\n')
            else:
                outfile.write(str(CSP.variable[Location]) + ',')