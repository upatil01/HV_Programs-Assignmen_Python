#take inputs from teacher
studentNamesList = []
mathMarksList =[]
scienceMarksList = []
englishMarksList = []
totalMarksList = []
percentageList = []

flag = "y"
while ( flag == "y"):
    studentName=input("Enter the student name:")
    studentNamesList.append(studentName)

    mathMarks=int(input("Enter the marks for maths:"))
    mathMarksList.append(mathMarks)

    scienceMarks=int(input("Enter the marks for science:"))
    scienceMarksList.append(scienceMarks)

    englishMarks=int(input("Enter the marks for english:"))
    englishMarksList.append(englishMarks)

    totalMarks=mathMarks+scienceMarks+englishMarks
    totalMarksList.append(totalMarks) 

    print("The total marks of student would be:" , totalMarks)

    percentage=(totalMarks/300)*100
    percentageList.append(percentage)
    print(percentage)
    if(percentage >= 30):
        print("The student has passesd")
        print("Congratulation")
    else:
        print("The student has failed")
        print("Better luck next time")

#printing the grades
    if(percentage < 30):
        print( "The student has failed")
        print("Grade f")
    elif(percentage < 60):
        print( "Grade D")
    elif(percentage < 80):
        print("Grade B")    
    elif(percentage < 100):
        print("Grade A")   
    flag = input("do you have another student data : y/n")    
        
print(studentNamesList)
print(totalMarksList)
print(percentageList)


# topper = 0
# topperi= 0
# for i in range (0 , len(totalMarksList) ,1):
#     if(totalMarks > totalMarksList[i]):
#         topper = totalMarksList[i]
#         topperIndex = i
# print(" The topper is " , studentNamesList[i])       


topper = 0
topperi= 0
for i in range (len(studentNamesList)):
    if(totalMarksList[i] > topper):
        topper = totalMarksList[i]
        topperi = i
print(" The topper is " , studentNamesList[topperi])       


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


# studentNames = []
# mathMarksList = []
# scienceMarksList = []
# englishMarksList = []
# totalMarksList = []
# percentageMarksList = []

# flag = "y"
# while (flag == "y"):
#     studentName = input("Please enter the student Name:")
#     studentNames.append(studentName)
# # validation logic
#     mathMarks = int(input("Please enter the marks for Math"))
#     mathMarksList.append(mathMarks)
#     scienceMarks = int(input(" Enter the marks for Science"))
#     scienceMarksList.append(scienceMarks)
#     englishMarks = int(input(" Enter the marks for English"))
#     englishMarksList.append(englishMarks)

# # Processing the marks
#     totalMarks = mathMarks+scienceMarks+englishMarks
#     totalMarksList.append(totalMarks)
#     print(" The total marks of the student would be ", totalMarks)

# # percentage of the total marks
#     percentageMarks = (totalMarks/300)*100
#     percentageMarksList.append(percentageMarks)
# #####
# # if statement
#     if (percentageMarks < 30):
#         print(" The student have failed")
#         print(" grade : F")
#     elif (percentageMarks < 60):

#         print("Grade D")

#     elif (percentageMarks < 80):

#         print("grade A")
#     else:
#         print("grade E")
#     flag = input("do you have any other student data y/n")

# print(studentNames)
# print(totalMarksList)


ranks = [1] * len(totalMarksList)

for i in range (len(totalMarksList)):
    for j in range (len(totalMarksList)):
        if totalMarksList[i] < totalMarksList[j]:
            ranks [i] += 1

##display the rank
print( " Ranking of the all students")

for a in range (len(studentNamesList)):
    print (" Rank" , ranks[a] , ":" , studentNamesList[a])


