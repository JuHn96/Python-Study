# 두 사람의 관심사
person_a = {"영화", "음악", "운동", "독서", "여행"}
person_b = {"음악", "게임", "독서", "요리", "여행"}

# 공통 관심사
common = person_a & person_b
print(f"공통 관심사: {common}")

# A만 좋아하는 것
only_a = person_a - person_b
print(f"A만 좋아함: {only_a}")

# B만 좋아하는 것
only_b = person_b - person_a
print(f"B만 좋아함: {only_b}")

# 모든 관심사
all_interests = person_a | person_b
print(f"모든 관심사: {all_interests}")

# 유사도 계산 (자카드 유사도)
similarity = len(common) / len(all_interests)
print(f"관심사 유사도: {similarity:.2%}")