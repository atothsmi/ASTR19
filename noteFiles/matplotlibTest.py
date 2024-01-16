#Example from matplotlib documentation 1/11/2024
#https://matplotlib.org/stable/users/getting_started/

#Import matplotlib and numpy as aliases
import matplotlib.pyplot as plt
import numpy as np

#Create some numpy arrays
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots() #Grid with single axes
print(fig) #Dimensions of the plot overall in (px X px)
print(ax) #Distance of axis from the edge of the overal figure 
#(left, bottom,dimensions relative to overall )
ax.plot(x, y)
plt.show()
