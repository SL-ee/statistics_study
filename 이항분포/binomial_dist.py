import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def bin_dist (k, n, p):
    nck = factorial(n) / (factorial(k) * factorial(n - k))
    pd = nck * p**k * (1-p)**(n-k)
    return pd

# 0~15 정수 값을 갖는 numpy 어레이
x = np.arange(16)
# k = k번 성공, n = n번 독립시행, p = 성공할 확률
pd1 = np.array([bin_dist(k, 15, 1) for k in range(16)])
# y축 범위
plt.ylim(0, 0.3)
# (x,y,s) x,y 좌표 위치에 문자열 s를 나타낸다
plt.text(12.5, 0.28, 'n, p = 15, 0.3')
plt.bar(x, pd1, color='lightcoral')
plt.show()
