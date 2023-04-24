def sum(arg):
    '''
    Adds sequences of number together
    '''
    total = 0 # declare the total value

    # loop over all the values contained in arg and add them to the total
    for val in arg:
        total += val
    return total # return the total value