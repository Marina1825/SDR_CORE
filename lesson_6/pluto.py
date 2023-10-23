import time
import adi
import matplotlib.pyplot as plt
import numpy as np


sdr = adi.Pluto("ip:192.168.3.1")


sdr.rx_lo = int(2400e6)
sdr.tx_lo = int(2400e6)
sdr.sample_rate = 1e6
sdr.rx_buffer_size = 1000


print(type(d[1]))
print(str_after)
plt.xlabel('sample')
plt.ylabel('ampl')
plt.plot(d)
plt.show()    