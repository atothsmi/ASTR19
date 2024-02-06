import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import axes3d ##D axes with matplotlib

#generate x and y corrdinates
x = np.linspace(0, 1*np.pi, 200)
y = np.linspace(0, 2*np.pi, 200)

#create all combinations of x,y on a grid
x, y = np.meshgrid(x,y)

#create some z data z = -sin(x)*sin(y)
z = -np.sin(x)*np.sin(y)

#create figure
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d') #create a single subplot

#create a 3D wire frame of the z surface
ax.plot_wireframe(x, y, z, rstride = 10, cstride=10, linewidth=0.5, color='0.25')
ax.view_init(20) #rotate viewing angle by 20 deg

#rstride = steps for rows
#cstride = steps for columns

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

from matplotlib import cm #import color maps

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

#create a surface plot
surf = ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap = cm.coolwarm, alpha = 0.7)

#add colorbar
fig.colorbar(surf, shrink=0.5, label='Z Label')

#add wireframe
ax.plot_wireframe(x, y, z, rstride = 10, cstride=10, linewidth=0.5, color='0.25')

#add projection of z (data) projected onto the (x,y) plane
cset = ax.contourf(x, y, z, zdir='z', cmap=cm.coolwarm, offset =-1)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')

plt.show()

plt.show()

