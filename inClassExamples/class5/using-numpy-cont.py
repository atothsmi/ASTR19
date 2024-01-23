import numpy as np 

x = 2.0     #define a float
y = 0.5     #define a float

#exponents and logarithms
print(f"np.exp({x}) = {np.exp(x)}")     #exp(x)
print(f"np.log({x}) = {np.log(x)}")     #log(x) (natural log)
print(f"np.log10({x}) = {np.log10(x)}") #log10(x)=log(x)/log(10)
print(f"np.log2({x}) = {np.log2(x)}")   #log2(x)=log(x)/log(2)

#min/max/misc functions
x = -1.0
print(f"np.fabs({x}) = {np.fabs(x)}")     #fabs(x)
print(f"np.fmin({x}, {y}) = {np.fmin(x, y)}")     #min of x and y
print(f"np.fmax({x}, {y}) = {np.fmax(x, y)}")     #max of x and y