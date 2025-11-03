students = {
    "김철수": {"나이": 20, "점수": 85},
    "이영희": {"나이": 21, "점수": 92},
    "박민수": {"나이": 20, "점수": 78}
}
# 여기에 코드 작성
for name in students.keys():
    print(name)

# 모든 학생의 이름 출력
# for student_name in students.keys():
#     print(student_name)

# print([student_name for student_name in students.keys()])  # 리스트로 출력(한줄로 출력됨)


# 이름과 나이 출력
# for student_name, info in students.items():
#     print(f"{student_name}: {info['나이']}세")

# students.items()는 students 딕셔너리에 values의 작은 딕셔너리를 가지고옴 for문 안에 있기 때문에 info에 임시로 한 학생의 값만 순차적으로 들어감
# 그리고 print에서 info['나이']로 info에 들어간 작은 딕셔너리에서 '나이'라는 키의 밸류값을 꺼내서 출력하는 방식
