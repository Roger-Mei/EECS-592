def PARSE(line):
    """
    This function aims to parse the line to sort out attribute and its corresponding value.
    The output should be a list whose first item is the attribute and the left ones are its 
    corresponding values.
    """
    # Create output list
    out_list = []
    # We first need to sort out the attribute of each line
    for i in range(len(line)):
        if i == 0:
            temp_item = line[i]
            idx = 0
            for temp_idx in range(len(temp_item)):
                if temp_item[temp_idx] == ':':
                    idx = temp_idx
            attribute = str(temp_item[:idx])
            out_list.append(attribute)
            value = str(temp_item[idx+1:])
            out_list.append(value.strip())
        else:
            out_list.append(line[i].strip())
    return(out_list)
