students_info = {}

info = input()

while ":" in info:
  name, student_id, course = info.split(":")

  if not students_info:
    students_info = {
      course: {
        name: student_id
      }
    }
  else:

    if course not in students_info:
      current_info = {
        course: {
          name: student_id
        }
      }
      students_info.update(current_info)
    else:
      current_info = {
        name: student_id
      }
      students_info[course].update(current_info)
  info = input()

searched_course = info

if "_" in searched_course:
  searched_course = searched_course.replace("_", " ")

for name, student_id in students_info[searched_course].items():
  print(f"{name} - {student_id}")
