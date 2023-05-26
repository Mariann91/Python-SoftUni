num = float(input())
 
if num == 0:
  print("zero")
elif 0 < num < 1:
  print("small positive")
elif 1 <= num <= 1_000_000:
  print("positive")
elif num > 1_000_000:
  print("large positive")
elif 0 > num > -1:
  print("small negative")
elif -1 >= num >= - 1_000_000:
  print("negative")
else:
  print("large negative")
  
