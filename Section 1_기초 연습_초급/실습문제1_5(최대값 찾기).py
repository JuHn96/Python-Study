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

print(f"최대값: {max}")