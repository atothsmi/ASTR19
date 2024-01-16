import numpy as np
import sys

def expo(x):
    return np.exp(x) #return the e^x function from numpy library

# subroutine -> does not return a value after performing task
def show_expo(start=0, end=9):
    x = np.arange(start, end, dtype = int)
    for i in x:
        print(i, expo(float(i)))

def main():
    # show_expo(-5, 5)
    # show_expo()
    
    if(len(sys.argv) > 1):

        user_end = int(sys.argv[1])

        show_expo(end=user_end)

if __name__  == '__main__':
    main()