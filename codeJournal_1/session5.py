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

def tableWriter(x, y, fname, xName='', yName=''):
    data = Table([x, y], names=[xName, yName])

    ascii.write(data, fname, format='commented_header', overwrite =True)
    #Read the data in from the file
    
def main():
    x = np.linspace(0, 2*m.pi, 1000)
    y = np.sin(x)
    fname = "codeJournal_1\\outputs\\session5Table.txt"

    tableWriter(y, x, fname, 'sin(x)', 'x')
    data_in = ascii.read(fname)
    #Display data from file in terminal
    print(data_in)

if __name__ == "__main__":
    main()