import numpy as np
from uncertainties import ufloat
import math
# Ddyn=ufloat(0.02096,0.00008)
D=ufloat(0.013,0.005)
Id=ufloat( 0.0021,0.0009)

#zylgroß
gewichtg=1.9739
durchmesserg=0.08
höheg=ufloat(np.mean([0.1415,0.1405]),np.std([0.1415,0.1405]))

Tdata=np.array([8.35/5,8.27/5,10.07/6,8.41/5,8.40/5])
T=ufloat(np.mean(Tdata),np.std(Tdata))

Ig=T**2*D/(4*(math.pi)**2)
print ('I großer Zylinder',Ig)

Igtheo=gewichtg*(durchmesserg/2)**2/2
print('Igtheo=',Igtheo)

#zylklein
gewichtk=1.4359
durchmesserk=ufloat(np.mean([0.0851,0.085]),np.std([0.0851,0.085]))
höhek=ufloat(np.mean([0.0301,0.0302]),np.std([0.0301,0.0302]))

Tdata1=np.array([7.46/5,7.56/5,7.49/5,7.50/5,7.50/5])
T1=ufloat(np.mean(Tdata1),np.std(Tdata1))

Ik=T1**2*D/(4*(math.pi)**2)
print('I kleiner Zylinder',Ik)

Iktheo=gewichtk*(durchmesserk/2)**2/2
print('Iktheo=',Iktheo)

print('Tg=',Tdata)
print('Tk=',Tdata1)
print('Tgmittel=',T)
print('Tkmittel=',T1)
