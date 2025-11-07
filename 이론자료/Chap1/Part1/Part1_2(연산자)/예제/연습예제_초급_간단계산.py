# 물건 가격 계산
price = 15000  # 물건 가격
quantity = 3   # 구매 수량

total = price * quantity
print(f"총 가격 : {total}원")  # 총 가격 : 45000원
print("총 가격 :", total, "원") 

# 거스름돈 계산
payment = 50000
change = payment - total
print(f"거스름돈 : {change}원")  # 거스름돈 : 5000원
print("거스름돈 :", change, "원")


# 거스름돈 단위별 계산
try:
    price = int(input("물건 가격: "))
    quantity = int(input("수량: "))
    payment = int(input("지불 금액: "))
    # 원하는 값 입력

    total = price * quantity
    print(f"\n총 금액: {total}원")

    # 💬 금액이 부족한 경우
    if payment < total:
        shortage = total - payment
        print(f"금액이 {shortage}원이 부족합니다.")
    else:
        change = payment - total
        print(f"거스름돈: {change}원\n")

        # 단위별 계산
        만원 = change // 10000; change %= 10000
        오천원 = change // 5000; change %= 5000
        천원 = change // 1000; change %= 1000
        오백원 = change // 500; change %= 500
        백원 = change // 100; change %= 100
        오십원 = change // 50; change %= 50
        십원 = change // 10; change %= 10

        # 결과 출력
        if 만원: print("만원권:", 만원, "장")
        if 오천원: print("오천원권:", 오천원, "장")
        if 천원: print("천원권:", 천원, "장")
        if 오백원: print("오백원:", 오백원, "개")
        if 백원: print("백원:", 백원, "개")
        if 오십원: print("오십원:", 오십원, "개")
        if 십원: print("십원:", 십원, "개")

except ValueError:
    print("⚠️ 숫자를 정확히 입력해주세요!")
