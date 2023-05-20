fire_cells = input().split("#")
water = int(input())

EFFORT_PERCENT = 0.25

effort, total_fire = 0, 0
extinguished_fires = []
for cell in fire_cells:
    cell_list = cell.split(" = ")
    needed_water = int(cell_list[1])

    if cell_list[0] == "High" and 81 <= needed_water <= 125 and needed_water <= water:
        water -= needed_water
        effort += EFFORT_PERCENT * needed_water
        total_fire += needed_water
        extinguished_fires.append(needed_water)
    elif cell_list[0] == "Medium" and 51 <= needed_water <= 80 and needed_water <= water:
        water -= needed_water
        effort += EFFORT_PERCENT * needed_water
        total_fire += needed_water
        extinguished_fires.append(needed_water)
    elif cell_list[0] == "Low" and 1 <= needed_water <= 50 and needed_water <= water:
        water -= needed_water
        effort += EFFORT_PERCENT * needed_water
        total_fire += needed_water
        extinguished_fires.append(needed_water)

print(f"Cells:")
for item in extinguished_fires:
    print(f" - {item}")
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")
