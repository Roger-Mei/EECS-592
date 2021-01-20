def Rewards(obj, state, action):
    """
    This function helps define the rewards of the state after taking the specific action
    """
    for List in obj.rewards:
        if List[0] == state and List[1] == action:
            return float(List[2])

def OPTIMIZE(obj,state,U):
    """
    This function aimes to find the max utility value of a certain state until it converges.
    """
    result = 0
    cmp_list = {}
    # Decide which row of the trasition matrix to use 
    idx = int(state[1])
    for action in obj.actions:
        T = obj.transition_model[action]
        sum_U = 0
        for i in range(0,3):
            sum_U += float(T[idx][i]) * U[i]
        result = Rewards(obj, state, action) + obj.discount * sum_U
        cmp_list[action] = result
    max_action = max(cmp_list, key=cmp_list.get)
    return max_action, cmp_list[max_action]
        