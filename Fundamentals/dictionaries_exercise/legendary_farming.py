materials_dic = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}

MATERIALS_LIMIT = 250

break_flag = False
while not break_flag:
    materials = input().split()

    for index in range(1, len(materials), 2):
        current_material = materials[index].lower()
        material_quantity = int(materials[index - 1])

        if current_material in materials_dic:
            materials_dic[current_material] += material_quantity
        else:
            materials_dic[current_material] = material_quantity

        if materials_dic["shards"] >= MATERIALS_LIMIT or \
                materials_dic["fragments"] >= MATERIALS_LIMIT or materials_dic["motes"] >= MATERIALS_LIMIT:
            break_flag = True
            break

if materials_dic["shards"] >= MATERIALS_LIMIT:
    materials_dic["shards"] -= MATERIALS_LIMIT
    print("Shadowmourne obtained!")

elif materials_dic["fragments"] >= MATERIALS_LIMIT:
    materials_dic["fragments"] -= MATERIALS_LIMIT
    print("Valanyr obtained!")

elif materials_dic["motes"] >= MATERIALS_LIMIT:
    materials_dic["motes"] -= MATERIALS_LIMIT
    print("Dragonwrath obtained!")

for material, quantity in materials_dic.items():
    print(f"{material}: {quantity}")
