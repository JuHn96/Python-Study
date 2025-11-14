def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로"""    
    return celsius * 9/5 + 32
    
def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로"""    
    return (fahrenheit - 32) * 5/9
    
def celsius_to_kelvin(celsius):
    """섭씨를 켈빈으로"""    
    return celsius + 273.15
    
def kelvin_to_celsius(kelvin):
    """켈빈을 섭씨로"""    
    return kelvin - 273.15
    
# 통합 변환 함수    
def convert_temperature(value, from_unit, to_unit):
    """온도 단위 변환"""    
    # 일단 섭씨로 변환    
    if from_unit == "F":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "K":
        celsius = kelvin_to_celsius(value)
    else:  # C        
        celsius = value
        
    # 목표 단위로 변환    
    if to_unit == "F":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "K":
        return celsius_to_kelvin(celsius)
    else:  # C        
        return celsius

# 함수는 return문을 만나면 즉시 종료되고 값을 반환한다. 더이상 진행 안되고 함수 계산 종료

# 테스트
print(f"25°C = {convert_temperature(25, 'C', 'F'):.1f}°F")
print(f"77°F = {convert_temperature(77, 'F', 'C'):.1f}°C")
print(f"300K = {convert_temperature(300, 'K', 'C'):.1f}°C")