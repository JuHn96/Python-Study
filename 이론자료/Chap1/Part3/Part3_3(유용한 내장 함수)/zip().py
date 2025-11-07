# 여러 리스트를 묶기
names = ["Kim", "Lee", "Park"]
scores = [85, 92, 78]
ages = [20, 21, 22]

for name, score, age in zip(names, scores, ages): # zip() 함수는 여러 리스트를 동시에 묶어서 반복하는 함수
    print(f"{name}: {score}점, {age}세")
   
# 딕셔너리로 변환
student_dict = dict(zip(names, scores))
print(student_dict)  # {'Kim': 85, 'Lee': 92, 'Park': 78}