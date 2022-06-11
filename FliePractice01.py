
fileName = open('info.txt', 'w')
print("Hello IT Students! \n wecome to file practice class", file=fileName)
fileName.close()

inFile = open('info.txt', 'r')
print(inFile.read())