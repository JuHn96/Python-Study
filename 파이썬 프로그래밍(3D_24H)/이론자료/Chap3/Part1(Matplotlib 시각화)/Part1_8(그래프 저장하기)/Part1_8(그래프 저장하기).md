## 그래프 저장하기

```python
x = range(10)
y = [i**2 for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('제곱 함수')

# 이미지로 저장
plt.savefig('graph.png', dpi=300, bbox_inches='tight')
plt.show()
```