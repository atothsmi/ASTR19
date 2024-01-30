###################
# import libraries
###################
import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib
from matplotlib import cm #get access to color maps
###################
# define a nice plot
###################
def image_plot(x,
    flag_save=True, #save the figure?
    xlabel='x', #x-axis label
    ylabel='y', #y-axis label

    dcmap='magma', #default color map
    fs=12, #font size
    fname='image_plot.png'): #default plot filename
    #by default, flag_save = True, and we'll save the figure #to a file.
    #The plot filename fname = 'plot.png' by #default, but we can
    #change this
    
    #define a figure and axis
    f, ax = plt.subplots(1,1,figsize=(4,4))
    #plot y vs. x
    si = ax.imshow(x,cmap=dcmap,origin='lower')
    #label our axes
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel(ylabel,fontsize=fs)
    #get a colorbar
    cbar = f.colorbar(si)
    cbar.ax.set_ylabel('z',fontsize=fs)
    #save the plot?
    if(flag_save):
        plt.savefig(fname,bbox_inches='tight',dpi=400)
###################
# define main
###################
def main():
    # yay!
    print('Making a plot!')
    #make a dummy x variable
    x = np.linspace(0, np.pi, 400)
    y = np.linspace(0, 2*np.pi, 400)
    x,y = np.meshgrid(x,y)
    #make a function of x and y
    z = 3*np.cos(x)*np.sin(y)
    #make the plot
    image_plot(z)
###################
# execute main()
###################
if __name__=='__main__':
    main()