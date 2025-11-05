# def get_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]

# print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def get_even_numbers(*numbers):
    return [num for num in numbers if num % 2 == 0]

while True:
    user_input = input("숫자를 입력하세요 (종료하려면 'stop'): ")
    if user_input.lower() == 'stop':
        break
    try:
        number = int(user_input)
        even_numbers = get_even_numbers(number)
        print(f"입력한 숫자 중 짝수: {even_numbers}")
    except ValueError:
        print("유효한 숫자를 입력하세요.")