def greethings(name):
    string = "Hello "+ name
    return string
# age = input("please enter the age: ")
# name = input("Please enter the name: ")
# print(greethings(name))

def calculator(number):
    # number = 5
    # [0,1,2,3,4]
    for i in range(number):
        print( i*i)

x,y = eval(input("Please enter the number: "))
print(f"value of X is: {x} and Value of Y is {y}")
calculator(x)
