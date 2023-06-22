interval = int(input())

license_plate_data = {}
for _ in range(interval):
  command_line = input().split()
  command = command_line[0]
  username = command_line[1]

  if command == "register":  
    license_plate_number = command_line[2]

    if username not in license_plate_data:
      license_plate_data[username] = license_plate_number
      print(f"{username} registered {license_plate_number} successfully")
    else:
      print(f"ERROR: already registered with plate number {license_plate_data[username]}")

  elif command == "unregister":
    if username not in license_plate_data:
      print(f"ERROR: user {username} not found")
    else:
        license_plate_data.pop(username)
        print(f"{username} unregistered successfully")

for username, license_plate_number in license_plate_data.items():
  print(f"{username} => {license_plate_number}")
  
