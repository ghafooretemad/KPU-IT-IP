subjectNo = int(input("Please enter number of subject"))

for i in range(subjectNo):
    department = input("Enter the department")
    subject = input("Enter the subject")
    credit = int(input("enter the cridit"))
    lecturer = input("ener the lecturer")
    
    stdName = input("student name")
    stdLName = input("Enter Last Name")
    score = int(input("Enter the score"))
    
    if(score >= 90):
        print(f' {stdName} {stdLName} is in the grade of A')
    elif(score >= 80 ):
        print(f' {stdName} {stdLName} is in the grade of B')
    else:
        print(f'{stdName} {stdLName}  is in the grade of F')
    