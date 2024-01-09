'''
Program Prompt:
Write a Python program that prints the sum of two floating point numbers, 
the difference between two integers, and the product of a floating point 
number and an integer. In each case, have the program print out the data 
type of the resulting answer.

Extra Notes:
This program also picks random floats and integers in a range [1, 100]
to perform the calculations.
'''
#Gets random module
import random

def main():
    
    #Gets and stores 2 random floats (rounded to 2 decimals) and 2 random integers
    float1 = round(random.uniform(0, 100), 2)
    float2 = round(random.uniform(0, 100), 2)
    int1 = random.randint(0,100)
    int2 = random.randint(0,100)

    #Empty variable to store results of calculations later
    result = 0

    #Adds the 2 stored random floats
    result = float1 + float2
    print(f'The sum of {float1} and {float2} is {result}.')
    print(f'The data type of {result} is {type(result)}.')

    #Subtracts the 2 stored random ints
    result = int1 - int2
    print(f'The difference between {int1} and {int2} is {result}.')
    print(f'The data type of {result} is {type(result)}.')

    #Multiplies the 1st stored float and the 1st stored int
    result = round(float1 * int1, 2)
    print(f'The product of {float1} and {int1} is {result}')
    print(f'The data type of {result} is {type(result)}.')

if __name__=="__main__":
    main()
