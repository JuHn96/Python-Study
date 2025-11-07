# 복리 이자 계산 (원금, 이율, 기간)
principal = 1000000  # 원금 100만원
rate = 0.05          # 연 5%
years = 10           # 10년

# 복리 공식: A = P(1 + r)^t
final_amount = principal * (1 + rate) ** years
interest = final_amount - principal

print(f"원금: {principal:,}원")
print(f"이율: {rate * 100}%")
print(f"기간: {years}년")
print(f"최종 금액: {final_amount:,.0f}원")
print(f"이자: {interest:,.0f}원")

# 2배가 되는 기간 계산 (72의 법칙)
doubling_time = 72 / (rate * 100)
print(f"원금이 2배가 되는 기간: 약 {doubling_time:.1f}년")