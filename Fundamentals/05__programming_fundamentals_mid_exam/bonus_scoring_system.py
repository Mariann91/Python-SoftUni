students_count = int(input())
course_lectures = int(input())
additional_bonus = int(input())

max_attendances = 0
max_bonus = 0

if course_lectures > 0:
  
  for _ in range(students_count):
    student_attendances = int(input())
  
    total_bonus = student_attendances / course_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
      max_bonus = total_bonus
      max_attendances = student_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")
