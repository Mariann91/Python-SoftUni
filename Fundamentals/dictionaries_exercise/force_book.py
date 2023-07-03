def check_user_presence(dic, name):
  for value in dic.values():
    if name in value:
      return True
  return False

forcebook = {}

while True:

  info = input()

  if info == "Lumpawaroo":
    break

  if " | " in info:
    force_side, force_user = info.split(" | ")
   
    if check_user_presence(forcebook, force_user):
      continue
    
    if force_side not in forcebook and force_user not in forcebook.values():
      forcebook[force_side] = []
    
    forcebook[force_side].append(force_user)

  elif " -> " in info:
    force_user, force_side = info.split(" -> ")
    
    if check_user_presence(forcebook, force_user):
      for side in forcebook:
        if force_user in forcebook[side]:
          forcebook[side].remove(force_user)      
    else:
      if force_side not in forcebook and force_user not in forcebook.values():
        forcebook[force_side] = []

    forcebook[force_side].append(force_user)
    print(f"{force_user} joins the {force_side} side!")

for side, users in forcebook.items():

  if len(users) > 0:
    print(f"Side: {side}, Members: {len(users)}")
    [print(f" ! {user}") for user in users]
    
