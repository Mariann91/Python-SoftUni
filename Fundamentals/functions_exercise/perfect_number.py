def find_perfect_number(num):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i

    if sum_divisors == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(find_perfect_number(number))
