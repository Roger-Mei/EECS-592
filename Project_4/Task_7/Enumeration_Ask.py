from Enumerate_All import *

def Normalize(Distribution):
    """
    This function is designed to normalize the distribution of the query variable.
    Distribution is a dictionary.
    """
    sum = 0
    for key in Distribution.keys():
        sum += Distribution[key]
    for key in Distribution.keys():
        Distribution[key] = Distribution[key]/sum
    return Distribution

def Enumeration_Ask(X, e, bn, prob_dict):
    """
    X is the query variable
    e is the observed evidence
    bn is the Bayes' Network with hidden variables
    """

    # Create a dictionary whose key is the variable's value and whose 
    # value is the corresponding probability
    Q_x = {} 
    # This step is intended to change the query variable from a string to a node
    for key in bn.node_dict.keys():
        if X == key:
            X = bn.node_dict[key]
    for x in X.value:
        # e_x_i is e extented with X = x
        X.specific_value = x
        temp_str = str(X.name) + '=' + str(x)
        e_x_i = e.copy()
        e_x_i.append(temp_str)
        # Sort the list to formalize 
        e_x_i = sorted(e_x_i)
        Var_cp_version = copy.deepcopy(bn.Var)
        Q_x[x] = Enumerate_All(Var_cp_version, e_x_i, prob_dict)

    # Normalization
    Normalize(Q_x)

    # Print result
    for key in Q_x.keys():
        round_number = round(Q_x[key], 4)
        print('P(' + str(X.name) + '=' + str(key) + '|' + str(e) + ')=' + str(round_number))