student_info = {}

info = input()

while info != "end":
  course_name, student_name = info.split(" : ")

  if course_name not in student_info:
    student_info[course_name] = []

  student_info[course_name].append(student_name)

  info = input()

for course_name, student_names in student_info.items():
  student_count = len(student_names)
  print(f"{course_name}: {student_count}")

  for student_name in student_names:
    print(f"-- {student_name}")
    
