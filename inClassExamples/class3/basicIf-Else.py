def flow_control(k, a=0, b=10):
    # %d indicates a placeholder to specify integer values
    # %s indicates a placeholder to specify string values
    # multiple % placeholders can be used by specifying a tuple
    # containing the requested values after the ending %

    # useful instead of f or .format
    if(k==a):
        s = "Variable k = %d equals %d." % (k, a)
    elif(k > a and k < b):
        s = "Variable k = %d is between %d and %d" % (k, a, b)
    else:
        s = "Variable k = %d is greater than or equal to %d" % (k, b)
    
    return s

def main():
    print(flow_control(0))

if __name__=="__main__":
    main()