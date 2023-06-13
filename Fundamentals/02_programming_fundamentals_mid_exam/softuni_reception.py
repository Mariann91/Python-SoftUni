from math import ceil

employer1, employer2, employer3 = int(input()), int(input()), int(input())
student_count = int(input())

student_per_hour = employer1 + employer2 + employer3
hours_interval = ceil(student_count / student_per_hour)
hours_break = hours_interval

for hour in range(1, hours_interval + 1):
    if hour % 3 == 0 and hour != hours_interval:
        hours_break += 1

print(f"Time needed: {hours_break}h.")
