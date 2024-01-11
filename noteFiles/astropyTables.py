import numpy as np
from astropy.table import Table  #imports Table class
from astropy.io import ascii #ascii plan text io (input/output)
from astropy.io import fits #FITS format


#create some data arrays
x = np.linspace(0, 1, 10)
y = 0.5*x**3 

#create a table
data = Table([x, y], names=['x', 'y'])
"""
#write the table to file
ascii.write(data, "noteFiles\\outputs\\table.txt", format='commented_header')
#Read the data in from the file
data_in = ascii.read("noteFiles\\outputs\\table.txt")

#Display data from file in terminal
print(data_in)
"""

"""
#create a binary fits table from a ascii fits table
data.write('noteFiles\\outputs\\table1.fits', format='fits')
"""

hdu_fits = fits.open("noteFiles\\outputs\\table1.fits")
hdu_fits.info()
hdu_fits.close()