longest_intersection = []

for _ in range(int(input())):
  first, second = input().split("-")
  first_start, first_end = [int(num) for num in first.split(",")]
  second_start, second_end = [int(num) for num in second.split(",")]
  start = max(first_start, second_start)
  end = min(first_end, second_end)
  
  comaparing_list = [num for num in range(start, end + 1)]

  if len(comaparing_list) > len(longest_intersection):
    longest_intersection = comaparing_list

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
