import numpy as np 

x = 1.0     #define a float
y = 0.5     #define a float

#trig (nat in radians)
print(f"np.sin({x}) = {np.sin(x)}")     #sin(x)
print(f"np.cos({x}) = {np.cos(x)}")     #cos(x)
print(f"np.tan({x}) = {np.tan(x)}")     #tan(x)
print(f"np.arcsin({x}) = {np.arcsin(x)}")     #arcsin(x)
print(f"np.arccos({x}) = {np.arccos(x)}")     #arccos(x)
print(f"np.arctan({x}) = {np.arctan(x)}")     #arctan(x)
print(f"np.arctan2({x}, {y}) = {np.arctan2(x, y)}")     #arctan(x/y)
print(f"np.rad2deg({x}) = {np.rad2deg(x)}")   #convert radians to degrees

print()

#constant
print("Constants:")
print(f"np.pi({x}) = {np.pi}")     #pi

print()

#hyperbolic functions
print("Hyperbolic Functions:")
print(f"np.sinh({x}) = {np.sinh(x)}")     #sinh(x)
print(f"np.cosh({x}) = {np.cosh(x)}")     #cosh(x)
print(f"np.tanh({x}) = {np.tanh(x)}")     #tanh(x)
print(f"np.arcsinh({x}) = {np.arcsinh(x)}")     #arcsinh(x)
print(f"np.arccosh({x}) = {np.arccosh(x)}")     #arccosh(x)
print(f"np.arctanh({y}) = {np.arctanh(y)}")     #arctanh(x)