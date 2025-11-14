# 5단 출력

for i in range(2, 10):
    dan = i
    print(f"=== {dan}단 ===")
    for i in range(1, 10):
          result = dan * i
          print(f"{dan} x {i} = {result}")