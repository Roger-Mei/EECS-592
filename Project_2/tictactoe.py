"""
This code plays the tictactoe game. Please view the output from command line.
To run this code. Please input :
python3 tictactoe.py seed_number
in your command line.
"""

import random
import math
import sys
import numpy as np



# Seed setting

s = int(sys.argv[1])
print('Seed = ', s)
random.seed(s)


# Define terminal test. True when game is over, False otherwise.

def terminal_test(state):
    # Check horizontals 
    if state[0][0] == state[0][1] and state[0][1] == state[0][2] and state[0][0] != '-':
        return True
    if state[1][0] == state[1][1] and state[1][1] == state[1][2] and state[1][0] != '-':
        return True
    if state[2][0] == state[2][1] and state[2][1] == state[2][2] and state[2][0] != '-':
        return True
    # Check verticals:
    if state[0][0] == state[1][0] and state[1][0] == state[2][0] and state[0][0] != '-':
        return True
    if state[0][1] == state[1][1] and state[1][1] == state[2][1] and state[0][1] != '-':
        return True
    if state[0][2] == state[1][2] and state[1][2] == state[2][2] and state[0][2] != '-':
        return True
    # Check diagnals:
    if state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[0][0] != '-':
        return True
    if state[0][2] == state[1][1] and state[1][1] == state[2][0] and state[0][2] != '-':
        return True
    # Check draws:
    temp_sum = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] != '-':
                temp_sum += 1
    if temp_sum == 9:
        return True
    return False


# Define Action function. Action function returns the set of legal moves in a state.

def Actions(state):
    legal_moves_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == '-':
                legal_moves_list.append([i, j])
    # print(legal_moves_list)
    return legal_moves_list


# Define Result function. This returns the result of a move. Note that action should be a 1x2 list which 
# record the players target coordinate.

def Result(state, action, player):
    state[action[0]][action[1]] = player
    return state


# Define a utility function. This function takes in a state, and returns the final numeric value for a game that ends in 
# terminal state for a player

def utility(state):
    # Check horizontals 
    if state[0][0] == state[0][1] and state[0][1] == state[0][2] and state[0][0] != '-':
        if state[0][0] == 'o':
            return 1
        return -1
    if state[1][0] == state[1][1] and state[1][1] == state[1][2] and state[1][0] != '-':
        if state[1][0] == 'o':
            return 1
        return -1
    if state[2][0] == state[2][1] and state[2][1] == state[2][2] and state[2][0] != '-':
        if state[2][0] == 'o':
            return 1
        return -1
    # Check verticals:
    if state[0][0] == state[1][0] and state[1][0] == state[2][0] and state[0][0] != '-':
        if state[0][0] == 'o':
            return 1
        return -1
    if state[0][1] == state[1][1] and state[1][1] == state[2][1] and state[0][1] != '-':
        if state[0][1] == 'o':
            return 1
        return -1
    if state[0][2] == state[1][2] and state[1][2] == state[2][2] and state[0][2] != '-':
        if state[0][2] == 'o':
            return 1
        return -1
    # Check diagnals:
    if state[0][0] == state[1][1] and state[1][1] == state[2][2] and state[0][0] != '-':
        if state[0][0] == 'o':
            return 1
        return -1
    if state[0][2] == state[1][1] and state[1][1] == state[2][0] and state[0][2] != '-':
        if state[0][2] == 'o':
            return 1
        return -1
    # Check draws:
    return 0


# Define Successor function. This function will update the game state.

def successor(state, player):
    if terminal_test(state):
        return state
    if player == 'x':
        while True:
            # Generate random number
            random_num = random.randint(0, 8)
            row = math.floor(random_num/3)
            col = random_num - 3 * row
            # Justify whether the calculated position is available
            if state[row][col] == '-':
                break
        # Update the state
        state[row][col] = player
        return state

    if player == 'o':
        action = minmax(state)
        state = Result(state, action, player)
        return state


# Define the MinMax-Decision function. This function will return an action.

def minmax(state):
    action_list = Actions(state)
    value_list = [] # Create an empty list to store the possible utility value
    for i in range(len(action_list)):
        action = action_list[i]
        temp_state = state.copy()
        value_list.append(min_value(Result(temp_state, action, 'o')))
    indx = value_list.index(max(value_list))
    return action_list[indx] # Return the corresponding action


# Define MAX_VALUE function. This function will return a utility value

def max_value(state):
    if terminal_test(state):
        return utility(state)
    value = -math.inf
    for action in Actions(state):
        temp_state = state.copy()
        value = max(value, min_value(Result(temp_state, action, 'o')))
    return value


# Define MIN_VALUE function. This function will return a utility value

def min_value(state):
    if terminal_test(state):
        return utility(state)
    value = math.inf
    for action in Actions(state):
        temp_state = state.copy()
        value = min(value, max_value(Result(temp_state, action, 'x')))
    return value


# Construct the game

# Initialization
real_state = np.array([['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']])
PLAYER = 'x'
GAME_RECORDER = []
# Proceed the game
for k in range(1, 10):
    if terminal_test(real_state):
        break
    print(k)
    print(successor(real_state, PLAYER))
    # switch game player
    if PLAYER == 'x':
        PLAYER = 'o'
    else:
        PLAYER = 'x'
    GAME_RECORDER.append(real_state)

# Write the file into csv file
with open('tictactoe.txt', 'w') as outfile:
    for i in range(len(GAME_RECORDER)):
        real_state = GAME_RECORDER[i]
        for Row in range(np.shape(real_state)[0]):
            for Column in range(np.shape(real_state)[1]):
                if Column == 2 and Row == 2:
                    outfile.write(real_state[Row][Column] + '\n')
                    outfile.write('\n')
                elif Column == 2 and Row != 2:
                    outfile.write(real_state[Row][Column] + '\n')
                else:
                    outfile.write(real_state[Row][Column] + ',')
