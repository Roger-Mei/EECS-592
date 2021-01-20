def HAVE_SAME_CLASSIFICATION(examples):
    """
    This function aimes to judge whether all the examples have the same classification
    """
    class_list = []
    # Sort the classifications of different examples into a list
    for items in examples:
        class_list.append(items[-1])
    return all(x == class_list[0] for x in class_list)

def CLASSIFICATION(examples):
    """
    This function will return the classification of the examples. The premise of this function is that
    the examples have the same classification value.
    """
    return examples[0][-1]
