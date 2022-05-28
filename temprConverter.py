
def converter(celc):
    result = (9/5)*celc + 32
    return result

celcDeg = eval(input("Please enter the Celc: "))
result = converter(celcDeg)

print(f"Calculated Frh {result}")

for i in range(20):
    print(i)