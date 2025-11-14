a = 15
b = 27
c = 19

max = 0 # 최대값을 저장할 변수

if a > b:                
    if a > c:
        max = a          
    else:
        max = c     
              
if b > a:
    if b > c:
        max = b
    else:
        max = c

if c > a:
    if c > b:
        max = c
    else:
        max = b




        

# 강사님 코드
# print(f"최대값: {max}")

# if a >b and a > c:
#     print(f"최대값: {a}")
# elif b > c:
#     print(f"최대값: {b}")
# else:
#     print(f"최대값: {c}")



# 더 간단한 방법
# print(f"가장 큰 수: {max(a, b, c)}")