courses_info = {}

current_course = input()

while current_course != "end":
    course_name, student_name = current_course.split(" : ")

    if course_name not in courses_info:
        courses_info[course_name] = []

    courses_info[course_name].append(student_name)

    current_course = input()

for course_name, student_names in courses_info.items():
    print(f"{course_name}: {len(student_names)}")

    [print(f"-- {student_name}") for student_name in student_names]
    
