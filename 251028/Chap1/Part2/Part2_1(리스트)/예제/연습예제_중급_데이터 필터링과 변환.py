

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만 선택
evens = [n for n in numbers if n % 2 == 0]
print(f"짝수: {evens}")

# 제곱 계산
squares = [n**2 for n in numbers]
print(f"제곱: {squares}")

# 5보다 큰 수만 제곱
filtered_squares = [n**2 for n in numbers if n > 5]
print(f"5보다 큰 수의 제곱: {filtered_squares}")

# 홀수는 2배, 짝수는 3배
transformed = [n*2 if n % 2 == 1 else n*3 for n in numbers]
print(f"변환된 값: {transformed}")