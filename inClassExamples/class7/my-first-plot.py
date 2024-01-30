import numpy as np
import matplotlib.pyplot as plt

def main():
    #define an integer
    n = 100

    #create array x from 0 to 2*pi, with n points
    x = np.linspace(0, 2.0*np.pi, n)

    #y = sin(x)
    y = np.sin(x)

    #plot x (horizontal) versus y (vertical)
    #generates figure in background
    plt.plot(x, y)

    #add labels to axes
    plt.xlabel("x")
    plt.ylabel("sin(x)")

    #show plot visually to your human eyes
    plt.show()

#run if running this script directly
if __name__=="__main__":
    main()