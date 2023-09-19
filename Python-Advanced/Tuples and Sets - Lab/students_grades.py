n = int(input())

students_info = {}

for _ in range(n):
    name, grade = input().split()

    if name not in students_info:
        students_info[name] = []

    students_info[name].append(float(grade))

for name, grades in students_info.items():
    print(f"{name} ->", ' '.join([f"{grade:.2f}" for grade in students_info[name]]),
          f"(avg: {sum(students_info[name]) / len(students_info[name]):.2f})")
