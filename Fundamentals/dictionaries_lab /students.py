student_dic = {}

while True:
  wanted_course = input()

  if ":" not in wanted_course:
    break
  
  name, id, course = wanted_course.split(":")
  
  if " " in course:
    course = course.replace(" ", "_")

  if course not in student_dic:   
    student_dic[course] = [name, id]
  else:
    name_id = [name, id]
    student_dic[course].extend(name_id)

wanted_course_student_list = student_dic[wanted_course]

for index in range(0, len(wanted_course_student_list), 2):
  student_name = student_dic[wanted_course][index]
  
  student_id = student_dic[wanted_course][index + 1]
  
  print(f"{student_name} - {student_id}")
