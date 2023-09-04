#Take inputs - starting no.  & ending no.

#Assume - starting no - 15     ending no. - 30

#loop - while /for loop

#print those numbers

###for Loop
# index = 0
# inp1 = int(input( " Enter a starting numder : "))
# inp2 = int(input( " Enter the ending number : "))
# for i in range( inp1 , inp2+1 , 1 ):
#     index = index+1
#     print(i)

              ####or
sum = 0
inp1 = int(input( " Enter a starting numder : "))
inp2 = int(input( " Enter the ending number : "))
for i in range( inp1 , inp2+1 , 1 ):
    if (i % 2 == 0):
        print(i)  
        sum += i
print(sum)



# take starting and ending number from user and print all even numbers using loop in python
# and add Even and Odd numbers
# startNumber = int(input("Enter the starting number: "))
# endNumber = int(input("Enter the ending number: "))

# sumOfEvenNumbers = 0
# sumOfOddNumbers = 0

# print("Even numbers between", startNumber, "and", endNumber, "are:")

# for num in range(startNumber, endNumber+1):
#     if num % 2 == 0:
#         print(num)
#         sumOfEvenNumbers += num
#     else:
#         sumOfOddNumbers += num


# print("Sum of even numbers:", sumOfEvenNumbers)
# print("Sum of odd numbers:", sumOfOddNumbers)

sumofevennumbers = 0
sumofoddnumbers = 0
inp1 = int(input( " Enter a starting numder : "))
inp2 = int(input( " Enter the ending number : "))
for i in range( inp1 , inp2+1 , 1 ):
    if (i % 2 == 0):
        # print(i)  
        sumofevennumbers += i
    else:
        print(i)
        sumofoddnumbers += i    
print("Sum of even numbers :" ,sumofevennumbers)    
print("Sum of odd numbers : " ,sumofoddnumbers)    


