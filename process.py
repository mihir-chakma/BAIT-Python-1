def find_highest(a, b, c):
    if a > b and a > c:
        highest = a 
    elif b > c:
        highest = b
    else:
        highest = c 
    return highest

def find_lowest(a, b, c):
    if a < b and a < c:
        lowest = a 
    elif b < c:
        lowest = b
    else:
        lowest = c 
    return lowest
