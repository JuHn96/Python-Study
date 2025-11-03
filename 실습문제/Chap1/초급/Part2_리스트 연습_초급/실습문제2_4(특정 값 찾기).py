scores = [75, 85, 92, 68, 88, 95, 72]

for i in scores:
    if i >= 80:
        print(i)

# ===============================================================

# # 강사님 코드
# scores = [75, 85, 92, 68, 88, 95, 72]

# print("80점 이상인 점수:")
# for score in scores:
#     if score >= 80:
#         print(score)

# ===============================================================


# # 리스트 컴프리헨션 사용
# high_scores = [score for score in scores if score >= 80]
# print(high_scores)