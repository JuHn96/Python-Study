# 섭씨를 화씨로 변환 (F = C * 9/5 + 32)
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit}°F")

# 화씨를 섭씨로 다시 변환
celsius_back = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {celsius_back}°C")