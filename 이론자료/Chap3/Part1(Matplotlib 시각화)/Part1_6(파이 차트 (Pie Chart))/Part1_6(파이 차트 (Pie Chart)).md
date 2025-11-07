## 파이 차트 (Pie Chart)

비율을 표시할 때 사용합니다.

```python
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('비율 분포')
plt.show()
```

### 파이 차트 꾸미기

```python
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  

# 첫 번째 조각 띄우기
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('프로그래밍 언어 사용 비율')
plt.show()
```