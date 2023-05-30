num = [int(num) for num in input()]
num.sort(reverse=True)
print(*num, sep="")
