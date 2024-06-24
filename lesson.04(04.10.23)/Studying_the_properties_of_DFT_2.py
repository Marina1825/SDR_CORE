from scipy.fftpack import fft , ifft , fftshift
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.signal import max_len_seq
fc = 2e9
tau = np.array([0.5, 1, 1.3]) * 1e-6
a= np.array([1, 0.7, 0.3])
ff=np.arange(-5,5, 0.02) * 1e6
H1=np.transpose(a) * np.exp(-1j*2*np.pifc*tau)
H2 = np.exp(-1j*2*np.pi*tau[0]*ff)+np.exp(-1j*2*np.pi*tau[1]*ff)+np.exp(-1j*2*np.pi*tau[2]*ff)
HH = H1[0] * H2+H1[1] * H2+H1[2] * H2
plt.figure(1)
plt.plot(ff,abs(HH))