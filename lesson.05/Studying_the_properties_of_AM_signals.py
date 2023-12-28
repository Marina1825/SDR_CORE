from scipy.fftpack import fft, ifft,  fftshift, ifftshift
from scipy import signal
from scipy.signal import kaiserord, lfilter, firwin, freqz
import numpy as np
import matplotlib.pyplot as plt
 
Ns = 2048 
Tmax = 10 
dt=Tmax/(Ns-1)  
fs = 1/dt 
t=np.arange(0, 10,1/fs) 
Ac = 2 
fc = 4  
wc = 2*np.pi*fc
xc = np.cos(wc*t) 
Am = 1
fm = 0.5  
wm = 2*np.pi*fm
xm = np.cos(wm*t)
mu = Am/Ac
sam = Ac*(1+mu*xm)*xc

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t,sam)
plt.title('Колебание АМ ')
plt.xlabel('t')
plt.ylabel('$s_{AM}(t)$')
plt.subplot(2,1,2)
plt.plot(t,xm)

N=2048 
X = fft(sam,N)/N
plt.figure(2)
plt.subplot(2,1,1)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(X[0:100 ] )) 
plt.title('Спектр АМ сигнала')
plt.xlabel('f')
plt.ylabel('$s_{AM}(f)$') 
plt.subplot(2,1,2)
X1 = fft(xm,N)/N 
plt.stem(kf[0:100 ]   ,abs(X1[0:100 ] )) 

plt.show()

s_d = sam**2
plt.figure(3)
plt.plot(t,s_d)
plt.title('Колебание АМ при квадратичном детектировании')
plt.xlabel('t')
plt.ylabel('$s_{AM}(t)$') 

Xd = fft(s_d)/N
plt.figure(4)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100 ]   ,abs(Xd[0:100 ]  ))
plt.title('Спектр колебания АМ при кв.дет. ')
plt.xlabel('f')
plt.ylabel('$s_{AM}(f)$') 

n=50
fn =   fm/fs
taps=signal.firwin(n,fn)
d=2*signal.lfilter(taps,1.0,s_d)
plt.figure(5)
plt.stem(taps)
plt.title('Сигнал на выходе ФНЧ детектора ')
plt.xlabel('t')
plt.ylabel('$m(t)$') 

Xdd = fft(d)/N
plt.figure(6)
kf = np.arange(0, N)*fs/N
plt.stem(kf[0:100]  ,abs(Xdd[0:100] )) 
plt.title('Спектр сигнала на выходе ФНЧ детектора ')
plt.xlabel('f')
plt.ylabel('$m(f)$') 
plt.show()