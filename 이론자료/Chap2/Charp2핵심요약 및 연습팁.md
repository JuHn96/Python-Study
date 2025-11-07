## 💡 핵심 요약

### NumPy:

1. **배열 생성**: `np.array()`, `np.zeros()`, `np.arange()`
2. **인덱싱**: `arr[0, 0]`, `arr[:, 0]`, `arr[arr > 5]`
3. **연산**: 배열끼리 바로 계산, 브로드캐스팅
4. **집계**: `sum()`, `mean()`, `max()` + axis
5. **변형**: `reshape()`, `flatten()`, `T`

### Pandas:

1. **데이터 읽기**: `pd.read_csv()`, `df.head()`
2. **선택**: `df['열']`, `df.loc[]`, `df.iloc[]`
3. **필터링**: `df[df['age'] >= 30]`
4. **결측치**: `isnull()`, `fillna()`, `dropna()`
5. **그룹화**: `groupby()`, `value_counts()`

### 연습 팁:

- NumPy는 수치 계산에 강함
- Pandas는 표 데이터 처리에 강함
- 둘이 함께 사용하는 경우가 많음!
- 초급 → 중급 → 고급 예제를 순서대로 풀어보세요
