# employee.txt - 

# Name Department Salary
# Rahul  IT Domain  20000

#Task 1 - Read the data from the file and display it in the terminal
# Task 2 - You have to check whether the file exists or not then only display the data from the file to the terminal 
# Task 3 - Take the inputs from the user, save those inputs in the file and then display those inputs in the terminal


def readfile():
    fileobject = open("employee.txt" , "r")
    data = fileobject.read()
    print(data)

readfile()    

# import os

# if os.path.exists("employee.txt"):
#     fileobject = open("employee.txt" , "w ")
#     data =("Name+"", ""+Department+"","" +Salary")
#     fileobject.write(data)

# else:
#     print("File already Exists")           
       
    
# def writefile():
#     fileobject = open("employee.txt" , "a")
#     name = input("Please enter the name : ")
#     department = input("Please enter the department : ")
#     salary = input("Please enter the department : ")
#     data = "\n" + (name+ "," +department+ "," +salary)
#     fileobject.write(data)
#     print(data)
# writefile()    
detail = []

def writefile():
    details = {}
    fileobject = open("employee.txt" , "a")
    details["name"] = input("Please enter the name : ")
    details["department"] = input("Please enter the department : ")
    details["salary"]= input("Please enter the department : ")
    # data = "\n" + (name+ "," +department+ "," +salary)
    # fileobject.write(data)
    # print(data)
    detail.append(details)
print(detail)    
writefile()   

