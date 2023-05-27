happiness_list = input().split()
factor = int(input())

happiness_list = [factor * int(num) for num in happiness_list]
average_happiness = sum(happiness_list) / len(happiness_list)
above_or_equal_to_average = list(filter(lambda x: x >= average_happiness, happiness_list))
half_people_count = len(happiness_list) / 2

if len(above_or_equal_to_average) >= half_people_count:
    print(f"Score: {len(above_or_equal_to_average)}/{len(happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(above_or_equal_to_average)}/{len(happiness_list)}. Employees are not happy!")
