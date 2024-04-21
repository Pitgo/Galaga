from dataclasses import dataclass

class Student:
    def __init__(self, name="", major="", minor="", emphasis="", grade=""):
        self.name = name
        self.major = major
        self.minor = minor
        self.emphasis = emphasis
        self.grade = grade

students = []

student_0 = Student()
student_0.name = "Jaime"
student_0.major = "CS"
student_0.minor = "Game Design"
student_0.emphasis = "Game Design"
student_0.grade = "A-"
students.append(student_0)

student_1 = Student()
student_1.name = "Alex"
student_1.major = "CS"
student_1.minor = "Cyber"
student_1.emphasis = "Cyber"
student_1.grade = "B+"
students.append(student_1)

student_2 = Student()
student_2.name = "Emily"
student_2.major = "CS"
student_2.minor = "Game Design"
student_2.emphasis = "Game Design"
student_2.grade = "A"
students.append(student_2)

student_3 = Student()
student_3.name = "Chris"
student_3.major = "EE"
student_3.minor = "ME"
student_3.emphasis = "Robotics"
student_3.grade = "B"
students.append(student_3)

student_4 = Student()
student_4.name = "Sophie"
student_4.major = "ME"
student_4.minor = "EE"
student_4.emphasis = "Robotics"
student_4.grade = "A-"
students.append(student_4)

student_5 = Student()
student_5.name = "Ryan"
student_5.major = "CS"
student_5.minor = "Cyber"
student_5.emphasis = "Cyber"
student_5.grade = "B+"
students.append(student_5)

student_6 = Student()
student_6.name = "Jordan"
student_6.major = "ME"
student_6.minor = "Robotics"
student_6.emphasis = "Robotics"
student_6.grade = "A"
students.append(student_6)

student_7 = Student()
student_7.name = "Mia"
student_7.major = "EE"
student_7.minor = "CS"
student_7.emphasis = "Robotics"
student_7.grade = "B+"
students.append(student_7)

student_8 = Student()
student_8.name = "Brandon"
student_8.major = "ME"
student_8.minor = "CS"
student_8.emphasis = "Robotics"
student_8.grade = "A-"
students.append(student_8)

while True:
    print("Display following:\n"
          "1. All CS Majors\n"
          "2. CS Minors with an EE or ME Major\n"
          "3. All CS Majors with an Emphasis on Robotics/Game Design/Cyber\n"
          "4. All students who have grades A- or A")
    option = int(input())

    if option == 1:
        for i, student in enumerate(students):
            if student.major == "CS":
                print(f"Student {i}:\nName: {student.name}\nMajor: {student.major}\nMinor: {student.minor}\nEmphasis: {student.emphasis}\nGrade: {student.grade}\n")

    if option == 2:
        for i, student in enumerate(students):
            if student.major == "EE" or student.major == "CS" and student.minor == "CS":
                print(f"Student {i}:\nName: {student.name}\nMajor: {student.major}\nMinor: {student.minor}\nEmphasis: {student.emphasis}\nGrade: {student.grade}\n")

    if option == 3:
        for i, student in enumerate(students):
            if student.major == "CS" and student.emphasis == "Robotics" or student.emphasis == "Game Design" or student.emphasis == "Cyber":
                print(f"Student {i}:\nName: {student.name}\nMajor: {student.major}\nMinor: {student.minor}\nEmphasis: {student.emphasis}\nGrade: {student.grade}\n")

    if option == 4:
        for i, student in enumerate(students):
            if student.grade == "A" or student.grade == "A-":
                print(f"Student {i}:\nName: {student.name}\nMajor: {student.major}\nMinor: {student.minor}\nEmphasis: {student.emphasis}\nGrade: {student.grade}\n")