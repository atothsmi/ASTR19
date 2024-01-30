###################
# import libraries
###################
import numpy as np #import numpy
import matplotlib.pyplot as plt #import matplotlib
###################
# define a nice plot
###################
def histogram_plot(x,
    flag_save=True, #save the figure?
    xlabel='x', #x-axis label
    ylabel='y', #y-axis label
    lcolor='red', #line color
    fs=14, #font size
    fname='histogram_plot.png'): #default plot filename
    #by default, flag_save = True, and we'll save the figure
    #to a file. The plot filename fname = 'plot.png' by
    #default, but we can change this
    #define a figure and axis
    f, ax = plt.subplots(1,1,figsize=(4,4))
    #plot y vs. x
    ax.hist(x,facecolor=lcolor,bins=50,edgecolor='black',alpha=0.5)
    #label our axes
    ax.set_xlabel(xlabel,fontsize=fs)
    ax.set_ylabel(ylabel,fontsize=fs)
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
    x = np.random.normal(scale=1,size=1000)
    #make the plot
    histogram_plot(x)

###################
# execute main()
###################
if __name__=='__main__':
    main()