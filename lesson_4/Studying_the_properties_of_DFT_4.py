from scipy.fftpack import fft , ifft , fftshift
import numpy as np
import matplotlib.pyplot as plt

fc = 10*2 # Частота косинуса
fs = 320 # частота дискретизации , избыточная
fc_1 = 10

t = np.arange(0 ,2 ,1/fs) # длительность сигнала 2 с
x = np.cos(2*np.pi*fc*t)+np.cos(2*np.pi*fc_1*t) # формирование временного сигнала

N = 256 # Количество точек в ДПФ
frequency_step = fs / N  # Шаг частоты между точками ДПФ
print(f"Шаг частоты между точками ДПФ: {frequency_step} Гц")

n = fc/frequency_step
print(f"Заданный сигнал надится в точке: {n}")

plt.plot(t, x)
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.title('Пятая часть задания')
plt.show()

X = fft(x,N)/N
plt.figure(2)
k = np.arange(0 ,N)
plt.stem(k,abs(X)) # выводим модуль ДПФ в точках ДПФ
plt.xlabel('k')
plt.ylabel('$x[k]$')