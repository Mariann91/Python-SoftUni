def find_min(n1, n2, n3):
    min_num = min([n1, n2, n3])
    return min_num


num1, num2, num3 = int(input()), int(input()), int(input())
print(find_min(num1, num2, num3))
