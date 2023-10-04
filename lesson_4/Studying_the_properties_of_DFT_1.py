from scipy.fftpack import fft , ifft , fftshift
import numpy as np
import matplotlib.pyplot as plt

fc = 10 # Частота косинуса
fs = 32*fc # частота дискретизации , избыточная

fc_2 = 10*2
fs_2 = 32*fc_2

t = np.arange(0 ,2 ,1/fs) # длительность сигнала 2 с
x = np.cos(2*np.pi*fc*t) # формирование временного сигнала

plt.plot(t, x)
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.title('Первая часть задания')
plt.show()