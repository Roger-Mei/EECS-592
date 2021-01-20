"""
This code construct the csp problem. It will be imported into the sudoku.py file. 
"""
import csv
import math

# Construct the CSP problem
class csp():
    def __init__(self, Input):
        self.variable, self.domain = self.get_variable_and_domain(Input)
        self.constraint, self.neighbor_dict = self.get_arcs(Input)
        self.state = Input

    def get_variable_and_domain(self, obj):
        variable_list = {} # Key is the variable's position. Value is the variable's value.
        domain_list = {} # Key is the variable's position. Value is the variable's domain.
        for i in range(len(obj)): # Extract row
            for j in range(len(obj[0])): # Extract column
                position = str(i) + str(j)
                variable_list[position] = int(obj[int(i)][int(j)])
                if int(obj[i][j]) == 0:
                    domain_list[position] = [1,2,3,4,5,6,7,8,9]
                else:
                    domain_list[position] = [int(obj[i][j])]
        return variable_list, domain_list

    def get_arcs(self, obj):
        arcs_list = [] # Elements in arcs_list should take the form as [variable_position, constraint_position]
        neighbor_dict = {} # Keys of the neighbor_dict is the location of certain value, values of this dic is its neighbor's location
        for position in self.variable.keys():
            row = int(position[0])
            col = int(position[1])
            temp_neighbor_list = []
            # Add the row constraints (arcs), which means check horizontally:
            for col_constraint in range(len(obj[0])):
                if col_constraint != col:
                    constraint_position = str(row) + str(col_constraint)
                    temp_neighbor_list.append(constraint_position)
                    arcs_list.append([position, constraint_position])
                    
            
            # Add the column constraints (arcs), which means check vertically:
            for row_constraint in range(len(obj)):
                if row_constraint != row:
                    constraint_position = str(row_constraint) + str(col)
                    temp_neighbor_list.append(constraint_position)
                    arcs_list.append([position, constraint_position])
            
            # Add the block constraints(arcs):
            block_row = math.floor(row/3) # We first localize the corresponding block row numebr
            block_col = math.floor(col/3) # We then localize the corresponding block column number
            for row_constraint in range(3*block_row, 3*block_row+3):
                for col_constraint in range(3*block_col, 3*block_col+3):
                    if row_constraint != row and col_constraint != col:
                        constraint_position = str(row_constraint) + str(col_constraint)
                        if [position, constraint_position] not in arcs_list: # Eliminate the repeated constraints
                            temp_neighbor_list.append(constraint_position)
                            arcs_list.append([position, constraint_position])
            neighbor_dict[position] = temp_neighbor_list
        return arcs_list,neighbor_dict





