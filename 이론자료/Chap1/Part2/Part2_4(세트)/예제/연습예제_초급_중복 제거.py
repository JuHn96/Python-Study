# 출석 명단 (중복 있음)
attendance = ["김철수", "이영희", "김철수", "박민수", "이영희", "최동욱"]

# 중복 제거
unique_students = list(set(attendance))
print(f"전체 출석: {len(attendance)}명")
print(f"실제 인원: {len(unique_students)}명")
print(f"학생 명단: {unique_students}")