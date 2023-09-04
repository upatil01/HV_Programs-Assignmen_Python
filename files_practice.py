
def userinput():
    name = input( "Please enter the student name :")
    age = input( " Please enter the age : ")
    physics = input( " please enter the physics marks : ")
    english = input( " Please enter the english marks : ")
    maths = input( "Please enter the maths marks : ")
    data = name+"," +age+"," +physics+"," +english+"," +maths+","
    return data

def writefile(data):
    fileObject = open("student.csv" , "a")
    data = "\n" + data
    fileObject.write(data)

def readfile():







data = userInput()
writeFile(data)
# pip :
ReadFlag = input("Do you want to read the file")
if (ReadFlag == "y"):
    readFile()
    username = input("tell me the name of the user you want to know baout")
    userData(username)    