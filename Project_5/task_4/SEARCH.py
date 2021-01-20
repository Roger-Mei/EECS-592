from IMPORTANCE import IDX_CHECK
def SEARCH(examples, A, value):
    """
    This function will return a list which contains the example with specific attribute's value.
    """
    idx = IDX_CHECK(A)
    exs_list = []
    for item in examples:
        if item[idx] == value:
            exs_list.append(item)
    return exs_list