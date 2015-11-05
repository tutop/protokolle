import numpy as np
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

x,y = np.genfromtxt('nü_hin_zurück.txt',usecols=(0,1),unpack=True)
delta=x-y
a=0
b=0
stufe=[]
while a<60:
    a+=6
    stufe.append(a)
    stufe.append(a)
    stufe.append(a)
    stufe.append(a)
    stufe.append(a)
    b+=1

np.savetxt(
    'delta_nü_hin_zurück.txt',
    np.column_stack([delta,stufe]),
    header='delta_nü''stufe',
)
delta1,stufe1=np.genfromtxt('Schwebung_delta_nü.txt',unpack=True)

print(linregress(stufe1,delta1))
print(linregress(stufe,delta))
