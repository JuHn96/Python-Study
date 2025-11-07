def get_student_info():
    name = "김철수"    
    age = 20    
    grade = "A"    
    score = 95    
    return (name, age, grade, score)
    
# 튜플 언패킹
student_name, student_age, student_grade, student_score = get_student_info()

print(f"이름: {student_name}")
print(f"나이: {student_age}")
print(f"학점: {student_grade}")
print(f"점수: {student_score}")