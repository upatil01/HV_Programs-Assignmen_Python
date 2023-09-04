##addition of two numbers 
##take input from users

def addition(num1, num2):
    return num1 + num2
    

num1 = int(input( " Please enter the number : "))
num2 = int(input( " Please enter the number : "))

opeartor = input( " Please enter the opeartor : ")

if (opeartor == '+'):
    result = addition(num1, num2)

else:
    result = "error"   
print(result)

##calculate using power of the digit

def power(num1 , num2):
    return num1 ** num2

num1 = int(input(" please Enter the digit: "))
num2 = int(input(" please Enter the digit: "))

if( num1 > 0 and num2 > 0):
    result = power(num1 , num2) 

else:
    result ="error"
print(result)         

###create new file 
# def power(num1 , num2):
#     return num1 ** num2

# num1 = int(input(" please Enter the digit: "))
# num2 = int(input(" please Enter the digit: "))

# def createfile(result):
#     f = open("student3.csv" , "x")
#     result = num1 ** num2 
#     f.write(result)


# if( num1 > 0 and num2 > 0):
#     result= power(num1 , num2)
   

# else:
#     result = "error"
# createfile(result)    
# print(result)        

###write in a file
# def power(num1 , num2):
#     data = num1 ** num2
#     return data

# num1 = (input(" please Enter the digit: "))
# num2 = (input(" please Enter the digit: "))

# def writefile(data):
#     f = open("student3.csv" , "a")
#     data = num1 , num2 
#     f.write(data)

# writefile(data)  


def power(num1 , num2):
    return num1 ** num2

num1 = (input(" please Enter the digit: "))
num2 = (input(" please Enter the digit: "))

def createfile(result):
    f = open("student4.csv" , "x")
    result = num1 ** num2 
    f.write(result)

createfile(result)











# if (num1 > 0 and num2 > 0):
#     print( num1 + num2 )

# else:
#     result = "error"    
# print(result)