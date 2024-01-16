import sys

def hello_world():
    print("Hello World, this sentence came from  %s." % __file__)
    print("This function is being run from %s." % sys.argv[0].split("/")[-1])