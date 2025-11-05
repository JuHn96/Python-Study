def analyze_grades(students):
    """성적 분석 함수"""
    total_students = len(students)

    # 1️⃣ 각 학생 평균 구하기
    averages = [sum(s["scores"]) / len(s["scores"]) for s in students]

    # 2️⃣ 전체 평균
    all_scores = [score for s in students for score in s["scores"]]
    overall_avg = sum(all_scores) / len(all_scores)

    # 3️⃣ 최우수 학생
    best_student = students[averages.index(max(averages))]["name"]

    # 4️⃣ 과목별 평균 (zip으로 과목별 묶기)
    subjects = list(zip(*[s["scores"] for s in students]))
    subject_avgs = [round(sum(sub) / len(sub), 1) for sub in subjects]

    # 5️⃣ 등급 분포 (90이상 A, 80이상 B, 나머지 C)
    grade_counts = {"A": 0, "B": 0, "C": 0}
    for avg in averages:
        if avg >= 90:
            grade_counts["A"] += 1
        elif avg >= 80:
            grade_counts["B"] += 1
        else:
            grade_counts["C"] += 1

    # 결과 딕셔너리로 반환
    return {
        "총인원": total_students,
        "전체평균": round(overall_avg, 1),
        "최우수학생": best_student,
        "과목별평균": subject_avgs,
        "등급분포": grade_counts
    }


# 테스트
students = [
    {"name": "김철수", "scores": [85, 90, 88]},
    {"name": "이영희", "scores": [92, 88, 95]},
    {"name": "박민수", "scores": [78, 82, 80]},
    {"name": "정지원", "scores": [88, 85, 90]},
    {"name": "최동욱", "scores": [95, 92, 98]}
]

result = analyze_grades(students)
print(result)
