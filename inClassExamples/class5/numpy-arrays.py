import numpy as np 

#creating arrays
#create a 1D array
arr_1d = np.array([1, 2, 3])
print(arr_1d, type(arr_1d))

#create an array with zeros
zeros_array = np.zeros(3, dtype=int)
print(zeros_array)

#create an array with ones
ones_array = np.ones(3)
print(ones_array)

# create an array with a range of values
#arange(start (inclusive), end (exclusive), step)
arange_array = np.arange(0 ,10, 2)
print(arange_array)

print()
#---------------------------------------------------------
#operation on arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

#element-wise addition
result_add = a+b
print(result_add)

#element-wise mult
result_mult = a*b
print(result_mult)

#dot product on 1D arrays
dot_product = np.dot(a, b)
print(dot_product)

#numpy functions can be applied to arrays element-wise
sin_a = np.sin(a)
print(a)
print(sin_a)
