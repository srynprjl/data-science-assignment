## Build a simple grade calculator for multiple students. Input their marks in a list and print the grades using a function

def calculate_grade(mark):
    if(mark >= 90):
        return 'A'
    elif(mark >= 80):
        return 'B'
    elif(mark >= 70):
        return 'C'
    elif(mark >= 60):
        return 'D'
    elif(mark >=50):
        return 'E'
    else:
        return 'F'

def get_students_grade(marks):
    grades = []
    for i in marks:
        grade = calculate_grade(i)
        grades.append(grade)


    return grades

def display_grades(grades):
    for i in grades:
        print(i)

while True:
    students = int(input("Enter the number of students: "))
    if(students > 0):
        break
    else:
            print("Number of students cant be less than 0 ")
marks = []
for i in range(students):
    while True:
        mark = int(input("Enter the marks of student"))
        if(mark >= 0 and mark <= 100):
            break
        else:
            print("Invalid marks")

    marks.append(mark)

grades = get_students_grade(marks)
display_grades(grades)

