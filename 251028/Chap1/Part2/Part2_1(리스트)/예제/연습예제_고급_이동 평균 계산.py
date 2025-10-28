# 주가 데이터
prices = [100, 102, 98, 105, 103, 107, 110, 108, 112, 115]

# n일 이동 평균 계산
window = int(input("이동 평균 기간을 입력하세요 (예: 3): "))
moving_avg = []
for i in range(len(prices) - window + 1):
    window_data = prices[i:i+window]
    avg = sum(window_data) / window
    moving_avg.append(avg)
    
print(f"원본 데이터: {prices}")
print(f"{window}일 이동 평균: {moving_avg}")

# 리스트 컴프리헨션으로
moving_avg_short = [sum(prices[i:i+window])/window
                    for i in range(len(prices)-window+1)]
print(f"간단한 방법: {moving_avg_short}")

# 상승/하락 추세 판단
trends = []
for i in range(1, len(moving_avg)):
    if moving_avg[i] > moving_avg[i-1]:
        trends.append("상승")
    elif moving_avg[i] < moving_avg[i-1]:
        trends.append("하락")
    else:
        trends.append("보합")
print(f"추세: {trends}")

trends_short = ["상승" if moving_avg[i] > moving_avg[i-1]
                else "하락" if moving_avg[i] < moving_avg[i-1]
                else "보합"
                for i in range(1, len(moving_avg))]
print(f"간단한 방법 추세: {trends_short}")