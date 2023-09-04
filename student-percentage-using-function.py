def input_subject_data():
    subjects = []
    subject_flag = "y"
    total_marks = 0

    while subject_flag == "y":
        subject = {}
        subject_name = input("Please enter the name of the subject: ")
        marks = int(input("Enter the marks for the subject: "))
        subject["name"] = subject_name
        subject["marks"] = marks
        subjects.append(subject)
        total_marks += marks
        subject_flag = input("Do you have any other subject data? (y/n): ")

    return subjects, total_marks


def calculate_percentage_marks(total_marks, num_subjects):
    return (total_marks / (num_subjects * 100)) * 100


def calculate_grade(percentage_marks):
    if percentage_marks >= 90:
        return "A"
    elif percentage_marks >= 60:
        return "B"
    elif percentage_marks >= 40:
        return "C"
    elif percentage_marks >= 20:
        return "D"
    else:
        return "E"


def add_student():
    student = {}
    student_name = input("Please enter the student name: ")
    student["name"] = student_name

    subjects, total_marks = input_subject_data()
    student["totalMarks"] = total_marks

    percentage_marks = calculate_percentage_marks(total_marks, len(subjects))
    student["percentageMarks"] = percentage_marks
    student["subjects"] = subjects

    return student


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


if __name__ == "__main__":
    main()