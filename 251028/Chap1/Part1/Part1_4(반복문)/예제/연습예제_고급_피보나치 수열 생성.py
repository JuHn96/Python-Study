# n번째까지 피보나치 수열 생성
n = int(input("몇 번째 항까지 피보나치 수열을 생성할까요? "))

# 첫 두 항
fib = [0, 1]

# 나머지 항 계산
for i in range(2, n):
    next_num = fib[i-1] + fib[i-2]  # 다음 항에 들어갈 값을 계산하는 부분
    fib.append(next_num)    # fib에 항 추가하는 부분
    
print(f"피보나치 수열 (처음 {n}개):")
print(fib)

# 황금비 계산 (연속된 두 항의 비율)
golden_ratio = fib[-1] / fib[-2]
print(f"황금비 근사값: {golden_ratio:.6f}")
print(f"실제 황금비: {(1 + 5**0.5) / 2:.6f}")