import time
import adi
import matplotlib.pyplot as plt
import numpy as np


sdr = adi.Pluto("ip:192.168.3.1")


sdr.rx_lo = int(2000e6 + 2e6 * 3)
sdr.tx_lo = int(2000e6 + 2e6 * 3)
sdr.sample_rate = 1e6
sdr.rx_buffer_size = 1024

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

signal = np.zeros(len(t))
non_zero_samples = 200
start_sample = 500
signal[start_sample:start_sample+non_zero_samples] = amplitude

sdr.tx_cyclic_buffer = True
sdr.tx_enabled = True
sdr.tx(sample)

plt.plot(t, signal)
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.title('Прямоугольный сигнал')
plt.grid(True)
plt.show()
sdr.close()
'''print(type(d[1]))
print(str_after)
plt.xlabel('sample')
plt.ylabel('ampl')
plt.plot(d)
plt.show()    '''