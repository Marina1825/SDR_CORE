import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.figure(figsize=(12, 7))

# график аналогового сигнала
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Аналоговый сигнал')
plt.xlabel('Время (t)')
plt.ylabel('Амплитуда (A)')
plt.grid()

# график дискретного сигнала
plt.subplot(2, 2, 2)
plt.stem(x, y)
plt.title('Дискретный сигнал')
plt.xlabel('Время (t)')
plt.ylabel('Амплитуда (A)')
plt.grid()

# график в виде квантованных уровней
plt.subplot(2, 1, 2)
plt.step(x, y)
plt.title('Квантованный график')
plt.xlabel('Время (t)')
plt.ylabel('Амплитуда (A)')
plt.grid()

plt.show()