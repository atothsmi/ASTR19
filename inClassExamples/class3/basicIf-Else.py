def flow_control(k, a=0, b=10):
    # %d indicates a placeholder to specify integer values
    # %s indicates a placeholder to specify string values
    # multiple % placeholders can be used by specifying a tuple
    # containing the requested values after the ending %

    # useful instead of f or .format
    # because it saves a format that can substitute any variable values for 
    # the % characters, instead of a nammed variable
    if(k==a):
        s = "Variable k = %d equals %d." % (k, a)
    elif(k > a and k < b):
        s = "Variable k = %d is between %d and %d" % (k, a, b)
    else:
        s = "Variable k = %d is greater than or equal to %d" % (k, b)
    
    return s

def main():
    print(flow_control(0))
    #{i:12d} print i with 12 spaces
    #{i:012d} print i with 12 spaces, 0's added to the front
    #{i:9.8e}

    #reminder: e is equivalent to *10^
    x = 123423414.2
    print(f'{x:9.8e}')

if __name__=="__main__":
    main()