import numpy as np

# 주가 데이터
prices = np.array([100, 102, 98, 105, 103, 107, 110, 108, 112, 115,
                   113, 118, 120, 117, 122, 125, 123, 128, 130, 127])
print("원본 데이터:", prices)

# 이동 평균 (5일)
window = 5
moving_avg = np.convolve(prices, np.ones(window)/window, mode='valid')
print(f"\n{window}일 이동평균:", moving_avg)
'''
1. np.convolve() - 컨볼루션(합성곱) 함수
두 배열의 합성곱 연산을 수행합니다.
2. np.ones(window)/window - 평균 계산용 커널
# 예: window = 3
np.ones(3)        # [1, 1, 1]
np.ones(3)/3      # [0.333, 0.333, 0.333]
→ 각 값에 1/3을 곱해서 평균을 구하는 가중치
3. mode='valid' - 완전히 겹치는 부분만 계산

원본 배열과 커널이 완전히 겹치는 구간만 결과로 반환
결과 길이: len(prices) - window + 1
'''
# 이동 표준편차
moving_std = np.array([prices[i:i+window].std()
                       for i in range(len(prices)-window+1)])
print(f"{window}일 이동 표준편차:", moving_std)

# 볼린저 밴드 (이동평균 ± 2*표준편차)
upper_band = moving_avg + 2 * moving_std
lower_band = moving_avg - 2 * moving_std
print(f"\n상단 밴드: {upper_band}")
print(f"하단 밴드: {lower_band}")

# 수익률 계산
returns = (prices[1:] - prices[:-1]) / prices[:-1] * 100
print(f"\n일일 수익률(%):", returns.round(2))
print(f"평균 수익률: {returns.mean():.2f}%")
print(f"변동성: {returns.std():.2f}%")