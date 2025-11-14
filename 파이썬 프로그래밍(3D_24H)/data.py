import pandas as pd
import numpy as np


# ages = list(range(20, 41))

data = pd.DataFrame({
    'No': range(101),
    'name': np.random.choice(['김씨', '이씨', '박씨', '최씨', '현씨', '배씨', '임씨', '진씨'], 101), 
    'age': np.random.randint(20, 40, 101), 
    'city': np.random.choice(['서울', '대전', '대구', '부산'], 101), 
    'score': np.random.randint(0, 101, 101)
    })
data.to_csv('studydb.csv', index=False, encoding='utf-8-sig')