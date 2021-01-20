import copy

def Has_Value(Y, e):
    """
    This function will justify whether Y and its value is in the evidence or not.
    """
    # print(e)
    for element in e:
        # print(Y.name)
        if Y.name == element[0]:
            return True
    return False

def Retrieve(Y,e):
    """
    This function is designed for retrieve the value of Y in evidence.
    """
    for element in e:
        if Y.name == element[0]:
            # Set up variable's value (T or F)
            Y.specific_value = element[2]
            return element[2]

def Conditional_P(Y, y, condition, prob_dict):
    """
    This function returns the conditional probabiblity of a variable Y with value y.
    Within this function, we should construct the key whose form matches the ones in
    prob_dict.
    """
    # Probability without condition
    if y == 'F':
        return 1 - Conditional_P(Y, 'T', condition, prob_dict)
    else:
        if condition == None:
            key = 'P(' + str(Y.name) + '=' + str(y) + ')'
            return prob_dict[key]
        else:
            # print(condition)
            key = 'P(' + str(Y.name) + '=' + str(y)+ '|' 
            for i in range(len(condition)):
                # When dealing with the last condition
                if i == len(condition) - 1:
                    key = key + str(condition[i].name) + '=' + str(condition[i].specific_value) + ')'
                else:
                    key = key + str(condition[i].name) + '=' + str(condition[i].specific_value) + ','
            return prob_dict[key]
        
def Parent(Y):
    """
    This function returns the parent of a node.
    """
    if not Y.parent:
        return None
    else:
        return Y.parent

def Enumerate_All(Var, e, prob_dict):
    """
    This function is designed to do the Bayes' Net Enumeration.
    """
    if not Var:
        return 1.0
    
    # Construct Y. 
    # Note: Y is a node!
    Y = Var.pop(0)

    if Has_Value(Y,e):
        # Retrieve Y's value in e
        y = Retrieve(Y,e)
        t1 = Enumerate_All(Var, e, prob_dict)
        temp_prob = Conditional_P(Y, y, Parent(Y), prob_dict) * t1
        return temp_prob
    else:
        temp_sum = 0
        for y in Y.value:
            Y.specific_value = y
            e_y = e.copy()
            Var_cp = copy.deepcopy(Var)
            e_y.append(str(Y.name) + '=' + str(y))
            t = Enumerate_All(Var_cp, e_y, prob_dict)
            temp_sum += Conditional_P(Y, y, Parent(Y), prob_dict) * t
        return temp_sum