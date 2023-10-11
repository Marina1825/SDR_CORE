import time
import adi
import matplotlib.pyplot as plt
import numpy as np

sdr = adi.Pluto("ip: ****")#узнать
sdr.rx_lo = 2437000000

rx_real_data = []
rx_imag_data = []
wait_values = []
for r in range(30):# Сбор данных
    rx = sdr.rx()
    plt.clf()

    wait = np.mean(rx.imag)
    wait_values.append(wait)

    plt.xlabel("Время")
    plt.ylabel("Амплитуда " + str(wait))
    plt.plot(rx.real)
    plt.plot(rx.imag)
   
    plt.draw()
    plt.pause(0.05)
    if wait > 200:
        time.sleep(5)

    time.sleep(0.5)# Пауза

plt.show()
