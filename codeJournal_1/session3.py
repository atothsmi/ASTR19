"""
Session Prompt: 
Write a Python program that defines a function f(x) 
that returns x**3 + 8. In the main function of the program, 
call f(x) with x = 9 and print the result.  
Use an if statement that executes if the result is larger 
than 27 and prints “YAY!”.
"""
#Definition of function f(x)
def f(x):
    return (x**3) + 8

def main():
    #Sets value of x
    x = 9
    #Stores result f(x)
    result = f(x)

    #Prints result of f(x) nicely
    print(f"The result of f(x) is {result}.")

    #If the result of f(x) is greater than 27, print "YAY!"
    if result > 27:
        print("YAY!")

if __name__=="__main__":
    main()