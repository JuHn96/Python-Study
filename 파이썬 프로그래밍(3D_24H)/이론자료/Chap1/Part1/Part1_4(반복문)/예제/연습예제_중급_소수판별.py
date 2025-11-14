number = int(input("숫자를 입력하세요: "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False            
            print(f"{number}는 {i}로 나누어떨어짐")
            break
if is_prime:
    print(f"{number}는 소수입니다")
else:
    print(f"{number}는 소수가 아닙니다")