# ==========================================
# STUDENT MANAGEMENT PROJECT
# ==========================================

# ---------- MODULE 1: Student ----------
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\n----- Student Details -----")
        print("Name    :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks   :", self.marks)


# ---------- MODULE 2: Operations ----------
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def check_result(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


# ---------- MAIN PROJECT ----------
print("===== STUDENT MANAGEMENT SYSTEM =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks: "))

# Create Student object
student = Student(name, roll_no, marks)

# Display student information
student.display()

# Calculate grade and result
print("Grade   :", calculate_grade(marks))
print("Result  :", check_result(marks))