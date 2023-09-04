# #Simple Interest Calculation

# A = P (1 + rt)
# A	=	final amount  # Output
# P	=	initial principal balance #Input from user
# r	=	annual interest rate   #fixed - r/i - 5%    rate_interest
# t	=	time (in years) #Input from user   # 10   15 


# Stage 1 - You are taking the inputs and it will display the final amount


# Stage 2 - Validation  - User - Principal Amount - 0
			    #    Time - 0

# p  = int(input ( "Enter the amount :"))
# t = int(input ("Enter the time : "))
# r = 0.05 
# A = p*( 1 + (r*t))
# print ("The final amount will be : " , A )

# P = int(input("Enter the Principal amount: "))
# t = int(input("Enter the time duration: "))

# r = 0.05 #(5%)
# A = P*(1 + (r*t))


# if P <= 0:
#     print("The Principal Amount or time cannot be 0 or negative")
# elif t <=0:
#     print("The Principal Amount or time cannot be 0 or negative")
# else:
#     print("The Final Amount Will be: ", A)

p  = int(input ( "Enter the amount :"))
t = int(input ("Enter the time duration : "))
r = 0.05 
#A = p(1+rt)
A = p*( 1 + (r*t))

#validation
if (p <= 0 ):
    print(" Check your value you dont put 0 ")
elif (t <= 0):
    print(" Check your value you dont put 0 ")
else:
    print("The final amount will be : " , A)    