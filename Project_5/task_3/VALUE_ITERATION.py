import math
import numpy as np
from OPTIMIZE import *
def VALUE_ITERATION(obj, tolerance):
    """
    Input obj should be the mdp model 
    Input tolerance should be the epsilon
    Local variables: U, U_p and delta
    """
    # Initialize local variables
    U = np.array([0.0,0.0,0.0])
    U_p = np.array([0.0,0.0,0.0])
    delta = math.inf
    # Calculate the threshold
    threshold = tolerance*(1-obj.discount)/obj.discount
    while delta >= threshold:
        U = U_p.copy()
        delta = 0
        for state in obj.states:
            if state == 'S0':
                action1, U_p[0] =  OPTIMIZE(obj,state,U)
            if state == 'S1':
                action2, U_p[1] = OPTIMIZE(obj,state,U)
            if state == 'S2':
                action3, U_p[2] = OPTIMIZE(obj,state,U)
        error = np.linalg.norm(U_p - U)
        if error > delta:
            delta = error
    optimal_action_list = [action1, action2, action3]
    return optimal_action_list,U_p
        