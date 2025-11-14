## 서브플롯 (여러 그래프 한 번에)

```python
# 2x2 그리드로 4개 그래프
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 첫 번째 그래프 (0, 0)
x = range(10)
y = [i**2 for i in x]
axes[0, 0].plot(x, y)
axes[0, 0].set_title('선 그래프')

# 두 번째 그래프 (0, 1)
axes[0, 1].scatter(x, y)
axes[0, 1].set_title('산점도')

# 세 번째 그래프 (1, 0)
axes[1, 0].bar(x, y)
axes[1, 0].set_title('막대 그래프')

# 네 번째 그래프 (1, 1)
axes[1, 1].hist(np.random.randn(1000), bins=30)
axes[1, 1].set_title('히스토그램')
plt.tight_layout()  

# 자동 간격 조정
plt.show()
```