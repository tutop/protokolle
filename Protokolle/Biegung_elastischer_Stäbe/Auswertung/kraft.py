import numpy as np
g=9.81

#gewicht einseitig Rechteck und Zylinder
m1=1.0427

#gewicht zweiseitig Rechteck
m2=3.5527

def F(m):
    return m*g

F1=F(m1)
F2=F(m2)
print (F1,'\n',F2)
