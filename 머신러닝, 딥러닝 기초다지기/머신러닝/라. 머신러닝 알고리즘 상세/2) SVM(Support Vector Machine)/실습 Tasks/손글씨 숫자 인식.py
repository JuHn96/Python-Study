from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 라이브러리 추가
import matplotlib  # 폰트 설정을 위한 라이브러리 추가

# matplotlib에서 한글 폰트가 깨지지 않도록 폰트 설정
matplotlib.rc('font', family='Malgun Gothic')  # 윈도우의 경우 'Malgun Gothic' 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 기호 깨짐 방지

# 손글씨 숫자 데이터셋 불러오기
# load_digits() 함수는 8x8 이미지로 된 숫자 데이터를 제공합니다.
digits = load_digits()
X, y = digits.data, digits.target  # X: 이미지 데이터, y: 정답(라벨)

# 데이터 일부 확인 (처음 5개)
print("X shape:", X.shape)  # 데이터의 크기 출력
print("y shape:", y.shape)  # 라벨의 크기 출력
print("첫 5개 라벨:", y[:5])  # 처음 5개 라벨 출력
print("첫 5개 데이터:", X[:5])  # 처음 5개 데이터 출력

# 데이터 시각화 (처음 5개 이미지와 라벨)
plt.figure(figsize=(10,2))
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(digits.images[i], cmap='gray')  # 8x8 이미지를 시각화
    plt.title(f'Label: {digits.target[i]}')  # 해당 이미지의 라벨 표시
    plt.axis('off')  # 축 제거
plt.suptitle('처음 5개 손글씨 이미지')
plt.show()

# 학습용/테스트용 데이터 분리 (8:2 비율)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# SVM 분류기 생성 (RBF 커널, gamma=0.001)
model = SVC(kernel='rbf', gamma=0.001)
model.fit(X_train, y_train)  # 모델 학습

# 테스트 데이터로 예측 및 정확도 출력
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))  # 정확도 출력