def calculator(num1, num2, operation):
    """계산기 함수
    operation: '+', '-', '*', '/'
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "0으로 나눌 수 없습니다"
        return num1 / num2
    else:
        return "지원하지 않는 연산자입니다"


# 테스트
print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # "0으로 나눌 수 없습니다"
