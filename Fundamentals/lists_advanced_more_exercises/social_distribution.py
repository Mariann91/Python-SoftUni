population_list = [int(num) for num in input().split(", ")]
min_wealth = int(input())

while min(population_list) < min_wealth:
    if sum(population_list) // len(population_list) < min_wealth:
        print("No equal distribution possible")
        break

    for index in range(len(population_list)):
        max_wealth = max(population_list)
        max_wealth_index = population_list.index(max_wealth)
        if population_list[index] < min_wealth:
            population_list[max_wealth_index] -= (min_wealth - population_list[index])
            population_list[index] = min_wealth
else:
    print(population_list)
