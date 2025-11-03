data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
min_v = min(data)
max_v = max(data)
normalized = [(x - min_v) / (max_v - min_v) for x in data]
print(normalized)
