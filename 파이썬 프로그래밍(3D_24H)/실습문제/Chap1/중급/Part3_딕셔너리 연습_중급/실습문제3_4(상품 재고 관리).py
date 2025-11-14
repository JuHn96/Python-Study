inventory = {
    "사과": {"가격": 1000, "재고": 50},
    "바나나": {"가격": 1500, "재고": 30},
    "포도": {"가격": 3000, "재고": 20}
}
# 다음 기능 구현:
# 1. 총 재고 가치 계산 (가격 × 재고의 합)
# 2. 재고가 25개 이하인 상품 찾기
# 3. 가장 비싼 상품 찾기

# 여기에 코드 작성
# 1. 총 재고 가치 계산
total_value = sum(item["가격"] * item["재고"] for item in inventory.values())
print(f"총 재고 가치: {total_value}원")

# 2. 재고가 25개 이하인 상품 찾기
low_stock_items = [item for item, details in inventory.items() if details["재고"] <= 25]
print(f"재고가 25개 이하인 상품: {low_stock_items}")

# 3. 가장 비싼 상품 찾기
most_expensive_item = max(inventory.items(), key=lambda x: x[1]["가격"])
print(f"가장 비싼 상품: {most_expensive_item[0]} ({most_expensive_item[1]['가격']}원)")