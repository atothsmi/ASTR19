"""
Session Prompt:
Write a Python program that writes out a table of the function sin(x) vs. x, 
where x is tabulated between 0 and 2 with a thousand entries. 
Follow the basic Python program structure, including a main program function.
"""
import numpy as np
import math as m
from astropy.table import Table  #imports Table class
from astropy.io import ascii #ascii plan text io (input/output)
from astropy.io import fits #FITS format

def main():
    x = np.linspace(0, 2*m.pi, 1000)
    y = np.sin(x)

    data = Table([y, x], names=['sin(x)', 'x'])

    ascii.write(data, "codeJournal_1\\outputs\\session5Table.txt", format='commented_header', overwrite =True)
    #Read the data in from the file
    data_in = ascii.read("codeJournal_1\\outputs\\session5Table.txt")

    #Display data from file in terminal
    print(data_in)
    pass

if __name__ == "__main__":
    main()