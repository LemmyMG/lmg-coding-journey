print("---------Student Record System---------")
student_name = input("Enter Student Name: ")
student_age = int(input("Enter student Age: "))
student_id = input("Enter student ID: ")
department = input("Enter student Department: ")
score = float(input("Enter student Score: "))

print("\n------- Student Record ---------\n")
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student ID:", student_id)
print("Department:", department)
print("Score:", score)

if score >= 70:
    print("Grade: Excellent")
elif score >= 60:
    print("Grade: Good")
elif score >= 50:
    print("Grade: Average")
else:
    print("Grade: Poor")
print("\n-------------------------------------")

