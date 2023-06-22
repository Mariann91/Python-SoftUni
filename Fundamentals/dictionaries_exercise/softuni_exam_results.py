submissions_info = {}
language_info = {}

while True:
  submission = input()

  if submission == "exam finished":
    break
    
  submission = submission.split("-")
  name = submission[0]

  if submission[1] == "banned":
    submissions_info.pop(name)
    continue

  language = submission[1]
  current_submission = int(submission[2])
  
  if name not in submissions_info or submissions_info[name] < current_submission:
    submissions_info[name] = current_submission

  if language in language_info:
    language_info[language] += 1
  else:
    language_info[language] = 1

print("Results:")
[print(f"{name} | {score}") for name, score in submissions_info.items()]
print("Submissions:")

[print(f"{language} - {count}") for language, count in language_info.items()]
