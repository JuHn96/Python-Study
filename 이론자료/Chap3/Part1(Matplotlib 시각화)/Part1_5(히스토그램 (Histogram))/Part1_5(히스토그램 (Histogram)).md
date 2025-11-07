## 히스토그램 (Histogram)

데이터의 분포를 확인할 때 사용합니다.

```python
# 정규분포 데이터 생성
data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor='black')
plt.xlabel('값')
plt.ylabel('빈도')
plt.title('데이터 분포')
plt.show()
```

### 여러 히스토그램 비교

```python
data1 = np.random.randn(1000)
data2 = np.random.randn(1000) + 2
plt.hist(data1, bins=30, alpha=0.5, label='데이터1')
plt.hist(data2, bins=30, alpha=0.5, label='데이터2')
plt.xlabel('값')
plt.ylabel('빈도')
plt.legend()
plt.show()
```