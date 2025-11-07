# 상품 데이터
products = [ # 리스트 안에 딕셔너리 구조
    {"name": "노트북", "price": 1500000, "rating": 4.5},
    {"name": "마우스", "price": 30000, "rating": 4.8},
    {"name": "키보드", "price": 80000, "rating": 4.3},
    {"name": "모니터", "price": 400000, "rating": 4.7}
]

# 가격 기준 정렬
by_price = sorted(products, key=lambda x: x["price"])
print("=== 가격순 ===")

for p in by_price:
    print(f"{p['name']}: {p['price']:,}원")
'''
마우스: 30,000원
키보드: 80,000원
모니터: 400,000원
노트북: 1,500,000원
'''
    
# 평점 기준 정렬 (높은 순)
by_rating = sorted(products, key=lambda x: x["rating"], reverse=True)
print("\n=== 평점순 ===")

for p in by_rating:
    print(f"{p['name']}: {p['rating']}점")
    
# 50만원 이하 제품만
affordable = list(filter(lambda x: x["price"] <= 500000, products))
print("\n=== 50만원 이하 ===")

for p in affordable:
    print(f"{p['name']}: {p['price']:,}원")
    
# 평점 4.5 이상이면서 100만원 이하
best_value = list(filter(
    lambda x: x["rating"] >= 4.5 and x["price"] <= 1000000,
    products
))
print("\n=== 가성비 제품 ===")

for p in best_value:
    print(f"{p['name']}: {p['price']:,}원, {p['rating']}점")