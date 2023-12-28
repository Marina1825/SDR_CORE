# Задание на практику 


1. Для заданных значений частоты синала и частоты дискретизации получите дискретное колебание, отсчеты посмотрите в *Variable Explorer*. Далее увеличьте частоту сигнала в несколько раз, при этом так же увеличится и частота дискретизации, но отношение частоты сигнала и частоты дискретизации - **нормированная частота** останется той же величиной. Сравните дискретные отсчеты первого и второго сигналов.
2. Вычислите шаг частот между точками ДПФ `∆f=fs/N`. Определите, в какой точке ДПФ находится заданный сигнал.
3. Измените частоту сигнала в целое чисто раз, определите номер точки ДПФ для данного сигнала.
4. Измените количество точек ДПФ до *512*. Вычислите шаг частот между точками ДПФ `∆f=fs/N`. Определите, в какой точке ДПФ находится заданный сигнал.
5. Задайте сигнал в виде суммы двух колебаний. Вычислите ДПФ сигнала.
6. Вычислите ОДПФ сигнала, заданого в частотной области в виде **X=np.array([0,0,1,0,0,0,0,0])** Задавайте ненулевое значение в различных разрядах. Также задайте значение в комплексной форме **X=np.array([0,0,1j,0,0,0,0,0])**, поменяйте знак мнимой единицы, задайте спектр ДПФ в виде **X=np.array([0,0,2-1j,0,0,0,0,0])** поменяйте знак мнимой единицы. Можно увеличить количество точек до 16 при одном ненулевом значении.

*Доп задание:
используя код задания прошлой недели построить граффик fft*

# Выполнение

### №1

![../../photo_screenshots/screenshots_4.1.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.1.png)
![../../photo_screenshots/screenshots_4.2.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.2.png)
![../../photo_screenshots/screenshots_4.3.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.3.png)
![../../photo_screenshots/screenshots_4.4.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.4.png)
![../../photo_screenshots/screenshots_4.5.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.5.png)

По графикам видно что нормированная частота одинаковая

### 2. Вычислите шаг частот между точками ДПФ `∆f = fs/N`. Определите, в какой точке ДПФ находится заданный сигнал.

```py
∆f = fs/N = 320/256=1.25
# частота сигнала  fc=10
k=8
```

![../../photo_screenshots/screenshots_4.7.1.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.7.1.png)
![../../photo_screenshots/screenshots_4.7.2.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.7.2.png)

### №3

```py
∆f = fs/N = 320/256=1.25
# частота сигнала  fc=20, с постоянной частотой дискредитации
k=16
```

![../../photo_screenshots/screenshots_4.8.1.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.8.1.png)
![../../photo_screenshots/screenshots_4.8.2.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.8.2.png)

### №4
 
```py
∆f = fs/N = 320/512=0.625
# частота сигнала  fc=10
k=16
```

![../../photo_screenshots/screenshots_4.9.1.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.9.1.png)
![../../photo_screenshots/screenshots_4.9.2.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.9.2.png)

### №5



![../../photo_screenshots/screenshots_4.10.1.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.10.1.png)
![../../photo_screenshots/screenshots_4.10.2.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.10.2.png)


### 6. Вычислите *ОДПФ* сигнала, заданого в частотной области в виде `X=np.array([0,0,1,0,0,0,0,0])`. Задавайте ненулевое значение в различных разрядах. Также задайте значение в комплексной форме `X=np.array([0,0,1j,0,0,0,0,0])`, поменяйте знак мнимой единицы, задайте спектр ДПФ в виде `X=np.array([0,0,2-1j,0,0,0,0,0])`поменяйте знак мнимой единицы. Можно увеличить количество точек до 16 при одном ненулевом значении.

`X=np.array([0,0,1,0,0,0,0,0])`

![../../photo_screenshots/screenshots_4.11.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.11.png)


`X=np.array([0,0,1j,0,0,0,0,0])`

![../../photo_screenshots/screenshots_4.12.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.12.png)


`X=np.array([0,0,2-1j,0,0,0,0,0])`

![../../photo_screenshots/screenshots_4.13.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.13.png)


`X=np.array([0,0,2-1j,0,0,0,0,1])`

![../../photo_screenshots/screenshots_4.14.png](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.14.png)

### Работа с SDR

Требовалось вывести спектр частот 

![../../photo_screenshots/screenshots_4.15.jpg](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.15.jpg)
![../../photo_screenshots/screenshots_4.15.jpg](https://github.com/Marina1825/SDR_CORE/blob/main/photo_screenshots/screenshots_4.15.jpg)
