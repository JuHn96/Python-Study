def rectangle_area(width, height):
    """직사각형 넓이 계산"""    
    return width * height
    
def rectangle_perimeter(width, height):
    """직사각형 둘레 계산"""    
    return 2 * (width + height)
    
# 사용
w = 5
h = 3
area = rectangle_area(w, h)
perimeter = rectangle_perimeter(w, h)

print(f"가로: {w}, 세로: {h}")
print(f"넓이: {area}")
print(f"둘레: {perimeter}")