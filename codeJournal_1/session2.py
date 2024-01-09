import random
int_list = [1, 4, 6]
float_list = [2.0, 2.3, 8.9]
operation_list = ['sum', 'difference', 'product']
result = 0

#Gets and stores 2 random floats and 2 random integers from their respective lists
float1 = float_list[random.randint(0,2)]
float2 = float_list[random.randint(0,2)]
int1 = int_list[random.randint(0,2)]
int2 = int_list[random.randint(0,2)]


for i in operation_list:
    if i=='sum':
        result = float1 + float2
        print(f'The sum of {float1} and {float2} is {result}.')
    elif i == 'difference':
        result = int1 - int2
        print(f'The difference between {int1} and {int2} is {result}.')
    elif i == 'product':
        result = round(float1 * int1, 1)
        print(f'The product of {float1} and {int1} is {result}')
    else:
        #Error message
        print("Uh oh something has gone wrong")
    print(f'The data type of {result} is {type(result)}.')