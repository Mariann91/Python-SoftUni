key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

while_break = False
while True:
    materials = input().split()

    material = ""
    for index in range(0, len(materials), 2):
        material = materials[index + 1].lower()
        quantity = int(materials[index])

        if material in key_materials:
            
            key_materials[material] += quantity
            if material == "shards" and key_materials[material] >= 250:
                print("Shadowmourne obtained!")
                while_break = True
                break

            if material == "fragments" and key_materials[material] >= 250:
                print("Valanyr obtained!")
                while_break = True
                break

            if material == "motes" and key_materials[material] >= 250:
                print("Dragonwrath obtained!")
                while_break = True
                break
        else:
            key_materials[material] = quantity

    if while_break:
        key_materials[material] -= 250
        break

for material, quantity in key_materials.items():
    print(f"{material}: {quantity}")
