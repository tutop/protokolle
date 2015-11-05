import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
t = np.genfromtxt('mittelwert.txt',usecols=(0),unpack=True)
#leange = np.genfromtxt('Länge.txt',unpack=True)
terr=np.genfromtxt('fehlermittelwert.txt',unpack=True)
"""
l=unp.uarray(0.461,0.0001)
tges=unp.uarray(t,terr)

v=l/tges
"""
t=ufloat(0.916,0.001)
l=ufloat(0.461,0.001)
print(l/t)
