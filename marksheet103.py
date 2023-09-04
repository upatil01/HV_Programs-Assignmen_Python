# # def printoperator(operator):
# #     print(operator)

# # num1 = (" Plesae enter the number : ")
# # num2 = (" Please enter the number :")
# # operator = ("+" , "-" , "%" , "/")

# # if(operator=="+"):
# #     print( num1 * num2) 
# # elif(operator=="+"):
# #     print(num1 + num2)    

# # else:
# #     print()    
     

# def multiply( num1 , num2):
#     return num1 * num2

# def addition( num1 , num2):
#     return num1 + num2
   
# operator = (" Please enter the operator : ")
# num1 = (" Plesae enter the number : ")
# num2 = (" Please enter the number :")

# if(operator=="*"):
#     result = multiply(num1 , num2)

# elif(operator=="+"):
#     result = addition(num1 , num2)


# print(result)    





# # operator=input("please input the operator")
# # num1=input("please enter number 1")
# # num2=input("please enter number 2")
# # if(operator=="*"):
# #     multiply()


from multiply import multiply
from division import division
from subtract import subtract
operator = input("please input the operator : ")
num1 = input("please enter number 1 : ")
num2 = input("please enter number 2 : ")
if (operator == "*"):
    result = multiply(num1 , num2)
elif (operator == "/"):
    result = division(num1 ,num2)
elif (operator == "-"):
    result = subtract(num1 , num2)
print(result)








