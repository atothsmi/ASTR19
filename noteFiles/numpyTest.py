"""
A file for testing the NumPy Library
"""

#import statement

import numpy as np 

#Defining a numpy array
#A mathmatical array is a list of numbers
#numpy arrays can perform element-wise
#operations
"""
a = np.array([1, 2, 3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a/b)
print(a**b)
"""
#numpy arrays can be sliced like strings
#They are numbered like strings too
"""
print(a[1])
"""
#Handout 2

#1.1 Getting a range of values using numpy
    #use numpy.arange(x) where x is the number of values
    #in the single dimension array
    #starting with 0
"""
x = np.arange(10)
print(x)

#Size is the total number of elements in the array
print(x.size)

#Shape is the "height" and "width" of the array
#It returns a tuple
print(x.shape)

#ndim is the "height" of the list 
#or number of lists in the lists
print(x.ndim)

# .reshape(x, y) where x is the number of lists and 
# y is the number of elements in each list.
# it will produce an error if the x * y does not
# equal the total number of elements in the list (x.size)
x = x.reshape(2, 5)
print(x)

# Arrays can only have one data type
# The type can be specified using the dtype argument

x = np.array([0.4, 1.5, 2.3], dtype = np.int32)

#Because dtype was specified as int, floats -> int
print(x)
"""

#1.3 linspace

# np.linspace can create a range of evenly spaced, 
# floating point values

# np.linspace(x, y, z, endpoint=False) 
    # where x is the first value, 
    # y is the last value, and z is the total number 
    # of elements in the resulting array
    # endpoint declares if the y is included

"""
x = np.linspace(0, 1, 10)
print(x)

x = np.linspace(0, 1, 10, endpoint=False)
print(x)
"""

#1.4 Initializing arrays

# numpy can specify arrays filled with a desired value
# you can also specify type with dtype

# np.zeros(x) or np.zeros([y, z])
# np.ones(x) or np.ones([y, z])
# np.full(x, a) or np.full([y,z], a)

# x -> len of 1-dimension array
# y -> y-dimensions
# z -> elements per dimension
# a -> value to fill array with

#1.5 Array Operations

# Mathmatical and comparision operations are
# applied element-wise
"""
x = np.array([1, 3, 2, 5])
print(x<4)
"""

#1.6 Random numbers

# The np.random submodule can be used to make
# random numbers.
# Defaults to range [0, 1)
"""
x = np.random.random(10)
print(x)
"""

#1.7 Statistics

#numpy also has several statistical functions

# np.min(x) -> returns min value of array
# np.max(x) -> returns max value of array
# np.mean(x) -> returns mean of array
# np.median(x) -> returns median of array
# np.std(x) -> returns the standard deviation 
                #(average deviation from mean)
# np.sum(x) -> returns sum of array values
# np.prod(x) -> returns product of array values
# np.array(x) -> returns a new copy of array x
# x.copy() -> returns a new copy of array x

# where x is an numpy array


#1.9 Element-wise vs matrix multiplication

# Perform matrix dot product multiplication using
# np.dot(x, y) -> z

# Ex: 
# x = [[1, 2], 
#       [3, 4]]
# y = [[1, 2], 
#       [3, 4]]

# x*y = [[1*1 + 2*3, 3*1 + 4*3],
#       [1*2 + 2*4, 3*2 + 3*3]]
# Note: Above might be wrong

# Perform matric cross product using
# np.cross(x, y) -> z

# Ex:
# x = [1, 0 , 0]
# y = [0, 1, 0]

# i j k
# 1 0 0
# 0 1 0

#   minus   plus
# 0 0   1 0     1 0
# 1 0   0 0     0 1

# (0*0 + 1*0) - (1*0 + 0*0) + (1*1 + 0*0)
# [0, 0, 1]

#Linear algebra operations can also be done in numpy



#Handout 3

#2.3 Numpy loadtxt and gentxt

# loadtxt() gives the contents of the file
# ignoring lines starting with #
# and puts it into a numpy n-dimensional array
# with the same number of rows and columns as the file

"""
#defines filename
fname = 'noteFiles\\outputs\\numpy_data.txt'
#opens the file with numpy loadtxt
test_data = np.loadtxt(fname)

#prints information about data now
print(test_data)
print(test_data.shape)
print(type(test_data))
"""

#use np.genfromtxt(fname) because it can provide
#handling for many different formats and special characters

#Quickly write arrays to a file using
#savetxt(x, y, fmt='FORMATTING INSTUCTIONS SEPERATED BY %')
"""
x = np.linspace(0,1,10) # 0 to 1 in 10 steps
y = x**2 #an example function
np.savetxt('outputs\\test.txt', np.transpose((x,y)),fmt='%4.3f')
"""