import numpy as np
from uncertainties import ufloat
import math
#rechteck Stab

l=0.602
m=0.6051
h=0.01
rvolumen=ufloat((np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.01198])*l*h,np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.01198])*l*h))
rdichte=m/rvolumen

print('Rechteckvolumen =',rvolumen)
print('Rechtec,kdichte=',rdichte)
print('b=',np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]),np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]))
#zylinder Stab.2

l=0.58
m=0.3564
r=ufloat(np.mean([.01,.01,.01,.01,.01,.01,.01,0.0098,0.0098,0.0098,])*0.5,np.std([.01,.01,.01,.01,.01,.01,.01,0.0098,0.0098,0.0098,])*0.5)
zylvolumen=(np.pi*r**2*l)
zyldichte=m/zylvolumen

print('zylinderdichte=',zyldichte)
print('d=',r*2)
