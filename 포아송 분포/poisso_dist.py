import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp

def pois_def(n, lamb):
    pd = exp(-lamb) * (lamb ** n) / factorial(n)
    return pd

# 0 ~ 39 numpy 어레이
x = np.arange(40)
# 각 x 값에 대한 확률질량함수 값을 갖는 어레이
# pd1 = np.array([pois_def(n, 10) for n in range(40)])
# plt.ylim(0, 0.15)
# # .text(x, y, s) 는 s의 위치 좌표값 x, y
# plt.text(34, 0.14, 'lamb = 10')
# plt.bar(x, pd1, color='lightcoral')
# plt.show()

plt.subplot(3, 1, 1)
pd1 = np.array([pois_def(n, 10) for n in range(40)])
plt.ylim(0, 0.15)
# .text(x, y, s) 는 s의 위치 좌표값 x, y
plt.text(33.5, 0.12, 'lamb = 10')
plt.bar(x, pd1, color='lightcoral')

plt.subplot(3, 1, 2)
pd2 = np.array([pois_def(n, 15) for n in range(40)])
plt.ylim(0, 0.15)
# .text(x, y, s) 는 s의 위치 좌표값 x, y
plt.text(33.5, 0.12, 'lamb = 15')
plt.bar(x, pd2, color='mediumaquamarine')

plt.subplot(3, 1, 3)
pd2 = np.array([pois_def(n, 20) for n in range(40)])
plt.ylim(0, 0.15)
# .text(x, y, s) 는 s의 위치 좌표값 x, y
plt.text(33.5, 0.12, 'lamb = 20')
plt.bar(x, pd2, color='royalblue')

plt.show()
