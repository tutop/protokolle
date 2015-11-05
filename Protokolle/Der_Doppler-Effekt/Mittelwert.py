import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

t = np.genfromtxt('zeitWagen.txt',usecols=(0),unpack=True)

a=0
b=0
while a <10:
    tmit=[]
    while b<5:
        tmit.append(t[b+a*5])
        b+=1
    #print(np.nominal_values(tmit))
    print((np.std(tmit,dtype=np.float64))/np.sqrt(5))
    a+=1
    b=0
