# 날짜 인덱스가 있는 DataFrame
dates = pd.date_range('2024-01-01', periods=10, freq='D')
# pd.date_range(start, periods, freq)
# start: 시작 날짜
# periods: 생성할 날짜 개수
# freq: 빈도/간격 ('D'=일, 'M'=월, 'H'=시간 등)
data = {
    'temperature': np.random.randint(20, 30, 10),
    'humidity': np.random.randint(40, 70, 10),
    'rainfall': np.random.randint(0, 50, 10)
}
weather = pd.DataFrame(data, index=dates)

print("날씨 데이터:\n", weather)
print("\n특정 날짜:", weather.loc['2024-01-05'])
print("\n특정 기간:\n", weather.loc['2024-01-03':'2024-01-07'])

# 주간 평균
weekly = weather.resample('W').mean()
print("\n주간 평균:\n", weekly)