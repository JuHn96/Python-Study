# 각 요소에 함수 적용
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers)) # map() - 모든 요소에 함수 적용
print(squared)  # [1, 4, 9, 16, 25]

# 문자열을 숫자로
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)  # [1, 2, 3, 4, 5]