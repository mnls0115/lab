import numpy as np
from scipy import stats

# 두 변수의 데이터 예시 (임의의 데이터)
variable1 = np.array([2.75,3,3.16666666666667,2,2.5,3,2.5,2.91666666666667,2.33333333333333,2.5,1.75,2.91666666666667,2.5])
variable2 = np.array([136.666666666667,187.5,90,55,145,55,187.5,62.5,230,146.5,70,220,62.5])

# 피어슨 상관계수 계산
correlation_coefficient1, p_value1 = stats.pearsonr(variable1, variable2)

# 스피어만
correlation_coefficient2, p_value2 = stats.spearmanr(variable1, variable2)

# 켄달
correlation_coefficient3, p_value3 = stats.kendalltau(variable1, variable2)

print('피어슨')
print(f"Pearson Correlation Coefficient: {correlation_coefficient1}")
print(f"P-value: {p_value1}")
print('==========================================')

print('스피어만')
print(f"Pearson Correlation Coefficient: {correlation_coefficient2}")
print(f"P-value: {p_value2}")
print('==========================================')

print('켄달')
print(f"Pearson Correlation Coefficient: {correlation_coefficient3}")
print(f"P-value: {p_value3}")
print('==========================================')