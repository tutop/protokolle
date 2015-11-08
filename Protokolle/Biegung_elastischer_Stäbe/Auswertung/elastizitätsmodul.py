#(8) einseitig eingespannt
import numpy as np
from uncertainties import ufloat
from differenz import W1,W2,Q1,Q2,E1,E2,E1_,E2_
from kraft import F1,F2
from dichte import r
import math

# E=F/(2*I*msteig)
b=ufloat(np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]),np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]))
h=.01
Ir=1/12*b*h**3

Iz=np.pi/4*r**4

Erecht=F1/(2*W1*Ir)
Ezyl=F1/(2*Q1*Iz)
Ezweilinks=F2/(48*Ir*E1)
Ezweirechts=F2/(48*Ir*E1_)

print('Ir=',Ir)
print('Iz=',Iz)
print('Erecht',Erecht)
print('Ezyl',Ezyl)
print('Ezweilinks',Ezweilinks)
print('Ezweirechts',Ezweirechts)
