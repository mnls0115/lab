import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.anova import AnovaRM

# 데이터 준비
# 여기서는 각 환자별로 0일, 2달, 3년 시점에서의 결과값을 포함하는 데이터 프레임을 생성합니다.
# 'Subject'는 각 환자를 식별하는 ID, 'Time'은 측정 시점, 'Value'는 측정 결과입니다.
data = {
    'Subject': ['1', '1', '1', '2', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '5'],
    'Time': ['0일', '2달', '3년', '0일', '2달', '3년', '0일', '2달', '3년', '0일', '2달', '3년', '0일', '2달', '3년'],
    'Value': [199
, 39
, 12.4
, 184
, 30.7
, 11.2
, 9
, 1.08
, 4.19
, 25.5
, 7.03
, 19
, 65.2
, 47
, 38.6
]
}
df = pd.DataFrame(data)

# Repeated Measures ANOVA 수행
anova = AnovaRM(df, depvar='Value', subject='Subject', within=['Time'])
res = anova.fit()

print(res.summary())




import numpy as np
from scipy.stats import friedmanchisquare



# 환자별 0일, 2달, 3년 시점의 결과값
# 이 데이터는 예제이며, 실제 데이터로 대체해야 합니다.
data_day_0 = np.array([199,184,9,25.5,65.2

])
data_month_2 = np.array([39,30.7,1.08,7.03,47

])
data_year_3 = np.array([12.4,11.2,4.19,19,38.6

])


# 환자별 0일, 2달, 3년 시점의 결과값
# 이 데이터는 예제이며, 실제 데이터로 대체해야 합니다.

# Friedman test 수행
stat, p = friedmanchisquare(data_day_0, data_month_2, data_year_3)

print('Statistics=%.3f, p=%.3f' % (stat, p))

# 유의 수준 0.05를 기준으로 결과 해석
if p > 0.05:
    print('같은 분포에서 나온 것으로 볼 수 있다. (중앙값에 차이가 없다)')
else:
    print('다른 분포에서 나온 것으로 볼 수 있다. (중앙값에 차이가 있다)')