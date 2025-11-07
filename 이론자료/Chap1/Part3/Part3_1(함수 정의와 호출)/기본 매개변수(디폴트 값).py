def power(base, exponent=2): # 현재 이 부분에 2를 지정한건 입력받을 값이 없을때를 위한 디폴트값
    return base ** exponent
    
print(power(3))      # 9 (3^2)
print(power(3, 3))   # 27 (3^3)