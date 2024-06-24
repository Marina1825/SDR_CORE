from scipy.fftpack import fft , ifft , fftshift
import numpy as np
import matplotlib.pyplot as plt

fc = 20 # Частота косинуса
fs = 32*fc # частота дискретизации , избыточная

t = np.arange(0 ,2 ,1/fs) # длительность сигнала 2 с
x = np.cos(2*np.pi*fc*t) # формирование временного сигнала

N = 256#len(x)  # Количество точек в ДПФ
frequency_step = fs / N  # Шаг частоты между точками ДПФ
print(f"Шаг частоты между точками ДПФ: {frequency_step} Гц")

n = fc/frequency_step
print(f"Заданный сигнал надится в точке: {n}")

plt.plot(t, x)
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')
plt.show()

df= fs/N
X = fft(x,N)/N

k2 = np.arange(-N/2 ,N/2)
kf2=k2*df
X2 = fftshift(X) # сдвиг ДПФ на центр
plt.figure(2)
plt.stem(kf2,abs(X2))
plt.xlabel('Гц')
plt.ylabel('$x[k]$')

X = fft(x,N)/N
plt.figure(3)
k = np.arange(0 ,N)
plt.stem(k,abs(X)) # выводим модуль ДПФ в точках ДПФ
plt.xlabel('k')
plt.ylabel('$x[k]$')

X1=np.array([0,0,0,0,2+3j,0,0,0])
plt.figure(4)
x_ifft = N*ifft(X1,N)
t = np.arange(0, len(x_ifft))/fs
plt.plot(t ,np.real(x_ifft ))
#plt.stem(t ,np.real(x_ifft )) # временные отсчеты колебания
plt.xlabel('c')
plt.ylabel('$x[n]$') 
plt.show()