# break: 반복문 종료
for i in range(10):
    if i == 5:
        break    
    print(i)  # 0, 1, 2, 3, 4
    
# continue: 다음 반복으로 해당 값 건너뛰기
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4