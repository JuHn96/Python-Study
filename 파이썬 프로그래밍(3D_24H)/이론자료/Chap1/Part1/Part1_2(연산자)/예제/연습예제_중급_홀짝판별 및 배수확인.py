number = 24

# 홀짝 판별
is_even = (number % 2 == 0)
print(f"{number}는 {'짝수' if is_even else '홀수'}입니다")

# 3의 배수이면서 4의 배수인지 확인
is_multiple_of_3 = (number % 3 == 0)
is_multiple_of_4 = (number % 4 == 0)
is_both = is_multiple_of_3 and is_multiple_of_4

print(f"3의 배수: {is_multiple_of_3}")
print(f"4의 배수: {is_multiple_of_4}")
print(f"3과 4의 공배수: {is_both}")