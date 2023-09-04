###calculator

num1 = int(input(" Please enter the number 1 : "))
num2 = int(input( "Please enter the number 2: "))
operator = input(" Enter the operator : ( + , - , / , *) : ")

if(operator == "+"):
    print( num1 + num2)

elif(operator == "-"):
    print(  num1 - num2)

elif(operator == "/"):
    print(num1 / num2)

elif(operator == "*"):
    print(num1 * num2)


             

# num1 = input("Enter a digit : ")
# num2 = input("Enter a digit : ")
# #taking operator from user
# operator = input("Enter operator : ( + , - , * , / ) : ")

# if (num1 >=1 and num2 >=1 , operator == "+"):
#     print(num1, operator , num2 , "=" , (num1 + num2))

# elif (num1 >=1 and num2 >=1 , operator == "-"):
#     print(num1, operator , num2 , "=" , (num1 - num2))

# elif (num1 >=1 and num2 >=1 , operator == "*"):
#     print(num1, operator , num2 , "=" , (num1 * num2))    

# elif (num1 >=1 and num2 >=1 , operator == "/"):
#     print(num1, operator , num2 , "=" , (num1 / num2))   


sum = 0
index = 0
for index in range(1, index+1, 1):
    if (index % 2 == 0):
        print(index)
        sum = sum+index
print(sum)