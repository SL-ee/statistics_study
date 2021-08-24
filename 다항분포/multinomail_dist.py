import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.stats

# 시행 횟수
N = 30
# 각각의 확률 5, 6이 나올 확률이 높은 주사위
mu = [0.1, 0.1, 0.1, 0.1, 0.3, 0.3]
rv = sp.stats.multinomial(N, mu)
# print(rv)
np.random.seed(0)
# 주사위를 30번 던지는 행위를 10번
X = rv.rvs(10)

plt.boxplot(X)
plt.xlabel("dice")
plt.ylabel("sample value")
plt.show()
