# 기본 사용
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
    
# range(시작, 끝, 간격)
for i in range(1, 10, 2):
    print(i)  # 1, 3, 5, 7, 9
    
# 리스트 순회
fruits = ["사과", "바나나", "포도"]
for fruit in fruits:
    print(fruit)
    
# enumerate: 인덱스와 값을 동시에
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")