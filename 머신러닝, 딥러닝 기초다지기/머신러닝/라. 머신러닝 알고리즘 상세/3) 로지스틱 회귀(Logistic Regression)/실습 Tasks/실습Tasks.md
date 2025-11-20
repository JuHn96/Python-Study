# 실습Tasks

### 1. **유방암 진단 (Breast Cancer Classification)**

- **목표**: 종양 특성 데이터를 기반으로 악성/양성 여부 분류
- **데이터셋**: `sklearn.datasets.load_breast_cancer()`
- **타입**: 이진 분류

---

### 2. **붓꽃 품종 분류 (Iris Classification)**

- **목표**: 꽃잎/꽃받침 크기로 3가지 품종 분류
- **데이터셋**: `sklearn.datasets.load_iris()`
- **타입**: 다중 클래스 분류
- **실습 포인트**: 다중 클래스에서 로지스틱 회귀 사용

---

### 3. **타이타닉 생존자 예측 (Titanic Survival Prediction)**

- **목표**: 승객의 나이, 성별, 선실 등으로 생존 여부 예측
- **데이터셋**: `Kaggle Titanic` or `seaborn.load_dataset("titanic")`
- **타입**: 이진 분류
- **실습 포인트**: 결측치 처리, 범주형 변수 인코딩

---

### 4. **심장병 예측 (Heart Disease Prediction)**

- **목표**: 환자의 특성으로 심장병 유무 예측
- **데이터셋**: [UCI Heart Disease Dataset]
- **타입**: 이진 분류
- **실습 포인트**: 정규화, 특성 선택, 성능 비교

---

### 5. **사회경제 정보로 은행 캠페인 응답 여부 예측**

- **목표**: 고객이 마케팅 캠페인에 참여할지 예측
- **데이터셋**: [UCI Bank Marketing Dataset]
- **타입**: 이진 분류
- **실습 포인트**: class imbalance, precision-recall 평가

---

### 6. **펭귄 종 분류 (Palmer Penguins)**

- **목표**: 펭귄의 부리 길이, 체중 등으로 종 분류
- **데이터셋**: `seaborn.load_dataset("penguins")`
- **타입**: 다중 클래스 분류
- **실습 포인트**: `multi_class='multinomial'` 설정

---

### 7. **이메일 스팸 필터링 (Spam Detection)**

- **목표**: 이메일 본문 내용을 기반으로 스팸 여부 분류
- **데이터셋**: SMS Spam Collection (UCI)
- **타입**: 이진 분류
- **실습 포인트**: 텍스트 → 벡터화 (TF-IDF)

---

### 8. **학생 성적 Pass/Fail 예측**

- **목표**: 출석률, 공부 시간 등을 기반으로 합격 여부 예측
- **데이터셋**: UCI Student Performance Dataset
- **타입**: 이진 분류
- **실습 포인트**: 확률 기반 예측, Threshold 조절