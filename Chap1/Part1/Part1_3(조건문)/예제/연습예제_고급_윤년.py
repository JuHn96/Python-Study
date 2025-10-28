year = 2024

# 윤년 조건:
# 1. 4로 나누어떨어지고
# 2. 100으로 나누어떨어지지 않거나
# 3. 400으로 나누어떨어지면 윤년

if year % 400 == 0:
    is_leap = True    
    reason = "400으로 나누어떨어짐"
elif year % 100 == 0:
    is_leap = False    
    reason = "100으로 나누어떨어지지만 400으로는 안 됨"
elif year % 4 == 0:
    is_leap = True    
    reason = "4로 나누어떨어짐"
else:
    is_leap = False    
    reason = "4로 나누어떨어지지 않음"
    
print(f"{year}년은 {'윤년' if is_leap else '평년'}입니다")
print(f"이유: {reason}")

# 해당 연도 2월의 일수
february_days = 29 if is_leap else 28
print(f"{year}년 2월: {february_days}일")