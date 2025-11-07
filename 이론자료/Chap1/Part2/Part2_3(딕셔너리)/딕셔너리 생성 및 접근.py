# key: value 쌍으로 저장
student = {
    "name": "홍길동",
    "age": 20,
    "major": "AI",
    "grades": [90, 85, 95]
}

# Key로 접근
print(student["name"])        # 홍길동
print(student["grades"][0])   # 90

# 안전한 접근 - get()
print(student.get("name"))           # 홍길동
print(student.get("email", "없음"))  # 없음 (기본값)