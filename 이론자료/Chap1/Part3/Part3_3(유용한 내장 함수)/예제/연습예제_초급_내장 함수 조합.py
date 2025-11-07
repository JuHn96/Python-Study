# 여러 리스트 조합
names = ["김철수", "이영희", "박민수"]
math = [85, 92, 78]
english = [90, 88, 85]

# zip으로 묶어서 출력
print("=== 학생 성적 ===")
for i, (name, m, e) in enumerate(zip(names, math, english), 1):
    total = m + e
    print(f"{i}. {name}: 수학 {m}, 영어 {e}, 합계 {total}")

#=== 학생 성적 ===
#1. 김철수: 수학 85, 영어 90, 합계 175
#2. 이영희: 수학 92, 영어 88, 합계 180
#3. 박민수: 수학 78, 영어 85, 합계 163