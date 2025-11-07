# 함수 합성
def compose(f, g):
    """두 함수를 합성"""    
    return lambda x: f(g(x))
    
# 기본 함수들
add_10 = lambda x: x + 10
multiply_2 = lambda x: x * 2
square = lambda x: x ** 2

# 함수 합성
add_then_multiply = compose(multiply_2, add_10)
multiply_then_add = compose(add_10, multiply_2)

x = 5
print(f"x = {x}")
print(f"(x + 10) × 2 = {add_then_multiply(x)}")
print(f"(x × 2) + 10 = {multiply_then_add(x)}")

# 파이프라인 처리
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 여러 단계 변환
result = list(map(
    lambda x: x ** 2,              # 3. 제곱    
    filter(
        lambda x: x % 2 == 0,      # 2. 짝수만        
        map(
            lambda x: x + 1,       # 1. 1 더하기            
            numbers
        )
    )
))

print(f"\n원본: {numbers}")
print(f"변환 결과: {result}")

# reduce 사용 (functools 필요)
# reduce() 함수는 리스트의 모든 요소를 하나의 값으로 누적 계산하는 함수
from functools import reduce

# 모든 수의 곱
product = reduce(lambda x, y: x * y, numbers) 
print(f"\n1부터 10까지 곱: {product}")

# 최대값 찾기
max_val = reduce(lambda x, y: x if x > y else y, numbers)
print(f"최대값: {max_val}")