'''
Author: wang w1838978548@126.com
Date: 2024-07-28 19:45:18
LastEditors: wang w1838978548@126.com
LastEditTime: 2024-07-28 20:11:41
FilePath: \Automation2\test\peak_find.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 生成一个包含噪声的正弦波信号
t = np.linspace(0, 1, 1000, endpoint=False)
x = np.sin(50.0 * 2.0*np.pi*t)
x += np.random.randn(len(t)) * 0.1

# 设计一个低通滤波器
b, a = signal.butter(4, 0.2, 'low')

# 对信号进行滤波
y = signal.lfilter(b, a, x)

# 绘制原始信号和滤波后的信号
plt.plot(t, x, label='Noisy signal')
plt.plot(t, y, label='Filtered signal')
plt.legend()
plt.show()
