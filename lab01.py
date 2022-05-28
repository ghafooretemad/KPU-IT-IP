def greetings(name):
    message = "hello "+ name + " how are you doing"
    return message
    
name = input("Please enter the name: ")
print(greetings(name))