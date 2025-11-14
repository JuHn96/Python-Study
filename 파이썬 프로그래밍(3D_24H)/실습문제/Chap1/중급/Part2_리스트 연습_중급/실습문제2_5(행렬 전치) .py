matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# zip과 리스트 컴프리헨션 사용
transposed = [list(row) for row in zip(*matrix)]

print(transposed)
