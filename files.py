# f =open("test.csv")
# data = f.read()
# print(data)


# def writeFile():
#     fileObject = open(".csv", "x")
#     data = "\nSanjoy,35,34,56,78,80"
#     fileObject.write(data)


# def writeFile():
#     fileObject = open("test.csv" , "a")    
#     name = input( " Enter a student name : ")
#     age = input( " Enter the age of the student : ")
#     physics = int(input( " Enter the marks for the maths : "))
#     science = int(input( " Enter the marks for the maths : "))

##sanjoy sir's code
def createFile():
    fileObject = open("Student.csv", "x")
    data = "name,age,physics,chemistry,english"
    fileObject.write(data)

#################


def userInput():
    name = input("please enter the student name")
    age = input("please enter the age")
    physics = input("Please enter the marks for physics")
    chemistry = input("Please enter the marks for chemistry")
    english = input("Please enter the marks for english")
    data = name+","+age+","+chemistry+","+english
    return data

######


def writeFile(data):
    fileObject = open("Student.csv", "a")
    data = "\n"+data
    fileObject.write(data)


def readFile():
    fileObject = open("Student.csv", "r")
    data = fileObject.read()
    print(data)


def userData(username):
    fileobject = open("student.csv", 'r')
    for line in fileobject:
        stringArray = line.split(",")
        if (stringArray[0] == username):
            print(line)


# if the file do not exist then
# 
data = userInput()
writeFile(data)
# pip :
ReadFlag = input("Do you want to read the file")
if (ReadFlag == "y"):
    readFile()
    username = input("tell me the name of the user you want to know baout")
    userData(username)
data = userInput()
writeFile(data)
# pip :
ReadFlag = input("Do you want to read the file")
if (ReadFlag == "y"):
    readFile()
    username = input("tell me the name of the user you want to know about : ")
    userData(username)



# import os
# def createFile():
#     if not os.path.exists("student.csv"):
#         fileObject = open("student.csv",'w')
#         data = "Name\t Age\t Physics\t English\t Science"
#         fileObject.write(data)
#     else:
#         print("File already exist!")
# createFile()    