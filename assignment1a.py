# Student profile system
student_name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")

skills = []
for i in range(1, 4):
    skill = input(f"Enter skill {i}: ")
    skills.append(skill)

student = {
    "Name" : student_name,
    "Age" : age,
    "Course": course,
    "Skills" : skills
}

print(student)