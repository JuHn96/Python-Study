## 산점도 (Scatter Plot)

점으로 데이터를 표시합니다. 상관관계를 볼 때 유용합니다.

```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 4, 8, 10, 9, 11, 13, 14]

plt.scatter(x, y)
plt.xlabel('공부 시간')
plt.ylabel('시험 점수')
plt.title('공부 시간과 점수의 관계')
plt.show()
```
