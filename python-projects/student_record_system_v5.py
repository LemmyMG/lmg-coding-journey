def get_student_details():
    print("\n---------Student Record System---------")

    student_name = input("Enter Student Name: ")
    student_age = int(input("Enter Student Age: "))
    student_id = input("Enter Student ID: ")
    department = input("Enter Student Department: ")
    score = float(input("Enter Student Score: "))

    return student_name, student_age, student_id, department, score


def calculate_grade(score):
    if score >= 70:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"


def display_student_record(student_name, student_age, student_id, department, score, grade):
    print("\n------- Student Record -------")
    print("Student Name:", student_name)
    print("Student Age:", student_age)
    print("Student ID:", student_id)
    print("Department:", department)
    print("Score:", score)
    print("Grade:", grade)
    print("------------------------------")


# ===========================
# Main Program
# ===========================

for student in range(2):
    print("\n====== Entering Student", student + 1, "======")

    student_name, student_age, student_id, department, score = get_student_details()

    grade = calculate_grade(score)

    display_student_record(
        student_name,
        student_age,
        student_id,
        department,
        score,
        grade
    )