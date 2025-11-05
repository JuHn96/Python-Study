# def find_max(a, b, c):
#     # 여기에 코드 작성
#     if a > b and a > c:
#         return a
#     elif b > c:
#         return b
#     else:
#         return c
#     return max(a, b, c)
# print(find_max(10, 25, 15))

# input_a = int(input("첫 번째 숫자를 입력하세요: "))
# input_b = int(input("두 번째 숫자를 입력하세요: "))
# input_c = int(input("세 번째 숫자를 입력하세요: "))
# print(find_max(input_a, input_b, input_c))

#------------------------------------------------------------------------
#------------------------------------------------------------------------

# 아래는 직접 입력받고 값 갯수에 제한이 없으며 입력을 하지 않으면 따로 안내문구가 나오는 코드. 현재 stop을 입력하면 종료 더 간단하게 원하면 while문 안에 break가 되는 조건에서 변경


def find_max(*numbers):
    return max(numbers)

nums = []  # 입력된 숫자를 저장할 리스트

while True:
    user_input = input("숫자를 입력하세요 (그만하려면 'stop'): ")
    
    if user_input.lower() == "stop":  # stop 입력 시 종료
        break
    
    # 숫자로 변환 가능한지 확인 (예외 처리)
    try:
        nums.append(int(user_input))
    except ValueError:
        print("숫자만 입력하세요.")

# 입력이 한 개 이상일 때만 결과 출력
if nums:
    print(f"가장 큰 수는 {find_max(*nums)}입니다.")
else:
    print("입력된 숫자가 없습니다.")