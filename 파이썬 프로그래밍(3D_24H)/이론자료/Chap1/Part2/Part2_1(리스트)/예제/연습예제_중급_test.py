numbers = []

print("숫자를 계속 입력하세요. 'x' 입력 시 종료됩니다.\n")

while True:
    value = input("입력: ")

    if value.lower() == "x":
        break

    try:
        numbers.append(int(value))
    except:
        print("⚠️ 숫자 또는 'x'만 입력해주세요.")

if not numbers:
    print("입력된 숫자가 없습니다.")
else:
    print(f"\n입력된 숫자: {numbers}")

    evens = [n for n in numbers if n % 2 == 0]
    print(f"짝수: {evens}")

    squares = [n**2 for n in numbers]
    print(f"제곱: {squares}")

    filtered_squares = [n**2 for n in numbers if n > 5]
    print(f"5보다 큰 수의 제곱: {filtered_squares}")

    transformed = [n*2 if n % 2 == 1 else n*3 for n in numbers]
    print(f"변환된 값: {transformed}")
