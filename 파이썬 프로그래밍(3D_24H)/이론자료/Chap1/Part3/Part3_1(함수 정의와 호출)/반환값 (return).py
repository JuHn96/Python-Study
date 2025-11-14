def add(a, b):
    return a + b
    
result = add(3, 5)
print(result)  # 8

# 여러 값 반환
def get_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg
    
total, avg = get_stats([1, 2, 3, 4, 5])
# 함수는 앞서 배운 for문과 다르게 값이 먼저 지정되지 않고 함수를 지정해서 나중에 지정한 함수의 계산이 필요할때 원하는 값으로 함수를 호출하는 방식

print(f"합계: {total}, 평균: {avg}")  # 합계: 15, 평균: 3.0