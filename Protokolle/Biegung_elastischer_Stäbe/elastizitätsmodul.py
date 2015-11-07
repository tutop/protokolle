#(8) einseitig eingespannt
import numpy as np
from uncertainties import ufloat
from differenz import W1,W2,Q1,Q2,E1,E2,E1_,E2_
from kraft import F1,F2

# E=F/(2*I*msteig)
b=ufloat(np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]),np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]))
h=.01
I=1/12*b*h**3
print(I)

Erecht=F1/(2*W1*I)
print(Erecht)
