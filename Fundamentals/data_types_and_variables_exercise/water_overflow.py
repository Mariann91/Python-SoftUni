TANK_CAPACITY = 255
interval = int(input())

current_tank_lv = 0
for _ in range(interval):
  litters_to_pour = int(input())

  if litters_to_pour > TANK_CAPACITY or litters_to_pour + current_tank_lv > TANK_CAPACITY:
    print("Insufficient capacity!")
    continue

  current_tank_lv += litters_to_pour
print(current_tank_lv)
