import matplotlib.pyplot as plt
import numpy as np

def generate_sinusoid_sin(N, A, f0, fs, phi):
    T = 1/fs
    array = np.arange(N)
    x1 = A * np.sin( 2*f0*np.pi*array*T + phi )
    return x1

def generate_sinusoid_cos(N, A, f0, fs, phi):
    T = 1/fs
    array = np.arange(N)
    x2 = A * np.cos( 2*f0*np.pi*array*T + phi )
    return x2

N = 1000
A = 5
f0 = 440
fs = 200000
phi = 0
x1 = generate_sinusoid_sin(N, A, f0, fs, phi)
x2 = generate_sinusoid_cos(N, A, f0, fs, phi)

plt.figure(figsize=(10,4))
plt.subplot(121)
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.text(0, -3.7, "A * sin(w*f*t)", fontsize=9)
plt.plot(x1)
plt.subplot(122)
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.text(70, 3.7, "A * cos(w*f*t)", fontsize=9)
plt.plot(x2)
#plt.show()



