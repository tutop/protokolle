import numpy as np
from uncertainties import ufloat
import math

Id=ufloat( 0.0021,0.0009)
D=ufloat(0.013,0.005)

gewicht=0.16272
kopf=ufloat(np.mean([0.0155,0.031,0.0309]),np.std([0.0155,0.031,0.0309]))
höhekopf=0.0524
rumpf=ufloat(np.mean([0.0378,0.0391,0.0255,0.0260,0.0323,0.0396]),np.std([0.0378,0.0391,0.0255,0.0260,0.0323,0.0396]))
höherumpf=0.0962
beine=ufloat(np.mean([.0150,.0204,.0193,.0157]),np.std([.0150,.0204,.0193,.0157]))
längebeine=ufloat(np.mean([.155,.149]),np.std([.155,.149]))
arme=ufloat(np.mean([.015,.0165,.0148,.0148]),np.std([.015,.0165,.0148,.0148]))
längearme=ufloat(np.mean([.1377,.1340]),np.std([.1377,.1340]))

Tanliegend_data=np.array([3.15/5,3.20/5,3.18/5,3.23/5,3.24/5])
Tabspreitzend_data=np.array([4.7/5,4.73/5,4.73/5,4.67/5,4.64/5])
Tanliegend=ufloat(np.mean(Tanliegend_data),np.std(Tanliegend_data))
Tabspreitzend=ufloat(np.mean(Tabspreitzend_data),np.std(Tabspreitzend_data))

Ipuppe_anliegend=Tanliegend**2*D/(4*(math.pi)**2)
Ipuppe_abspreitzend=Tabspreitzend**2*D/(4*(math.pi)**2)

print('Anliegend',Ipuppe_anliegend)
print('Abspreitzend',Ipuppe_abspreitzend)

def zylinder(r,h):
    volume=math.pi*r**2*h
    return volume


zylkopf=zylinder(kopf/2,höhekopf)
zylrumpf=zylinder(rumpf/2,höherumpf)
zylbein=zylinder(beine/2,längebeine)
zylarm=zylinder(arme/2,längearme)

gesamtvolumen=2*zylarm+2*zylbein+zylrumpf+zylkopf

def teilmasse(a):
    return (a*gewicht/gesamtvolumen)

teilmassekopf=teilmasse(zylkopf)
teilmasserumpf=teilmasse(zylrumpf)
teilmassebein=2*teilmasse(zylbein)
teilmassearm=2*teilmasse(zylarm)

def I(m,d):
    return (m*(d/2)**2/2)
def I_(m,d,h):
    return (m*((d/2)**2/4+h**2/12))

#I Anliegend:

Ikopf=I(teilmassekopf,kopf)
Irumpf=I(teilmasserumpf,rumpf)
Ibein=I(teilmassebein,beine)+teilmassebein*(beine/2)**2
Iarm=I_(teilmassearm,arme,längearme)+teilmassearm*(rumpf/2+längearme/2)**2

Igesamt=Ikopf+Irumpf+2*Ibein+2*Iarm

print('I Anliegend',Igesamt)

#I Abspreitzend:

Ibeinab=I_(teilmassebein,beine,längebeine)+teilmassebein*(längebeine/2)**2

Igesamtab=Ikopf+Irumpf+2*Ibeinab+2*Iarm

print('I Abspreitzend',Igesamtab)


print('T pos 1=',Tanliegend_data,'\n',Tanliegend)
print('T pos 2=',Tabspreitzend_data,'\n',Tabspreitzend)
print(
gewicht, 'gewicht','\n',
kopf, 'kopf','\n',
höhekopf, 'höhekopf','\n',
rumpf, 'rumpf','\n',
höherumpf, 'höherumpf','\n',
beine, 'beine','\n',
längebeine, 'längebeine','\n',
arme, 'arme','\n',
längearme, 'längearme','\n')
