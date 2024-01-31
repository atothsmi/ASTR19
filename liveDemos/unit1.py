import sys  
import numpy as np 

def main():
    x = 0.0
    for i in range(20):
        x = (i*2) + 19.0
        print(f"The value of x is = {x}")

    # could also be here
    # print(f"The value of x is = {x}")
if __name__ == "__main__":
    main()