import numpy as np
from uncertainties import ufloat
import math
#rechteck Stab

l=0.602
m=605.1
rvolumen=ufloat(1*(np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198])*l,np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198])*l))
rdichte=m/rvolumen

print('Rechteckvolumen =',rvolumen)
print('Rechteckdichte=',rdichte)

#zylinder Stab.2

l=0.58
m=356.4
r=ufloat(0.5*np.mean([.01,.01,.01,.01,.01,.01,.01,0.098,0.098,0.098,]),0.5*np.std([.01,.01,.01,.01,.01,.01,.01,0.098,0.098,0.098,]))
zylvolumen=(np.pi*r*l)
zyldichte=m/zylvolumen

print('zylinderdichte=',zyldichte)
