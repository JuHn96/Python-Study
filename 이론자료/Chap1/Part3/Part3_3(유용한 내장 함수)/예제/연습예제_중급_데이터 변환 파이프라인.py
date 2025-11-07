# 원본 데이터
prices = ["1,000", "2,500", "3,200", "1,800", "4,000"]

# 파이프라인: 문자열 → 숫자 → 계산
# 1. 쉼표 제거
cleaned = list(map(lambda x: x.replace(",", ""), prices))
print(f"1. 쉼표 제거: {cleaned}")

# 2. 정수로 변환
numbers = list(map(int, cleaned))
print(f"2. 숫자 변환: {numbers}")

# 3. 10% 할인
discounted = list(map(lambda x: int(x * 0.9), numbers))
print(f"3. 10% 할인: {discounted}")

# 4. 2000원 이상만
filtered = list(filter(lambda x: x >= 2000, discounted))
print(f"4. 2000원 이상: {filtered}")

# 5. 다시 문자열로 (천 단위 구분)
formatted = list(map(lambda x: f"{x:,}원", filtered))
print(f"5. 최종 결과: {formatted}")

# 1. 쉼표 제거: ['1000', '2500', '3200', '1800', '4000']
# 2. 숫자 변환: [1000, 2500, 3200, 1800, 4000]
# 3. 10% 할인: [900, 2250, 2880, 1620, 3600]
# 4. 2000원 이상: [2250, 2880, 3600]
# 5. 최종 결과: ['2,250원', '2,880원', '3,600원']