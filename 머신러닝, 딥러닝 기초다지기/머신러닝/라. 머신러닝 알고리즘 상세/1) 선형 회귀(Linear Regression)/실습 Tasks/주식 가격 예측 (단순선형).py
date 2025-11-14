import pandas as pd
from sklearn.linear_model import LinearRegression
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 그래프 스타일 설정
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# AAPL 데이터 다운로드
print("AAPL 데이터를 다운로드 중입니다...")
df = yf.download('AAPL', start='2023-01-01', end='2023-06-01')

# 데이터 확인
print("\n=== 데이터 정보 ===")
print(f"데이터 형태: {df.shape}")
print(f"컬럼: {list(df.columns)}")
print(f"데이터 기간: {df.index[0].strftime('%Y-%m-%d')} ~ {df.index[-1].strftime('%Y-%m-%d')}")

print("\n=== 데이터 미리보기 ===")
print(df.head())

print("\n=== 데이터 통계 ===")
print(df.describe())

# 다음날 종가를 예측 타겟으로
df['Target'] = df['Close'].shift(-1)
df.dropna(inplace=True)

# 특성과 타겟
X = df[['Close']]
y = df['Target']

# 모델 학습
model = LinearRegression()
model.fit(X, y)

# 예측에 사용할 최신 종가
latest_price = float(df['Close'].iloc[-1])  # float으로 명확히 변환
latest_price_input = np.array([[latest_price]])  # (1,1) 2차원 배열로 만듦

# 예측 수행
predicted_price = model.predict(latest_price_input)[0]

print(f"\n오늘 종가: {latest_price:.2f}")
print(f"내일 예측 종가: {predicted_price:.2f}")

# 시각화
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('AAPL Stock Price Analysis and Prediction', fontsize=16, fontweight='bold')

# 1. 주가 변동 추이
axes[0, 0].plot(df.index, df['Close'], linewidth=2, color='blue', alpha=0.7)
axes[0, 0].set_title('AAPL Stock Price Trend')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Stock Price (USD)')
axes[0, 0].grid(True, alpha=0.3)

# 2. 거래량
axes[0, 1].plot(df.index, df['Volume'], linewidth=2, color='green', alpha=0.7)
axes[0, 1].set_title('Trading Volume')
axes[0, 1].set_xlabel('Date')
axes[0, 1].set_ylabel('Volume')
axes[0, 1].grid(True, alpha=0.3)

# 3. 실제값 vs 예측값 산점도
y_pred = model.predict(X)
axes[1, 0].scatter(y, y_pred, alpha=0.6, color='red')
axes[1, 0].plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
axes[1, 0].set_title('Actual vs Predicted Values')
axes[1, 0].set_xlabel('Actual Close Price')
axes[1, 0].set_ylabel('Predicted Close Price')
axes[1, 0].grid(True, alpha=0.3)

# 4. 예측 결과
dates = df.index[-10:]  # 최근 10일
actual_prices = df['Close'].iloc[-10:]
predicted_prices = model.predict(df[['Close']].iloc[-10:])

axes[1, 1].plot(dates, actual_prices, 'o-', label='Actual Price', linewidth=2, markersize=6)
axes[1, 1].plot(dates, predicted_prices, 's-', label='Predicted Price', linewidth=2, markersize=6)
axes[1, 1].set_title('Recent 10 Days: Actual vs Predicted Price')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Stock Price (USD)')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 모델 성능 평가
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"\n=== 모델 성능 ===")
print(f"평균 제곱 오차 (MSE): {mse:.4f}")
print(f"결정 계수 (R²): {r2:.4f}")
print(f"모델 정확도: {r2*100:.2f}%")