import math
def IDX_CHECK(attribute_name):
    """
    This function will return the index number of the attribute name in the example.
    """
    if attribute_name == 'Alt':
        return 0
    if attribute_name == 'Bar':
        return 1
    if attribute_name == 'Fri':
        return 2
    if attribute_name == 'Hun':
        return 3
    if attribute_name == 'Pat':
        return 4
    if attribute_name == 'Price':
        return 5
    if attribute_name == 'Rain':
        return 6
    if attribute_name == 'Res':
        return 7
    if attribute_name == 'Type':
        return 8
    if attribute_name == 'Est':
        return 9

def B(q):
    """
    This function will calculate the Boolean Entropy
    """
    # print('Value q')
    # print(q)
    if q > 0 and q != 0 and q != 1:
        result = -(q*math.log(q,2) + (1-q)*math.log(1-q,2))
    else:
        result = 0
    # print('Result of B')
    # print(result)
    return result

def REMAINDER(attribute_name, examples, attribues):
    """
    This function aims to calculate the remainder of the information
    """
    # print('attribute_name')
    # print(attribute_name)
    remainder = 0
    denominator = len(examples)
    idx = IDX_CHECK(attribute_name)
    for value in attribues[attribute_name]:
        p_k = 0
        n_k = 0
        for item in examples:
            if item[idx] == value:
                if item[-1] == 'Yes':
                    p_k += 1
                else:
                    n_k += 1
        if (p_k+n_k) != 0:
            remainder += (p_k+n_k)/denominator * B(p_k/(p_k+n_k))
    return remainder
        
def IMPORTANCE(attribute_name, examples, attribues):
    """
    This function will calculate the information gains of a certain attrubute
    """
    p = 0
    n = 0
    # First count the number of p and n 
    for item in examples:
        if item[-1] == 'Yes':
            p += 1
        else:
            n += 1
    Gain = B(p/(p+n)) - REMAINDER(attribute_name, examples, attribues)
    return Gain