import numpy as np
from uncertainties import ufloat
import math

m=ufloat(np.mean([0.22341,0.22171]),np.std([0.22341,0.22171]))
durchmesser=0.035
d=0.5*0.02935
T=np.array([12.78/5.,14.25/5.,16.20/5.,18.43/5.,20.47/5.,23.18/5.,25.58/5.,28.32/5.,30.83/5.,33.27/5.])
a=np.array([0.01*(3.+d),0.01*(4.71+d),0.01*(6.84+d),0.01*(8.8+d),0.01*(10.92+d),0.01*(12.91+d),0.01*(14.9+d),0.01*(17.1+d),0.01*(19.+d),0.01*(21.65+d)])

def linregress(x, y):
    assert len(x) == len(y)

    x, y = np.array(x), np.array(y)

    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

    return A, A_error, B, B_error
print(linregress(a*a,T*T))
A,Aerr,B,Berr=linregress(a*a,T*T)


#T²=4pi²(Id+Izyl+m*a²)/D
höhe=0.02935
D=ufloat(0.013,0.005)

# Ddyn=ufloat(0.02096,0.00008)

Id=(B)*D/(4*(math.pi)**2)-2*m*(durchmesser**2/4+höhe**2/12) #Id für a=0

print('Id=',Id)
print('T=',T)
print('a=',a)
print('T²=',T*T)
print('a²=',a*a)
print('Izyl=',m*(durchmesser**2/4+höhe**2/12))
