interval = int(input())

student_info = {}
for _ in range(interval):
  name = input()
  grade = float(input())

  if name not in student_info:
    student_info[name] = []

  student_info[name].append(grade)

for name, grades in student_info.items():
  average_grade = sum(grades) / len(grades)

  if average_grade < 4.50:
    continue

  print(f"{name} -> {average_grade:.2f}")
  
