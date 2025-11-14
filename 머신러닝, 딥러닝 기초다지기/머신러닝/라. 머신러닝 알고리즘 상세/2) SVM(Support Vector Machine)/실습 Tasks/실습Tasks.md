# 실습 Tasks

## ✅ 1. **이메일 스팸 분류 (Spam vs Ham)**

- **설명**: 이메일 본문 내용을 분석하여 스팸 여부 분류
- **데이터셋**: [UCI SMS Spam Collection]
- **타입**: 이진 분류
- **실습 포인트**: 텍스트 전처리, TF-IDF 벡터화 후 SVM

---

## ✅ 2. **손글씨 숫자 인식 (Digit Classification)**

- **설명**: 8x8 혹은 28x28 이미지의 손글씨 숫자 이미지 분류
- **데이터셋**: `sklearn.datasets.load_digits()` 또는 MNIST
- **타입**: 다중 클래스 분류 (0~9)
- **실습 포인트**: 이미지 → 벡터 변환 후 분류

---

## ✅ 3. **붓꽃 품종 분류 (Iris Classification)**

- **설명**: 꽃받침과 꽃잎의 길이/너비로 세 가지 품종 분류
- **데이터셋**: `sklearn.datasets.load_iris()`
- **타입**: 다중 클래스 분류
- **실습 포인트**: SVM의 커널 종류(RBF, linear 등)에 따른 성능 비교

---

## ✅ 4. **유방암 진단 (Breast Cancer Classification)**

- **설명**: 종양 크기, 밀도 등 다양한 특성을 통해 악성/양성 분류
- **데이터셋**: `sklearn.datasets.load_breast_cancer()`
- **타입**: 이진 분류
- **실습 포인트**: 특성 스케일링 후 정확도 측정

---

## ✅ 5. **심장 질환 예측 (Heart Disease Prediction)**

- **설명**: 환자의 혈압, 심박수 등으로 심장질환 유무 예측
- **데이터셋**: [UCI Heart Disease Dataset]
- **타입**: 이진 분류
- **실습 포인트**: 특성 선택 + 파라미터 튜닝

---

## ✅ 6. **펭귄 종 분류 (Palmer Penguins)**

- **설명**: 펭귄의 부리 길이, 체중 등을 활용한 종 분류
- **데이터셋**: `seaborn.load_dataset("penguins")`
- **타입**: 다중 클래스 분류
- **실습 포인트**: 결측치 처리, 시각화, SVM 커널 비교

---

## ✅ 7. **이미지 얼굴 인식 (Face Recognition)**

- **설명**: 여러 사람의 얼굴을 이미지로 분류
- **데이터셋**: `sklearn.datasets.fetch_lfw_people()`
- **타입**: 다중 클래스 분류
- **실습 포인트**: 차원 축소(PCA) 후 SVM 적용

---

## ✅ 8. **음성 감정 분류 (Speech Emotion Recognition)**

- **설명**: 음성에서 특징(피치, 에너지 등)을 추출해 감정 분류
- **데이터셋**: [RAVDESS] 또는 [CREMA-D]
- **타입**: 다중 클래스 분류
- **실습 포인트**: 음성 피처 추출 + 표준화 후 SVM