a = True
b = False

print(a and b)  # False (둘 다 참이어야 참)
print(a or b)   # True  (하나만 참이어도 참)
print(not a)    # False (반대)

# 실전 예시
age = 20
has_license = True
can_drive = age >= 18 and has_license # True