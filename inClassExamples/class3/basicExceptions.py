import sys

try:
    a = sys.argv[1]
    print(a)

except:
    print("a is not defined")

try:
    a = sys.argv[1]
    print(a)
except NameError:
    print("a is not defined")
except:
    print("Something else went wrong")