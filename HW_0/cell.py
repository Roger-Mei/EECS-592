import random

# Cell automaton
def cell(noc, nog):
    cell = rng(noc) # Generate random number in cell
    cell2 = [0]*len(cell) # Create an empty cell to store string data
    cell2 = cell_transform(cell)
    print('The original cell is')
    print(cell2) 
    nog = int(nog)
    i = 1
    while i < nog:
        cell =  generation_calculating(cell)
        cell2 = cell_transform(cell)
        print('The {}th generation is: '.format(i+1))
        print(cell2)
        i = i+1

# Random number generator
def rng(n):
    n = int(n)
    cell  = [0] * n
    cell2 = [0] * n
    for x in range(len(cell)):
        if (x == 0) | (x == n-1):
            cell2[x] = 0
        else:
            cell2[x] = random.randint(0,1)
    return cell2

# Cell Transformation
def cell_transform(cell):
    cell2 = [0] * len(cell)
    for i in range(len(cell)):
        if cell[i] == 0:
            cell2[i] = '.'
        else:
            cell2[i] = '*'
    return cell2

# Generation calculating
def generation_calculating(cell):
    length = len(cell) 
    cell2 = [0] * length # Create an empty list to store values
    for i in range(len(cell)):
        if (i == 0) | (i == len(cell)-1):
            cell2[i] = 0
            continue
        else:
            if (cell[i] == 0) & (cell[i-1] ^ cell[i+1]):
                cell2[i] = 1
            else:
                cell2[i] = 0
    return cell2

noc = input('Please input the number of cells: ') # noc = number of cells
nog = input('Please input the number of generations: ') # nog = number of generations
cell(noc, nog)

#### Question: Does the function order matters???
