numberSubject = int(input("Please Enter number of subject"))

def getSubjects():
    subjectList = []
    for i in range(numberSubject):
        subjectList.append(input('Please Enter Subject Name:'))
    return subjectList

def getCredits():
    creditList = []
    for i in range(numberSubject):
        creditList.append(int(input('Please Enter Credit')))
    return creditList
def getMarks():
    marksList = []
    for i in range(numberSubject):
        marksList.append(float(input('Please Enter Marks')))
    return marksList
def main():
    subjectList = getSubjects()
    creditList = getCredits()
    marksList = getMarks()
    
    for index, item in enumerate(subjectList):
        print(f' Subject Name: {item} Credit: {creditList[index]} ')
if __name__ == '__main__':
    main()
    