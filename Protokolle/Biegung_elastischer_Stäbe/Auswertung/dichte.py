import numpy as np
from uncertainties import ufloat
import math
#rechteck Stab

l=0.602
m=605.1
h=0.01
rvolumen=ufloat((np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198])*l*h,np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198])*l*h))
rdichte=m/rvolumen

print('Rechteckvolumen =',rvolumen)
print('Rechtec,kdichte=',rdichte)
print('b=',np.mean([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]),np.std([.012,.012,.012,.012,.012,.012,.012,.012,.012,.0198]))
#zylinder Stab.2

l=0.58
m=356.4
r=ufloat(np.mean([.01,.01,.01,.01,.01,.01,.01,0.098,0.098,0.098,])*0.5,np.std([.01,.01,.01,.01,.01,.01,.01,0.098,0.098,0.098,])*0.5)
zylvolumen=(np.pi*r*l)
zyldichte=m/zylvolumen

print('zylinderdichte=',zyldichte)
print('d=',r*0.5)
