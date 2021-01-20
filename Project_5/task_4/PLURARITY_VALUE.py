def PLURARITY_VALUE(examples):
    P_number = 0
    N_number = 0
    for item in examples:
        if item[-1] == 'Yes':
            P_number += 1
        else:
            N_number += 1
    if P_number >= N_number:
        return 'Yes'
    else:
        return 'No'