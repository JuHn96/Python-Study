# def calculate_sum(numbers):
#     return sum(numbers)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
# def calculate_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total


# print(calculate_sum([1, 2, 3, 4, 5]))


#------------------------------------------------------------------------
#------------------------------------------------------------------------

# 아래는 직접 입력받고 값 갯수에 제한이 없으며 입력을 하지 않으면 따로 안내문구가 나오는 코드. 현재 stop을 입력하면 종료 더 간단하게 원하면 while문 안에 break가 되는 조건에서 변경

def calculate_sum(*numbers):
    return sum(numbers)

sumdata = []

while True:
    user_input = input("숫자를 입력하세요 (종료하려면 'stop'): ")
    if user_input.lower() == 'stop':
        break
    try:
        number = int(user_input)
        sumdata.append(number)
    except ValueError:
        print("유효한 숫자를 입력하세요.")
if sumdata:
    print(f"입력한 숫자의 합은: {calculate_sum(*sumdata)}")