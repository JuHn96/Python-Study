age = 15
is_student = True
is_weekend = False

# 기본 요금
base_price = 10000

# 나이별 할인
if age < 13:
    discount = 0.5  # 50% 할인
elif age < 19:
    discount = 0.3  # 30% 할인
elif age >= 65:
    discount = 0.4  # 40% 할인
else:
    discount = 0    # 할인 없음
    
# 학생 추가 할인
if is_student and 13 <= age < 19:
    discount += 0.1  # 10% 추가 할인 여기서 위에 할인율에 + 적용된 값이 discount에 저장됨

# 주말 할증
if is_weekend:
    base_price = base_price * 1.2 # 여기서 최종 할인율에 곱해짐
    
# 최종 요금
final_price = base_price * (1 - discount) # 할인 + 할증이 모두 적용된 최종 요금 계산되는 부분
    
print(f"나이: {age}세")
print(f"학생 여부: {is_student}")
print(f"주말 여부: {is_weekend}")
print(f"할인율: {discount * 100}%")
# print(f"최종 요금: {final_price:,.0f}원")
print(f"최종 요금: {final_price:,.0f}원" if final_price>0 else "무료입장입니다")  # 행사 등의 이유로 요금이 0원일 경우 무료입장 문구 출력