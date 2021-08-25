import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

data = pd.read_excel("D:/SLee/다이브/지하철 간격/테스트용2.xlsx", "Sheet1")

# 산점도+선형회귀선 그래프 용
sns.set_style("white")
fig = sns.lmplot(x="accidents", y="distance(mm)", data=data, palette="inferno", height=10)
fig.set(xlim=(0, 5), ylim=(0, 300))

# 행렬화
accidents = np.array(data.loc[:, "accidents"]).reshape((-1, 1))
distance = np.array(data.loc[:, "distance(mm)"]).reshape((-1,1))

# 선형회귀선 값 나타내기
model = LinearRegression()
model.fit(accidents, distance)
r_sq = model.score(accidents, distance)
print("coefficient of determination is ", r_sq)

# p-value
mod = sm.OLS(accidents, distance)
fii = mod.fit()
p_value = fii.summary2().tables[1]['P>|t|']
print('p-value for the regression is ', p_value)
print('p-value for the regression is %0.9f' % p_value)

# 그래프 그리기
plt.show()
