from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = load_iris()
X = data.data
y = data.target
target_names = data.target_names

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.figure() # 쉽게 말해 도화지 생성
for i, target_name in enumerate(target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=target_name)
    print(target_name)
    print(i)
    print(X_pca)
    print(y)
    
plt.legend()
plt.title("PCA on Iris Dataset")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()