contest_data = {}

data = input()

while data != "no more time":
  # "{username} -> {contest} -> {points}"
  username, contest, points = data.split(" -> ")
  points = int(points)

  if not contest_data:
    contest_data = {
      contest : {
        username : points,
      }
    }

  elif contest not in contest_data:
    current_info = {
      contest : {
        username : points,
      }
    }
    contest_data.update(current_info)
  else:
    if username in contest_data[contest]:     
      if contest_data[contest][username] < points:
        contest_data[contest][username] = points
    else:
      contest_data[contest][username] = points
      
  data = input()

standings = {}

for course in contest_data:
  print(f"{course}: {len(contest_data[course])} participants")
  
  sorted_contest_data = dict(sorted(contest_data[course].items(), key=lambda x:x[1], reverse=True))
  counter = 0
  for name, points in sorted_contest_data.items():
    if name not in standings:
      standings[name] = points
    else:
      standings[name] += points
    counter += 1
    print(f"{counter}. {name} <::> {points}")
    
print("Individual standings:")

sorted_standings = dict(sorted(standings.items(), key=lambda x:x[1], reverse=True))
number = 0
for name, points in sorted_standings.items():
  number += 1
  print(f"{number}. {name} -> {points}")
