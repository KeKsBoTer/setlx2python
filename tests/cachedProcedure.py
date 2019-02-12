p_values = {}
def p(x,y):
    if (x,y) in p_values:
        return p_values[(x,y)]
        
    print("computed")

    return_value = x+y
    p_values[(x,y)] = return_value
    return return_value