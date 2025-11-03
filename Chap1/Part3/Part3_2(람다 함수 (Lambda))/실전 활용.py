# 리스트 정렬
students = [
    {"name": "Kim", "score": 85},
    {"name": "Lee", "score": 92},
    {"name": "Park", "score": 78}
]

# score 기준으로 정렬
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(sorted_students[0]["name"])  # Lee

# filter 함수와 함께
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]