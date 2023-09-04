##finding the topper
##parameter students

def find_class_topper(students):
    topper = None
    topper_percentage = 0

    for student in students:
        if student["percentageMarks"] > topper_percentage:
            topper = student
            topper_percentage = student["percentageMarks"]

    return topper

def display_topper(topper):
    if topper is not None:
        print("The topper in the class is:", topper["name"])
    else:
        print("No students found.")

def main():
    students = []
    flag = "y"

    while flag == "y":
        student = add_student()
        students.append(student)
        flag = input("Do you have any other student data? (y/n): ")

    topper = find_class_topper(students)
    display_topper(topper)

    print(students)

def students_rank(totalmarkslist):
    rank = [i] * (len(totalmarkslist))

