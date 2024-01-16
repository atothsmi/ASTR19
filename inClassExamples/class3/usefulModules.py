import numpy as np      # imports the numpy library

import sys              # accesses C-like sys library
import os               # accesses the operating system

print(sys.argv)         #prints any command line argument
                        #including program name
print(os.getcwd())      #prints the current working directory
                        #equivalent to pwd in terminal
print(os.system('date'))    #
print(os.system('ls'))     