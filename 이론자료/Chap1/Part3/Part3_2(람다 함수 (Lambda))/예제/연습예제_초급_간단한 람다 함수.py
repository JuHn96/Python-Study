# 다양한 연산을 람다로
add = lambda x, y: x + y
multiply = lambda x, y: x * y
power = lambda x, n: x ** n

print(f"5 + 3 = {add(5, 3)}")
print(f"5 × 3 = {multiply(5, 3)}")
print(f"5^3 = {power(5, 3)}")

# 리스트에 적용
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"2배: {doubled}")