from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 한글 폰트 설정 (Windows 기준, 나눔고딕 사용)
matplotlib.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

faces = fetch_lfw_people(min_faces_per_person=60)
X, y = faces.data, faces.target

# 데이터 정보 출력
print(f"데이터 shape: {X.shape}")
print(f"타겟 shape: {y.shape}")
print(f"클래스 개수: {len(faces.target_names)}")
print(f"클래스 이름: {faces.target_names}")

# 이미지 시각화 (처음 12장)
fig, axes = plt.subplots(3, 4, figsize=(10, 8))
for i, ax in enumerate(axes.flat):
    ax.imshow(faces.images[i], cmap='gray')
    ax.set_title(faces.target_names[faces.target[i]])
    ax.axis('off')
plt.suptitle('LFW 얼굴 샘플')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

pca = PCA(n_components=150, whiten=True)
model = make_pipeline(pca, SVC(kernel='rbf', class_weight='balanced'))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))

# Confusion matrix 시각화
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=faces.target_names)
disp.plot(xticks_rotation=45, cmap='Blues')
plt.title('Confusion Matrix')
plt.show()