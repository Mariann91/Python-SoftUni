nums = tuple(float(num) for num in input().split())

output = {num: nums.count(num) for num in nums}
[print(f"{num} - {times} times") for num, times in output.items()]
