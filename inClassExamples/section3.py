def reverseSTR(string):
    return string[::-1]

print(reverseSTR("people"))

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))

def greeting(name, message="How was your day?"):
    print(f"Hello, {name}!")
    print(message)

greeting("Wormica")