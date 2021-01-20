import csv
from VALUE_ITERATION import *
# Read the mdpinput.txt file
INPUT = open('mdpinput.txt', 'r')
READER1 = csv.reader(INPUT)

# Create empty list to store variable
States = []
Actions = []
T_1 = []
T_2 = []
Rewards = []
STATE_FLAG = 0
ACTION_FLAG = 0
T_1_FLAG = 0
T_2_FLAG = 0
REWARDS_FLAG = 0
DISCOUNT_FLAG = 0
TOLERANCE_FLAG = 0

# Parse the input
for rows in READER1:
    if rows[0][0] == '%' and rows[0][2:8] == 'States':
        STATE_FLAG = 1
        continue
    if STATE_FLAG == 1:
        for items in rows:
            States.append(items.strip())
        STATE_FLAG = 0
    if rows[0][0] == '%' and rows[0][2:9] == 'Actions':
        ACTION_FLAG = 1
        continue
    if ACTION_FLAG == 1:
        for items in rows:
            Actions.append(items.strip())
        ACTION_FLAG = 0
    if rows[0][0] == '%' and rows[0][2:10] == 'Action 1':
        T_1_FLAG = 1
        continue
    if T_1_FLAG == 1 and rows[0][0] != '%':
        temp_list = []
        for items in rows:
            temp_list.append(items.strip())
        T_1.append(temp_list)
    else:
        T_1_FLAG = 0
    if rows[0][0] == '%' and rows[0][2:10] == 'Action 2':
        T_2_FLAG = 1
        continue
    if T_2_FLAG == 1 and rows[0][0] != '%':
        temp_list = []
        for items in rows:
            temp_list.append(items.strip())
        T_2.append(temp_list)
    else:
        T_2_FLAG = 0
    if rows[0][0] == '%' and rows[0][2:9] == 'Rewards':
        REWARDS_FLAG = 1
        continue
    if REWARDS_FLAG == 1 and rows[0][0] != '%':
        temp_list = []
        for items in rows:
            temp_list.append(items.strip())
        Rewards.append(temp_list)
    else:
        REWARDS_FLAG = 0
    if rows[0][0] == '%' and rows[0][2:10] == 'Discount':
        DISCOUNT_FLAG = 1
        continue
    if rows[0][0] != '%' and DISCOUNT_FLAG == 1:
        gamma = float(rows[0])
    else:
        DISCOUNT_FLAG = 0
    if rows[0][0] == '%' and rows[0][2:9] == 'Epsilon':
        TOLERANCE_FLAG = 1
        continue
    if rows[0][0] != '%' and TOLERANCE_FLAG == 1:
        epsilon = float(rows[0])
    else:
        TOLERANCE_FLAG = 0
    
# Construct mdp model
class MDP:
    def __init__(self):
        self.states = []
        self.actions = []
        self.transition_model = {}
        self.rewards = []
        self.discount = None

mdp = MDP()
mdp.states = States.copy()
mdp.actions = Actions.copy()
mdp.transition_model['a0'] = T_1.copy()
mdp.transition_model['a1'] = T_2.copy()
mdp.rewards = Rewards.copy()
mdp.discount = gamma

# Run the main function
optimal_action_list, U_p = VALUE_ITERATION(mdp, epsilon)

# Write the output into the csv file
with open('policy.txt', 'w') as outfile:
    for i in range (0,3):
        outfile.write(str(States[i])+': '+str(optimal_action_list[0])+' '+'('+str(U_p[i])+')'+'\n')


