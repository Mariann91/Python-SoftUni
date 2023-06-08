from math import ceil

student_count = int(input())
number_of_lectures = int(input())
add_bonus = int(input())

bonuses = []
lectures = []
for _ in range(student_count):
  current_student = int(input())

  total_bonus = ceil(current_student / number_of_lectures * (5 + add_bonus))  
  bonuses.append(total_bonus)
  lectures.append(current_student)

if len(bonuses) > 0:
  max_bonus = max(bonuses)
  max_bonus_index = bonuses.index(max_bonus)
  highest_student_lectures = lectures[max_bonus_index]

else:
  max_bonus = 0
  highest_student_lectures = 0

print(f"Max Bonus: {max_bonus}.\nThe student has attended {highest_student_lectures} lectures.")
