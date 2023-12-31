from scipy import signal
from scipy.signal import max_len_seq
import matplotlib.pyplot as plt
import numpy as np
import adi
import time

sdr = adi.Pluto("ip:192.168.2.1")
sdr.rx_lo = int(900e6)
sdr.tx_lo = int(900e6)

fs = 600e3
Ft= 100e3
ns = fs/Ft
ts1 =np.array([0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1])
b = np.ones(int(ns))
def gen_sig():
    data=max_len_seq(6)[0]

    #Преобразование нулей и единиц последовательности в передаваемое сообщение 
    m=2*data-1
    #Ft= 100e3
    #fs = 600e3

    #ns = fs/Ft
    ts1 =np.array([0,0,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,1])

    #b = np.ones(int(ns)) #Коэффициенты фильтра интерполятора

    ts1t = 2*ts1-1

    x_IQ = np.hstack((ts1t,m))

    #x_IQ = m # формирование пакета 
    N_input = len(x_IQ)
    xup = np.hstack((x_IQ.reshape(N_input,1),np.zeros((N_input, int(ns-1)))))

    xup= xup.flatten()

    x1 = signal.lfilter(b, 1,xup)

    x=x1.astype(complex) # in complex

    xt=.5*(1+x) #комплексные отсчеты для adalm

    triq=2**14*xt # in format
    print(len(triq))
    return triq
    
data = gen_sig()


n_frame = len(data)
# sdr.tx(triq)
# sdr.rx_rf_bandwidth = 200000
# sdr.rx_destroy_buffer()
# sdr.tx_hardwaregain_chan0 = -10
# sdr.rx_buffer_size = 2*n_frame
# xrec1=sdr.rx()

sdr.tx(data)
rx_data = sdr.rx()
#plt.plot(rx_data)
plt.show()

def listen_efir(data,n_frame):
   
    for r in range(50):
        sdr.tx(data)
        sdr.rx_rf_bandwidth = 200000
        sdr.tx_destroy_buffer()
        sdr.tx_hardwaregain_chan0 = -10
        sdr.rx_buffer_size = 2*n_frame  
        rx_data = sdr.rx()
        plt.clf()
        plt.plot(rx_data)
        plt.draw()
        plt.xlabel('Гц')
        plt.ylabel('$x[k]$')
        plt.pause(0.05)
        time.sleep(0.1)

def rx_data_form(xrec):
    
    fsr=2*np.pi * rs/fs
    b2,a2 = signal.butter(10,fsr)
    y1 = signal.lfilter(b2,a2,xrec)
    #y2=signal.decimate(y1,ns)
    yf=np.convolve(np.abs(y1.real),b)
    y2=signal.decimate(yf,ns)
    y=np.correlate(y2, ts1)
    plt.figure(2)
    plt.plot(np.abs(y))
    ind = np.argmax(abs(y),axis=0)
    yy=y2[ind:ind+len(data)]
    
np.savetxt ("my_data2.csv", rx_data, delimiter=" , ")