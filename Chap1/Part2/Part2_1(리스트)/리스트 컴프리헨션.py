# [표현식 for 변수 in 반복가능한객체]

# [표현식 for 변수 in 반복가능한객체 if 조건식]


# 일반 방법
squares = []

for i in range(10):
    squares.append(i ** 2)
    
# 리스트 컴프리헨션 (한 줄로!)
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 조건 포함
evens = [i for i in range(20) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# 테스트
evens = [i ** 2 for i in range(20) if i % 2 == 0]
print(evens)  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]