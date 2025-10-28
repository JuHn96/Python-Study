fruits = ["사과", "바나나"]

# 추가
fruits.append("포도")           # 끝에 추가
fruits.insert(1, "딸기")        # 특정 위치에 추가
print(fruits)
fruits.extend(["수박", "참외"]) # 여러 개 추가
print(fruits)

# 삭제
fruits.remove("바나나")  # 값으로 삭제
print(fruits)
popped = fruits.pop()    # 마지막 요소 삭제 후 반환
print(fruits)
del fruits[0]            # 인덱스로 삭제
print(fruits)

# 기타
print(len(fruits))       # 길이
print("사과" in fruits)  # 포함 여부
print(fruits)
fruits.sort()            # 정렬
print(fruits)
fruits.reverse()         # 역순
print(fruits)