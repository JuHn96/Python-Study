weight = 70  # kg
height = 1.75  # m

bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "저체중"
elif bmi < 23:
    result = "정상"
elif bmi < 25:
    result = "과체중"
else:
    result = "비만"

print(f"BMI: {bmi:.2f} > 판정: {result}")

print("-" * 40)