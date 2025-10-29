nums = [i for i in range(1, 51)]
filtered_squared = [x**2 for x in nums if x % 3 == 0]
print(filtered_squared)