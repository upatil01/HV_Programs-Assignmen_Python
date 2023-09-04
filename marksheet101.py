# userInput=int(input("Provide your input"))
# program for adding two numbers
# create a Marksheet application for a school
# 3 subjects , maths, science, english
# student name , marks of these three subjects
# total of the marks , if the student have passed or not/
# The grade of the student , 0 t0 30: F,30-60: D, 61, 80,: B, 81,100: A
# to store multiple values in one single variable
# array/list


# identify the topper for the batch
# rank of the learner
# we need to store that information
# variable
# list
students = []


flag = "y"
while (flag == "y"):
    student = {}
    studentName = input("Please enter the student Name: ")
    student["name"] = studentName
    subjectFlag = "y"
    # subject = {}
    subjects = []
    # taking the inputs for marks
# validation logic
    totalMarks = 0
    while (subjectFlag == "y"):
        subject = {}
        subjectName = (input("Please enter the name of the subject : "))
        marks = int(input("enter the marks for the subject : "))
        subject["name"] = subjectName
        subject["marks"] = marks
        subjects.append(subject)
        totalMarks = totalMarks+marks
        subjectFlag = input("do you have any other subject data y/n")

# Processing the marks
    student["totalMarks"] = totalMarks
    print(" The total marks of the student would be ", totalMarks)

# percentage of the total marks
    percentageMarks = (totalMarks/300)*100
    student["percentageMarks"] = percentageMarks
    student["subjects"] = subjects
    # appending the student to the list
    students.append(student)
#####
# if statement
    if (percentageMarks < 30):
        print(" The student have failed")
        print(" grade : F")
    elif (percentageMarks < 60):

        print("Grade D")

    elif (percentageMarks < 80):

        print("grade A")
    else:
        print("grade E")
    flag = input("do you have any other student data y/n")

print(students)


# subject: name, marks
# subjects: list of subject
# student: has a key as subjects
# students is a list of student