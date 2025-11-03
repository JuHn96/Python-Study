# 인덱스와 값을 동시에
fruits = ["사과", "바나나", "포도"]

for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")
    
# 시작 인덱스 지정
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}번째: {fruit}")