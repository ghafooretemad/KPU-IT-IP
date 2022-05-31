import math

def mbMosaFormula(a, b, c, operator):
    fistPart =  (-1*b if operator == '-' else b )- math.sqrt(b*b - 4*a*c)
    secondPart = 2*a
    return fistPart/secondPart


# a,b,c = eval(input("Please Enter values for a, b,c :"))

# firstRoot = mbMosaFormula(a, b, c, '-')
# secondRoot = mbMosaFormula(a, b, c, '+')

# print(f'First Root {firstRoot} Second Root {secondRoot}')



myList = []
for i in range(10):
    myList.append(20)
    
print(myList)