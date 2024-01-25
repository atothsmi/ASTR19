"""
Session Prompt:
Write a Python program that writes out a table of the function sin(x) vs. x, 
where x is tabulated between 0 and 2pi with a thousand entries. 
Follow the basic Python program structure, including a main program function.
"""
import numpy as np
from astropy.table import Table  #imports Table class
   
def main():
    x = np.linspace(0, 2*np.pi, 1000)
    y = np.sin(x)

    #Create a table using the np arrays
    data = Table([x, y], names=["sin(x)", "x"])

    #Display table in terminal
    print(data)

if __name__ == "__main__":
    main()