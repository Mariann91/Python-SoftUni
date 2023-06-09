from math import ceil

employer1 = int(input())
employer2 = int(input())
employer3 = int(input())
students_count = int(input())

students_per_hour = employer1 + employer2 + employer3
hours = ceil(students_count / students_per_hour)
hours_break = hours

for hour in range(1, hours + 1):
    if hour % 3 == 0 and hour != hours:
        hours_break += 1

print(f"Time needed: {hours_break}h.")
