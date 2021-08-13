
def left_bisect(sorted_list, element):
    """Find an element in a list (from left side)
    """
    idxLeft = 0
    idxRight = len(sorted_list) - 1
    while idxLeft < idxRight:
        # the middle is like taking the average of the left and right
        # since we create an integer / truncate, this is a left bisection
        idxMiddle = (idxLeft + idxRight) // 2
        middle = sorted_list[idxMiddle]
        # each time we take a step, get rid of half the range we have left
        if middle < element:
            idxLeft = idxMiddle + 1
        elif middle >= element:
            idxRight = idxMiddle
    return idxLeft
    
def right_bisect(sorted_list, element):
    """
    Find an element in a list (from the right)
    """
    idxLeft = 0
    idxRight = len(sorted_list) - 1
    while idxLeft < idxRight:
        idxMiddle = (idxLeft + idxRight) // 2
        middle = sorted_list[idxMiddle]
        if middle <= element:
            idxLeft = idxMiddle
        elif middle > element:
            idxRight = idxMiddle - 1
    return idxRight
