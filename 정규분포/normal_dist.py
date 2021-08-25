import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.stats

np.random.seed(0)

plt.style.use('default')
# 그래프 창 크기
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 5

# 평균
mean = 20.0
# 
deviation = 5.0

x = np.linspace(0, 40, 1500)
y = (1 / np.sqrt(2 * np.pi * deviation**2)) * np.exp(-1/2 * ((x - mean) / deviation)**2)

plt.plot(x, y, alpha = 0.7, color="lightcoral",label="pdf of N(20,5)")
plt.xlabel('x')
plt.ylabel('f(x)')
# 범례 위치
plt.legend(loc="upper left")

# x1과 x2 사이에 있을 확률
rv = sp.stats.norm(mean, deviation)
x1, x2 = 15, 27
print(f"Prob ({x1} < x < {x2}) = ", rv.cdf(x2) - rv.cdf(x1))

plt.show()
