# studentnames = ["Sanjoy" , "Urvashi" , "Minakshi"]
# physicsmarks = [50 , 60 , 70]
# sciencemarks = [50 , 60 , 70]
# englishmarks = [50 , 60 , 70]

# print(studentnames[0] , "got" , physicsmarks[0] , "in Physics" , sciencemarks[0] , "in Science" , englishmarks[0] , "in English")
# print(studentnames[1] , "got" , physicsmarks[1] , "in Physics" , sciencemarks[1] , "in Science" , englishmarks[1] , "in English")
# print(studentnames[2] , "got" , physicsmarks[2] , "in Physics" , sciencemarks[2] , "in Science" , englishmarks[2] , "in English")

# ###using for loop

# studentNames = ["Sanjoy" , "Urvashi" , "Minakshi"]
# physicsMarks = [50 , 60 , 70]
# scienceMarks = [50 , 60 , 70]
# englishMarks = [50 , 60 , 70]



####for adding name in a range
studentNames = ["Sanjoy" , "Urvashi" , "Minakshi"]

for index in range (0 , 1, 1):
    studentNames.append ("Ayush")
    print(studentNames)

###for inserting a name in a range
for index in range (0 , 1 ,1):
    studentNames.insert(0 , " Purva")
    print(studentNames)