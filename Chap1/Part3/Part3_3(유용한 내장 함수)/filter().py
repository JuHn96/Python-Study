# 조건에 맞는 요소만 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers)) #filter() 함수는 조건을 만족하는 요소만 골라내는 함수
print(evens)  # [2, 4, 6, 8, 10]

# 리스트 컴프리헨션과 동일
evens2 = [x for x in numbers if x % 2 == 0]