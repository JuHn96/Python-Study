import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows 기본 한글 폰트
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 데이터 로드 (미국 EPA 차량 연비 데이터)
#df = pd.read_csv("https://www.fueleconomy.gov/feg/epadata/vehicles.csv", low_memory=False)
df = pd.read_csv("./머신러닝, 딥러닝 기초다지기/머신러닝/라. 머신러닝 알고리즘 상세/1) 선형 회귀(Linear Regression)/실습 Tasks/vehicles.csv", low_memory=False)

# 올바른 컬럼명 사용: 'displ'이 엔진 배기량
df = df[['displ', 'cylinders', 'city08', 'co2TailpipeGpm']].dropna()

# 1. 데이터 시각화
print("=== 데이터 시각화 ===")
print(f"데이터 크기: {df.shape}")
print(f"컬럼: {df.columns.tolist()}")
print("\n데이터 통계:")
print(df.describe())

# 히스토그램으로 각 변수 분포 확인
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('데이터 분포 시각화', fontsize=16, fontweight='bold')

# 엔진 배기량 분포
axes[0, 0].hist(df['displ'], bins=30, alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('엔진 배기량 분포')
axes[0, 0].set_xlabel('배기량 (L)')
axes[0, 0].set_ylabel('빈도')

# 실린더 수 분포
axes[0, 1].hist(df['cylinders'], bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
axes[0, 1].set_title('실린더 수 분포')
axes[0, 1].set_xlabel('실린더 수')
axes[0, 1].set_ylabel('빈도')

# 도시 연비 분포
axes[1, 0].hist(df['city08'], bins=30, alpha=0.7, color='lightcoral', edgecolor='black')
axes[1, 0].set_title('도시 연비 분포')
axes[1, 0].set_xlabel('도시 연비 (mpg)')
axes[1, 0].set_ylabel('빈도')

# CO2 배출량 분포
axes[1, 1].hist(df['co2TailpipeGpm'], bins=30, alpha=0.7, color='gold', edgecolor='black')
axes[1, 1].set_title('CO2 배출량 분포')
axes[1, 1].set_xlabel('CO2 배출량 (g/mile)')
axes[1, 1].set_ylabel('빈도')

plt.tight_layout()
plt.show()

# 상관관계 히트맵
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=0.5, cbar_kws={"shrink": .8})
plt.title('변수 간 상관관계 히트맵', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# 설명 변수 및 타겟 지정
X = df[['displ', 'cylinders', 'city08']]
y = df['co2TailpipeGpm']

# 데이터 분할 및 학습
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 결과 출력
print("\n=== 모델 성능 평가 ===")
print(f"R² score: {model.score(X_test, y_test):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"R² score (sklearn): {r2_score(y_test, y_pred):.4f}")

# 2. 결과 시각화
print("\n=== 결과 시각화 ===")

# 실제값 vs 예측값 비교
plt.figure(figsize=(12, 5))

# 산점도
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.6, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('실제 CO2 배출량')
plt.ylabel('예측 CO2 배출량')
plt.title('실제값 vs 예측값')
plt.grid(True, alpha=0.3)

# 잔차 플롯
plt.subplot(1, 2, 2)
residuals = y_test - y_pred
plt.scatter(y_pred, residuals, alpha=0.6, color='green')
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('예측값')
plt.ylabel('잔차')
plt.title('잔차 플롯')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 계수 중요도 시각화
feature_names = X.columns
coefficients = model.coef_

plt.figure(figsize=(10, 6))
bars = plt.bar(feature_names, coefficients, color=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('선형 회귀 모델 계수', fontsize=16, fontweight='bold')
plt.xlabel('특성')
plt.ylabel('계수 값')
plt.grid(True, alpha=0.3, axis='y')

# 계수 값 표시
for bar, coef in zip(bars, coefficients):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{coef:.4f}', ha='center', va='bottom' if coef > 0 else 'top')

plt.tight_layout()
plt.show()

# 모델 성능 요약
print("\n=== 모델 성능 요약 ===")
print(f"절편 (Intercept): {model.intercept_:.4f}")
print("\n계수:")
for feature, coef in zip(feature_names, coefficients):
    print(f"  {feature}: {coef:.4f}")