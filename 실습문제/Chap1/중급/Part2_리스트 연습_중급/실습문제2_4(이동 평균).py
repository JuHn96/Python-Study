prices = [100, 102, 98, 105, 103, 107, 110, 108]
moving_avg = []

for i in range(len(prices)):
    if i == 0:
        avg = prices[i]
    elif i == len(prices) - 1:
        avg = prices[i]
    else:
        avg = (prices[i-1] + prices[i] + prices[i+1]) / 3
    moving_avg.append(round(avg, 2))

print(moving_avg)  # [100.0, 101.67, 101.67, 102.0, 105.0, 106.67, 108.33, 109.33]