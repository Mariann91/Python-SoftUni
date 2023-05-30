budget = float(input())
flour_per_kg_price = float(input())

loaf_price = flour_per_kg_price * 0.75 + flour_per_kg_price + (flour_per_kg_price * 1.25) * 0.25

loaf_count = 0
colored_eggs = 0
while budget >= loaf_price:
  loaf_count += 1
  colored_eggs += 3
  budget -= loaf_price

  if loaf_count % 3 == 0:
    colored_eggs -= loaf_count - 2

print(f"You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
