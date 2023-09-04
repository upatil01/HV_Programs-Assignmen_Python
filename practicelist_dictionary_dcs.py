studentsnames = ["Urvashi" , "Minakshi" , "Sunita"] 

for n in studentsnames:
    print( n )


##print the total marks of the student
##take i/p from user

marks = [67, 78, 89]
name = input("Enter your name : ")

##multiple ways to get similar o/p
# sum = marks[0] + marks[1] + marks[2]
#print("The name is :- ", name, "and the total marks is :-", (marks[0]+marks[1]+marks[2]))
# print("The name is :- ", name, "and the total marks is :-", sum)

print("The name is :- ", name, "and the total marks is :-", sum(marks))

##dictionary - key-value pair
##in dictionary we mentioned inputs in {} brackets

# subject_marks = { "maths" : 78 , "Science" : 80 , "English" : 90}
subject_marks = { "maths" : 0, "Science" : 0, "English" : 0}

print(subject_marks.keys())
print(subject_marks.values())
print(subject_marks)

##for adding maarks
tm = 0
for marks in subject_marks.values():
    tm += marks
if(tm == 0):
    print( "The total marks is zero")

else:
    print( "The total marks is : " , tm)
     
# print(" The total marks : " , tm ) 

my_dict = {"name": [], "age": []}
# my_dict["name"].append("Anik")
print(my_dict)   

##if you want to take input from user

user_input1 = input("Enter the name ")
my_dict["name"].append(user_input1)
# print(my_dict)

user_input2 = int(input("Enter the age "))
my_dict["age"].append(user_input2)
print(my_dict)