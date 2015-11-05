import numpy as np
from uncertainties import ufloat
#rechteck Stab

l=0.602
m=605.1
volumen=ufloat(1*(np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198])*l,np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198])*l))
dichte=m/volumen

print('volumen =',volumen)
print('dichte=',dichte)
