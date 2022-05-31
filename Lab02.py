myItems = [1, "Ahmad", 6, 3]
myItems[2] = "Karimi"
myNewItems = (3,5,6, "Ahmd")
print('myNewItems data Type:', type(myNewItems))
for i in myNewItems:
    print("New Item: ", i)
        
for index, item in enumerate(myItems):
    print("Item: ", item)
    print("Index", index)
    
print(type(myItems))

studentList =  []
listSize = int(input("Enter number of student"))
