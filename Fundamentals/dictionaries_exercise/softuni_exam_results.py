exam_info = {}
submission_count = {}

while True:

  course_info = input()

  if course_info == "exam finished":
    break

  course_info = course_info.split("-")
  name = course_info[0]
  language = course_info[1]

  if language == "banned":
    if name in exam_info:
      exam_info.pop(name)
    else:
      continue
  else:
    points = int(course_info[2])
    if language not in submission_count:
      submission_count[language] = 1
    else:
      submission_count[language] += 1
    
    if len(exam_info) < 1:
       exam_info = {
        name: {
          language: [points]
        }
      }
      
    elif name not in exam_info:

      current_information = {
        name: {
          language: [points]
        }
      }
      exam_info.update(current_information)
        
    else:
      if language in exam_info[name]:
        exam_info[name][language].append(points)
      else:
        exam_info[name][language] = [points]

print("Results:")

for item in exam_info:
  print(item, end=" | ")
  for key, value in exam_info[item].items():
    print(max(value))
    break
    
print("Submissions:")
for language, count in submission_count.items():
  print(f"{language} - {count}")
