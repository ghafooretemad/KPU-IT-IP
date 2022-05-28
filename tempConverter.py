fahr = eval(input("Please enter the Fahr value:"))

def tempCalc(fahr):
    celc = 5/9*fahr-32
    return celc

result = tempCalc(fahr)
print(f"result is: {result}")