import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import kaiserord, lfilter, firwin, freqz
from scipy import fftpack

Ts1 = 1e-3
fs1 = 1 / Ts1
f = (0.4 * np.pi * fs1) / (2 * np.pi)
t = np.arange(-5, 11) * Ts1
s = np.cos(f * t * (2 * np.pi))

plt.figure(1)

#график аналового сигнала
plt.subplot(3, 1, 1)
plt.plot(t, s)
plt.title('Аналоговый сигнал')
plt.xlabel('Время (t)')
plt.ylabel('Амплитуда (A)')
plt.grid()

#график дискретного сигнала
plt.subplot(3, 1, 3)
plt.stem(t, s)
plt.title('Дискретный сигнал')
plt.xlabel('Время (t)')
plt.ylabel('Амплитуда (A)')
plt.grid()

print("Аналоговая частота:", f)

plt.figure(2)

#спектр сигнала
sp = fftpack.fft(s)
freqs = np.arange(0, fs1, fs1 / len(s))
plt.stem(freqs, np.abs(sp))
plt.xlabel('Частота в герцах [Hz]')
plt.ylabel('Модуль спектра')

plt.show()
