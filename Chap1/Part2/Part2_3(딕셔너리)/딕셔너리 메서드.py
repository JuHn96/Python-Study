person = {"name": "Kim", "age": 25}

# 추가/수정
person["city"] = "Seoul"   # 추가
person["age"] = 26         # 수정

print(person)

# 삭제
del person["city"]
removed = person.pop("age")  # 삭제하고 값 반환
print(person)
print(removed)

# 조회
print(person.keys())    # 모든 키
print(person.values())  # 모든 값
print(person.items())   # 모든 (키, 값) 쌍

# 순회
for key, value in person.items():
    print(f"{key}: {value}")