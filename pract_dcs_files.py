import os

def createFile():
    if not os.path.exists("Calculations.csv"):
        fileObject = open("Calculations.csv",'w')
        data = "FirstNum\t SecondNum\t Addition \t Power"
        fileObject.write(data)
        fileObject.close()
    else:
        print("File already Exist !")

def addition(num1,num2):
    Addresult = num1 + num2
    print("Addition of", num1 , " and " , num2 , " is:", Addresult) 
    return Addresult

def power(num1,num2):
    Powresult  = num1 ** num2
    print("Power of" , num1 , " to the " , num2 , " is:", Powresult) 
    return Powresult

def userInput():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num1 > 0 and num2 > 0:
        add_result = addition(num1,num2)
        pow_result = power(num1,num2)
        return num1,num2,add_result, pow_result
    else:
        print("Please enter only postive numbers greater than zero.")
        return None


def writeFile(num1,num2,add_result,pow_result):
    fileObject = open("Calculations.csv",'a')
    data = "\n" + str(num1) + "\t\t\t" + str(num2) + "\t\t\t" + str(add_result) + "\t\t\t" + str(pow_result)
    fileObject.write(data)
    fileObject.close()

createFile()
user_input = userInput()

if user_input:
    num1,num2,add_result,pow_result = user_input
    writeFile(num1,num2,add_result,pow_result)

